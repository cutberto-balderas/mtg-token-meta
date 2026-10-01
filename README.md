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

Version 0.2 focuses on a small, reproducible dataset:

- **Initial decklist source:** Magic Online (MTGO) Challenge events and Leagues.
- **Card and token metadata:** Scryfall API.
- **Formats:** one format at a time.
- **Event window:** a manually selected event.
- **Output:** a JSON with the tokens in most played order.

MTGO Challenge decklists are the first dataset used to validate the pipeline.
Future versions may support competitive decklists from additional databases and
tournament sources.

Each analysis run should document its decklist source, format, event dates,
source URLs, and collection date.

## Methodology

1. Select a competitive decklist source, format, and date range from MTGO.
2. Collect decklists from the selected dataset.
3. Extract card names and quantities from each decklist.
4. Retrieve card and token metadata from Scryfall API.
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

- A JSON file containing token name, characteristics, source cards, format,
  decklist source, and decklist frequency.
- A JSON file containing cards that produce tokens with each token and data from Scryfall
- A summary table of the most frequently represented tokens per format.
- A visual report or gallery using token metadata and image URLs.

## Project Status

**Current Status:** In Active Development

We are currently building out the initial core scraping pipeline. The development milestones are structured as follows:

*   **Milestone 1 (Done):** Integrate the Scryfall API using the Oracle Bulk Data file to isolate token-producing cards and map out exactly which tokens they generate, producing a JSON with this reference information.
*   **Milestone 2 (Up Next):** Download, parse, and inspect raw Magic Online (MTGO) Challenge decklists to verify data structures before implementing token comparison with the generated data.

## Data sources

- **Competitive decklists:** Magic Online Challenge events initially; additional
  databases and tournament sources may be supported in future versions.
- **Card and token metadata:** Scryfall API.

Data availability, event coverage, and card information may change over time.

## Attribution and disclaimer

### Wizards of the Coast Policy Compliance
This token-scraping utility and data analysis project is an unofficial fan tool permitted under the Wizards of the Coast Fan Content Policy. It is not approved, endorsed, sponsored, or affiliated with Wizards of the Coast LLC or Magic: The Gathering Online.

Portions of the data and materials utilized within this application (including card names, mana symbols, token associations, and game mechanics) are the intellectual property of Wizards of the Coast. © Wizards of the Coast LLC, a subsidiary of Hasbro, Inc.

### Scryfall API Usage Compliance
Supplementary card metadata, image links, and token relation datasets are retrieved via the public Scryfall API. This software is completely independent, and its development is neither sponsored by nor affiliated with Scryfall. 

### Data Sourcing
Tournament decklists are aggregated from publicly accessible Magic Online tournament listings.
