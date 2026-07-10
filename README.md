## What this is
A small Flask-based web app that takes a URL, calls the ScreenshotBase API, saves the returned image to disk and shows a preview in the browser — useful for quickly generating website screenshots via a simple web UI.

### Stack
- **Language(s):** HTML (UI) + Python (server)
- **Framework / runtime:** Flask (single-file app)
- **Notable libraries:** Flask, requests, Jinja2 (templates), gunicorn

## How it's organized
Top-level (annotated):
```
README.md                      minimal README
requirements.txt               top-level pip requirements (Flask + deps)
screenshot-generator/          main application package
  app.py                       Flask app, request handling and API call
  requirements.txt             pip requirements for the app (same stack)
  templates/
    index.html                 Jinja2 HTML UI (form + preview)
  static/
    screenshot.png             example/generated screenshot (saved output)
```

How it fits together:
- The runtime entrypoint is screenshot-generator/app.py. It exposes "/" supporting GET and POST.
- On POST the app reads form values (url, format, full_page), builds a request to ScreenshotBase, writes the binary response to screenshot-generator/static/screenshot.<ext>, and renders templates/index.html with the saved file path to display the preview.
- Templates (templates/index.html) contain the form and preview UI (Bootstrap via CDN). The app uses the requests library to call the external ScreenshotBase API.

## How to run it
Shortest path (from repository root):

```sh
# create a venv and install dependencies
cd screenshot-generator
python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows (PowerShell)
# .\venv\Scripts\Activate.ps1

pip install -r requirements.txt

# set API key (the app also has a base-endpoint constant in app.py — see note)
export SCREENSHOTBASE_API_KEY="your_screenshotbase_api_key"

# run the Flask app
python app.py
# open http://127.0.0.1:5000
```

Alternative (production): run with gunicorn from screenshot-generator directory:
```sh
gunicorn app:app --bind 0.0.0.0:8000
```

Notes / caveats:
- The app expects an environment variable SCREENSHOTBASE_API_KEY (app.py reads it into API_KEY), but app.py also defines a constant SCREENSHOTBASE_BASE_ENDPOINT that already contains a query-string with an apikey and a default url — that looks accidental and should be fixed so the configured API key and dynamic URL are used correctly.
- Templates include form fields for viewport width/height and format, but app.py currently reads only url, format and full_page; viewport fields are present in the UI but not used.
- The app writes screenshots to screenshot-generator/static/screenshot.<ext>. Ensure the process has write permission to that directory and sanitize filenames if multiple concurrent users are expected.
