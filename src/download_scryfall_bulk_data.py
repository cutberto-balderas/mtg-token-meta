import shutil
from pathlib import Path
import requests

SCRYFALL_BULK_URL = "https://api.scryfall.com/bulk-data"
OUTPUT_FILE = "scryfall_data/scryfall_oracle_cards.jsonl.gz"
Path(OUTPUT_FILE).parent.mkdir(parents=True, exist_ok=True)

session = requests.Session()
session.headers.update({
    "User-Agent": "mtg-token-meta/0.2 (GitHub: cutberto-balderas; https://github.com/cutberto-balderas/mtg-token-meta)",
    "Accept": "application/json",
})


def get_oracle_cards_entry():
    """ Fetch the Scryfall bulk-data manifest and return the oracle_cards entry."""
    print("Fetching Scryfall bulk-data manifest...")
    resp = session.get(SCRYFALL_BULK_URL, timeout=60)
    resp.raise_for_status()
    manifest = resp.json()

    entry = next(
        (x for x in manifest.get("data", []) if x.get("type") == "oracle_cards"),
        None,
    )
    if not entry:
        raise RuntimeError("Could not find Scryfall oracle_cards bulk data entry.")
    
    return entry


def download_oracle_bulk(output_path=OUTPUT_FILE):
    """Download the Scryfall oracle_cards bulk data to the specified output path."""
    output_path = Path(output_path)

    entry = get_oracle_cards_entry()
    download_uri = entry.get("jsonl_download_uri")
    if not download_uri:
        raise RuntimeError(
            f"No 'jsonl_download_uri' found in oracle_cards entry: {entry}"
        )

    print(f"Found oracle_cards entry updated at: {entry.get('updated_at')}")
    print(f"Downloading from: {download_uri}")

    r = session.get(download_uri, timeout=300, stream=True)
    r.raise_for_status()

    with open(output_path, "wb") as f:
        shutil.copyfileobj(r.raw, f)

    print(f"Saved JSONL to {output_path}")
    print(f"File size: {output_path.stat().st_size} bytes")


if __name__ == "__main__":
    download_oracle_bulk()