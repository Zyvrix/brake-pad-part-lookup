# Brake Pad Part Lookup

## Open the site

After enabling GitHub Pages for the `main` branch, open the repository's Pages URL. The home page redirects to `part_lookup.html`.

The site loads its part catalogue from `parts.json`, which must stay beside `part_lookup.html`.

## Test QR scanning on a phone

1. Open the Pages URL on the phone using HTTPS.
2. On another screen, open the site's `part_lookup.html#labels` page and display a generated QR label.
3. On the phone, tap **Scan QR**, allow camera access, and point the rear camera at that label.

The browser must support camera access and be allowed to use it. If scanning is unavailable, enter a part number such as `BP-1001` in the search field.

## Update the catalogue

Edit `parts.json` to update the published part data. The Excel workbook and Python exporter are not required to run the hosted site.
