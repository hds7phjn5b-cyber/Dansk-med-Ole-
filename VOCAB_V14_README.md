# Dansk med Ole – Vokabeln und Aussprache (V15)

- 128 zusätzliche Vokabeln von A1 bis C1 gegenüber V13: 236 Vokabeln und 72 Dialogsätze.
- Insgesamt 308 MP3-Dateien unter `audio/`.
- **Stimme:** `da-DK-ChristelNeural`, eine weibliche dänische Neural-Stimme. Erzeugung mit `edge-tts`, Sprechtempo `-6%`.
- **Offline:** Der Service Worker verwendet ab V15 einen neuen Cache und speichert die Sprachdateien auf dem Gerät. Alte eSpeak-Dateien sollen nicht weiter ausgeliefert werden.
- Lernstände und Vokabelschlüssel werden nicht verändert.
- Falls eine MP3-Datei fehlt, versucht die App eine dänische Geräte-Stimme, bevorzugt eine als weiblich erkennbare.

## Neue Audiodateien erzeugen

GitHub Actions: `.github/workflows/dansk-audio-v14.yml` startet bei Änderungen an der Audio-Erzeugung oder an den Lektionen. Das Workflow-Skript ersetzt alte eSpeak-MP3s und committet die neuen Dateien automatisch auf dem jeweiligen Branch.

Lokal (benötigt Internetverbindung):
```sh
python3 -m pip install edge-tts
python3 tools/generate_audio.py
```
Eine erneute vollständige Erzeugung ist mit `FORCE_AUDIO=1 python3 tools/generate_audio.py` möglich. Nach der ersten Erzeugung werden nur MP3s neu geschrieben, wenn sich Stimme, Tempo oder Text ändern.

**Hinweis:** `edge-tts` verwendet einen externen Online-Sprachdienst ohne offiziellen SLA. Die vorhandenen fertigen MP3s spielen unabhängig davon offline; zukünftige automatische Regenerierung kann bei Änderungen des Dienstes scheitern. Die erzeugten Dateien und die Zuordnung im Audio-Manifest müssen vor einem Produktionsrelease überprüft werden.

## Test

1. GitHub-Actions-Lauf muss erfolgreich sein und 308 aktualisierte Dateien enthalten.
2. In der Cloudflare-Vorschau dänische Wörter und Dialogsätze abspielen.
3. Offline-Wiedergabe nach vollständiger Speicherung auf dem iPhone testen, einschließlich Tempo und Wiederholen.
