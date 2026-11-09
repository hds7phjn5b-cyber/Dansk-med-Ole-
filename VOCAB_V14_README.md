# Dansk med Ole – Wortschatz und Aussprache (V15)

- 128 zusätzliche Wörter auf A1–C1, insgesamt 236 Vokabeln und 72 Dialogsätze.
- 308 vorhandene MP3-Dateien unter `audio/` – weiterhin als Fallback verfügbar.
- **Neue bevorzugte Sprachausgabe:** die dänische Gerätestimme des Browsers statt der alten, robotisch klingenden eSpeak-Aufnahmen. Der automatische Modus bevorzugt weibliche dänische Stimmen anhand ihrer Namen (z. B. „Sara“).
- Ein neues Auswahlfeld „Stimme“ zeigt die auf dem Gerät vorhandenen dänischen Stimmen. Man kann eine konkrete Stimme wählen oder die bisherigen MP3s aktivieren.
- Falls die Geräte-Vorlesefunktion ausfällt, versucht die App die vorhandene MP3-Datei.
- Das Sprechtempo bleibt einstellbar.
- Die V15-Service-Worker-Cachekennung lädt die aktualisierte App neu; vorhandener Lernfortschritt bleibt erhalten.

## Wichtig zur Sprachqualität

Welche dänischen weiblichen Stimmen auswählbar sind, hängt von iPhone, Browser und installierten Systemstimmen ab. **Es wurden noch keine neuen Frauenstimmen-MP3-Dateien erstellt.** Die vorhandenen MP3s sind weiterhin mit eSpeak erzeugt.

Ein Versuch, 308 MP3s online mit der dänischen weiblichen Neural-Stimme `da-DK-ChristelNeural` zu erzeugen, scheiterte an wiederholten Ausfällen des Online-Sprachdienstes. Dieser nicht zuverlässige Generierungsweg wurde daher nicht in den Produktions-Workflow übernommen.

## Prüfung

1. JavaScript-Syntax prüfen.
2. In der Cloudflare-Vorschau „Stimme“ öffnen und die dänischen Einträge auf dem iPhone testen.
3. Bei einer weiblichen Stimme (etwa Sara) Wörter und Dialoge anhören, anschließend Wiederholen, Tempo und Offline-Betrieb prüfen.
4. Erst nach Hörtest eine neue MP3-Produktion in Betracht ziehen.
