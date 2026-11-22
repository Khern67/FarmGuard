# FarmGuard — Flask Web Application

A Flask + HTML + CSS + JavaScript conversion of the supplied Streamlit FarmGuard prototype. SQLite is used for persistence. The existing classification rules and DSA modules are retained.

## Run locally
1. Install Python 3.10+.
2. Open a terminal in this folder.
3. (Recommended) Create a virtual environment: `python -m venv .venv`
4. Activate it, then install: `pip install -r requirements.txt`
5. Start: `python app.py`
6. Open `http://127.0.0.1:5000`.

## Phase 2 functionality
- Edit crop records and open a crop-specific observation timeline.
- View full observation details and mark pending reports as inspected.
- Owner-only user management: create Owner/Worker accounts and activate or deactivate accounts.
- Role-based controls: Workers can submit observations and inspect reports; Owners manage crops, farms, coordinates, and user accounts.
- Interactive Leaflet map for crop plots with verified coordinates (requires internet access for map tiles).
- Responsive mobile navigation and layouts.

## Demo accounts
- Owner: `admin` / `farmguard123`
- Worker: `worker` / `worker123`

Demo credentials and the fallback Flask secret key are for local demonstration only. Set the `FARMGUARD_SECRET_KEY` environment variable and change demo passwords before deployment. This educational prototype still needs production hardening, including CSRF protection, HTTPS, stronger validation, and a secure deployment configuration.

## Data Structures and Algorithms
- Max Heap: ranks pending inspection reports by urgency.
- Tree ADT: builds the farm → crop → section hierarchy on the Farm Management page.
- Linked List: constructs the ordered observation history stream.
- Hash Table: indexes crop records by ID during request processing.
- Merge Sort: sorts the observation history for display.

## Classification note
Severity thresholds are the prototype rules supplied with the original project. They are inspection-triage aids, not validated crop-disease standards, diagnoses, or treatment recommendations. Have an agriculture adviser review the thresholds before relying on them in real farming decisions.
