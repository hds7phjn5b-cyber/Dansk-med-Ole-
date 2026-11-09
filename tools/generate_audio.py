#!/usr/bin/env python3
"""Generate all Danish lesson MP3s with a natural Danish female neural voice.

Run from the repository root:
    python3 -m pip install edge-tts
    python3 tools/generate_audio.py

Requires an internet connection for generation; finished MP3s play offline.
Previously generated eSpeak files are replaced when the voice/text differs.
"""
import asyncio
import json
import os
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parent.parent
VOICE = "da-DK-ChristelNeural"
RATE = "-6%"
MIN_BYTES = 1000


def get_lesson_entries():
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    start = html.index("const lessons=") + len("const lessons=")
    end = html.index(";\nconst audioFiles=", start)
    lessons = json.loads(html[start:end])
    for n, lesson in enumerate(lessons):
        for part in ("d", "v"):
            for i, pair in enumerate(lesson[part]):
                yield {"path": f"audio/{n}-{part}-{i}.mp3",
                       "danish": pair[0], "voice": VOICE, "rate": RATE}


async def generate_clip(entry):
    path = ROOT / entry["path"]
    temp = path.with_suffix(".mp3.part")
    # Do not leave an incomplete file in the released audio directory.
    try:
        for attempt in range(4):
            try:
                if temp.exists():
                    temp.unlink()
                await asyncio.wait_for(
                    edge_tts.Communicate(
                        entry["danish"], voice=VOICE, rate=RATE
                    ).save(str(temp)),
                    timeout=75,
                )
                if not temp.exists() or temp.stat().st_size <= MIN_BYTES:
                    raise RuntimeError("Empty or unusually small MP3 received")
                temp.replace(path)
                return
            except Exception as error:
                if attempt == 3:
                    raise RuntimeError(
                        f"Audio generation failed for {entry['path']}: {error}"
                    ) from error
                print(f"Retry {attempt + 1}/3 for {entry['path']}: {error}", flush=True)
                await asyncio.sleep(2 ** attempt)
    finally:
        temp.unlink(missing_ok=True)


async def main():
    entries = list(get_lesson_entries())
    paths = {entry["path"] for entry in entries}
    if len(paths) != len(entries):
        raise ValueError("Duplicate MP3 file names in lessons")

    output_dir = ROOT / "audio"
    output_dir.mkdir(exist_ok=True)
    manifest_path = ROOT / "audio-manifest.json"
    try:
        previous = {entry["path"]: entry
                    for entry in json.loads(manifest_path.read_text(encoding="utf-8"))}
    except (OSError, ValueError, KeyError, TypeError):
        previous = {}

    generated = 0
    kept = 0
    for entry in entries:
        path = ROOT / entry["path"]
        old = previous.get(entry["path"])
        if (old == entry and path.is_file() and path.stat().st_size > MIN_BYTES
                and not os.environ.get("FORCE_AUDIO")):
            kept += 1
            continue
        await generate_clip(entry)
        generated += 1
        if generated % 20 == 0:
            print(f"Generated {generated}/{len(entries)} Danish MP3s...", flush=True)
        await asyncio.sleep(0.15)

    manifest_path.write_text(
        json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Voice {VOICE}, rate {RATE}; generated {generated}, "
          f"kept {kept}, total {len(entries)} MP3 clips.", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
