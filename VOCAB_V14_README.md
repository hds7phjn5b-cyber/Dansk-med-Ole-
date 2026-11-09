# Dansk med Ole – Wortschatz und Audio (V14)

- **128 zusätzliche Vokabeln** auf den Stufen A1 bis C1: je acht neue Wörter in 16 bestehenden Lektionen.
- **236 Vokabeln insgesamt**, zuzüglich 72 Dialogsätze.
- **308 MP3-Dateien** sind unter `audio/` im GitHub-Repository enthalten (automatisch durch GitHub Actions erzeugt).
- **Offline-Unterstützung:** Der Service Worker lädt alle im Manifest aufgeführten MP3-Dateien für die Offline-Nutzung vor. Bei Fehlern nutzt die App nach Möglichkeit die dänische Gerätestimme.
- Der ursprüngliche Lernfortschritt bleibt durch unveränderte Lektionen- und Vokabelindizes erhalten.
- Die Aufnahmen wurden mit einer **synthetischen dänischen Computerstimme** erstellt; natürlichere Sprecheraufnahmen können später ersetzt werden.

## Audio-Wartung

Die GitHub-Aktion `.github/workflows/dansk-audio-v14.yml` erzeugt bei Änderungen an `index.html` oder `tools/generate_audio.py` automatisch neue Audio-Dateien, solange der Entwicklungsbranch existiert. Lokal: `python3 tools/generate_audio.py` (benötigt `espeak` und `ffmpeg`).

## Qualitätssicherung

Die JavaScript-Syntax wurde geprüft. GitHub-Actions hat die 308 MP3-Dateien erzeugt und die Manifest-Zuordnung stimmt vollständig. Die tatsächliche Sprachqualität sollte auf einem iPhone mit dänischer Muttersprache überprüft werden.
