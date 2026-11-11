# Acadia dark-sky planner

A planning toolkit for comparing vacation rentals around Acadia National Park (Mount Desert Island, the Schoodic Peninsula, and nearby mainland towns), with an emphasis on darker skies (Bortle class and sky-quality estimates), winter practicality, and group capacity.

This is a personal planning project by [Shaun Barry](https://shaun-barry-portfolio.vercel.app). Listing details and prices were collected from public Airbnb and Vrbo pages and can go stale — confirm everything with the host before booking.

## What's in this repo

Scripts and the processed datasets needed to rebuild the comparison:

| File | Role |
|---|---|
| `parse.py` | Extract stay results from a saved Airbnb search HTML page |
| `fetch.sh` | Download listing pages for the IDs in `ids.txt` into a local `pdp/` cache (not committed) |
| `bortle.py` | Look up sky quality and Bortle class for listing coordinates (via [Clear Outside](https://clearoutside.com/)) |
| `build.py` | Join listing data, manual notes, and sky-quality scores into `rows.json`, ranked for darker-sky value |
| `all.json`, `det.json`, `bortle.json`, `ids.txt` | Processed inputs |
| `rows.json`, `data.txt`, `short.txt` | Ranked comparison table and notes |

## What is not included

Raw scraped search and listing HTML (`s_*.html`, `pdp/`, and similar cache files) and Python `__pycache__` are excluded. They were large, easily re-fetched, and don't belong in git. No committed file is over 50 MB.

## How to use

```bash
python3 parse.py path/to/search.html
# optional: bash fetch.sh    # refreshes pdp/ from ids.txt
python3 bortle.py
python3 build.py             # writes rows.json and prints a ranked table
```

Requires Python 3 and `curl`.

## Notes

Sky-quality values are estimates at rounded coordinates, not on-site measurements. Prices are dated quotes from the collection window and should not be treated as current rates.
