#!/usr/bin/env python3
"""Create Danish MP3 clips for every dialogue line and vocabulary card.
Run from the project root: python3 tools/generate_audio.py
Requires espeak and ffmpeg (available via apt on Ubuntu).
"""
from pathlib import Path
import json
import subprocess

root = Path(__file__).resolve().parent.parent
html = (root / 'index.html').read_text(encoding='utf-8')
start = html.index('const lessons=') + len('const lessons=')
end = html.index(';\nconst audioFiles=', start)
lessons = json.loads(html[start:end])
audio_dir = root / 'audio'
audio_dir.mkdir(exist_ok=True)
count = 0
skipped = 0
manifest = []
for n, lesson in enumerate(lessons):
    for part in ('d', 'v'):
        for i, pair in enumerate(lesson[part]):
            danish = pair[0]
            filename = f'{n}-{part}-{i}.mp3'
            output = audio_dir / filename
            manifest.append({'path': f'audio/{filename}', 'danish': danish})
            if output.is_file() and output.stat().st_size > 1000:
                skipped += 1
                continue
            wav = subprocess.run(['espeak','-v','da','-s','135','--stdout',danish], stdout=subprocess.PIPE, check=True).stdout
            result = subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i','pipe:0','-codec:a','libmp3lame','-q:a','5','-ar','22050',str(output)],input=wav,capture_output=True)
            if result.returncode or output.stat().st_size < 1000:
                raise RuntimeError(f'Could not generate {filename}: {result.stderr.decode()}')
            count += 1
(root / 'audio-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n',encoding='utf-8')
print(f'Generated {count}, kept {skipped}, total {len(manifest)} Danish MP3 clips.')
