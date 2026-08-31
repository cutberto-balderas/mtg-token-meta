# MTG Token Meta

A data pipeline to identify and visualize Magic: The Gathering tokens that cards
across competitive decklists in different formats can create.

## Project goal

This project analyzes competitive Magic: The Gathering decklists to identify the
tokens that cards included in those decks can create.

Its goal is to produce a format-specific reference of relevant tokens, showing
how frequently token-producing cards appear across an analyzed competitive
decklist dataset.

## Initial scope

Version 0.1 focuses on a small, reproducible dataset:

- **Initial decklist source:** Magic Online (MTGO) Challenge events.
- **Card and token metadata:** Scryfall API.
- **Formats:** one format at a time.
- **Event window:** a manually selected date range.
- **Output:** a ranked CSV table of identifiable tokens.

MTGO Challenge decklists are the first dataset used to validate the pipeline.
Future versions may support competitive decklists from additional databases and
tournament sources.

Each analysis run should document its decklist source, format, event dates,
source URLs, and collection date.

## Methodology

1. Select a competitive decklist source, format, and date range.
2. Collect decklists from the selected dataset.
3. Extract card names and quantities from each decklist.
4. Retrieve card and token metadata.
5. Identify tokens that included cards can create.
6. Aggregate results by token, format, and decklist source.
7. Export the results for analysis and visualization.

## Interpretation of results

A token's frequency represents the number of analyzed competitive decklists that
contain at least one card capable of creating that token.

It does **not** represent:

- the number of times a token was created in actual matches;
- the number of physical tokens required by a player or store;
- a token's popularity outside the selected competitive decklist dataset;
- a complete representation of every possible token in Magic: The Gathering.

## Planned outputs

- A CSV file containing token name, characteristics, source cards, format,
  decklist source, and decklist frequency.
- A summary table of the most frequently represented tokens per format.
- A visual report or gallery using token metadata and image URLs.

## Project status

Planning and repository setup.

The first development milestone is to download and inspect one Magic Online
Challenge decklist without performing token detection yet.

## Data sources

- **Competitive decklists:** Magic Online Challenge events initially; additional
  databases and tournament sources may be supported in future versions.
- **Card and token metadata:** Scryfall API.

Data availability, event coverage, and card information may change over time.

## Attribution and disclaimer

This is an unofficial, non-commercial fan project. It is not approved or
endorsed by Wizards of the Coast.

Magic: The Gathering and related materials are property of Wizards of the Coast.
Card and token data are obtained from Scryfall.
