import gzip
import json
from pathlib import Path

INPUT_FILE = Path("scryfall_data/scryfall_oracle_cards.jsonl.gz")
OUTPUT_FILE = Path("scryfall_data/scryfall_token_data.json")
Path(OUTPUT_FILE).parent.mkdir(parents=True, exist_ok=True)

def iter_cards(path):
    """Read Scryfall JSONL.GZ one card at a time."""
    with gzip.open(path, "rt", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue


def build_token_index(cards):
    """Build an index of token cards made by Magic: The Gathering cards by name from the same bulk data file."""
    index = {}

    for card in cards:
        if card.get("layout") != "token":
            continue

        name = card.get("name")
        if not name:
            continue

        image_uris = card.get("image_uris") or {}
        small_image_uri = ""
        normal_image_uri = ""
        if isinstance(image_uris, dict):
            small_image_uri = image_uris.get("small") or ""
            normal_image_uri = image_uris.get("normal") or ""

        key = name.casefold()
        index[key] = {
            "name": name,
            "type_line": card.get("type_line") or "",
            "oracle_text": card.get("oracle_text") or "",
            "power": card.get("power"),
            "toughness": card.get("toughness"),
            "small_image_url": small_image_uri,
            "normal_image_url": normal_image_uri,
        }

    return index


def extract_tokens_from_all_parts(card):
    """Extract token parts from Scryfall's all_parts field."""
    results = []
    seen = set()

    for part in card.get("all_parts", []) or []:
        if part.get("component") != "token":
            continue

        token_name = part.get("name")
        if not token_name:
            continue

        token_name = token_name.strip()

        if token_name.casefold().endswith(" token"):
            token_name = token_name[:-6].strip()

        key = token_name.casefold()
        if key in seen:
            continue

        seen.add(key)
        results.append(token_name)

    return results


def build_pt(power, toughness):
    """Build a power/toughness string for a token card."""
    if power is None or toughness is None:
        return ""
    return f"{power}/{toughness}"


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"{INPUT_FILE} was not found. Run download_scryfall_bulk_data.py first."
        )

    cards = list(iter_cards(INPUT_FILE))
    token_index = build_token_index(cards)

    rows = []

    for card in cards:
        card_name = card.get("name")
        if not card_name:
            continue

        token_names = extract_tokens_from_all_parts(card)
        if not token_names:
            continue

        token_items = []
        for token_name in token_names:
            token_data = token_index.get(token_name.casefold(), {})
            token_items.append({
                "name": token_name,
                "type_line": token_data.get("type_line", ""),
                "oracle_text": token_data.get("oracle_text", ""),
                "pt": build_pt(
                    token_data.get("power"),
                    token_data.get("toughness"),
                ),
                "small_image_url": token_data.get("small_image_url", ""),
                "normal_image_url": token_data.get("normal_image_url", ""),
            })

        rows.append({
            "card_name": card_name,
            "tokens": token_items,
        })

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)

    print(f"Processed JSON.GZ file: {INPUT_FILE}")
    print(f"Found {len(rows)} cards with tokens.")
    print(f"Saved token data to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()