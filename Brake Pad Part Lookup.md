# Brake Pad Part Lookup

## Run locally

1. Install Python, then install the exporter dependencies with `python -m pip install pandas openpyxl`.
2. From this folder, run `python excel_to_json.py` to generate `parts.json` from `brake_pads_parts.xlsx`.
3. Start a local web server with `python -m http.server 8000`.
4. Open `http://localhost:8000/part_lookup.html` in a browser. Do not open the HTML file directly; the app fetches `parts.json`.
5. Edit the `CONTACT` object near the top of `part_lookup.html` with your business details.

## Publish

Upload `part_lookup.html` and `parts.json` to the same folder on a static host. On GitHub Pages, publish the repository and visit the page at `https://<username>.github.io/<repository>/part_lookup.html`. On Netlify, deploy the folder and visit `/part_lookup.html` on the deployed site. The Excel workbook and Python exporter are only needed when updating the parts data.

## QR labels

Open the page and add `#labels` to its address. Each generated QR code now contains that part's details as plain text, so a phone's built-in QR scanner can read the details without opening the website or needing an internet connection. Print the labels or download each PNG. Previously printed URL-based QR codes still need a network connection; regenerate and reprint those labels to use the offline format.
