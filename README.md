# City of South Lyon, Michigan: council wiki

Transcripts of City of South Lyon, Michigan city council meetings, and the agendas, packets and minutes as Markdown. Not run by the city.

**Unofficial.** Transcripts and conversions are machine-made and can contain errors. The city's own minutes and the meeting videos are the record. Every page links to its original source. No text here is written by an AI model: pages are filled in from the sources by templates.

## What is here

| Folder | Contents |
|---|---|
| `docs/meetings/` | one page per meeting: video, documents, who was there, who spoke |
| `docs/transcripts/` | full transcripts, each paragraph linked to its moment in the video |
| `docs/documents/` | agendas, packets and minutes converted to Markdown (source URL, SHA-256 and a link to each original page) |
| `docs/people/`, `docs/years/` | officials and staff with their dates and sources; meetings by year |
| `exports/transcripts/` | the same transcripts as standalone Markdown files |

All of it is plain Markdown, so you can read it here or download it. Scanned documents were read by OCR; where a page needed that, the page says so and links to the original PDF.

## Privacy

In public comment, home addresses, phone numbers, e-mail addresses and "my name is" introductions are replaced by software with `[address redacted]`, `[contact redacted]` or `[name redacted]`. This is automatic and can miss things. The meeting videos and the city's own documents are not changed. To report a mistake or ask for something to be removed, open an issue in this repository (describe where it is; do not repeat the personal information) or see the About page.

## How the site is built

`mkdocs build` (pinned in `requirements.txt`) turns `docs/` into the website; `hooks.py` and `overrides/` add the Markdown download links. The files in `docs/` and `exports/` are generated from a private library by a separate tool; edit those at the source, not here.
