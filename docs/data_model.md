# Data Model

## Overview

The project follows a Medallion Architecture:

Source → Bronze → Silver → Gold

## Dimensions

### dim_character

| Column | Description |
|----------|-------------|
| character_id | Unique character identifier |
| character_name | Character name |
| gender | Gender |
| status | Alive/Deceased |
| crew_id | Crew identifier |
| devil_fruit_id | Devil fruit identifier |
| first_appearance_arc | First appearance |

### dim_crew

| Column | Description |
|----------|-------------|
| crew_id | Crew identifier |
| crew_name | Crew name |
| captain | Captain |
| crew_type | Pirate crew type |

### dim_devil_fruit

| Column | Description |
|----------|-------------|
| fruit_id | Fruit identifier |
| fruit_name | Fruit name |
| fruit_type | Paramecia, Logia, Zoan |
| description | Fruit description |

### dim_arc

| Column | Description |
|----------|-------------|
| arc_id | Arc identifier |
| arc_name | Arc name |
| saga | Saga |
| episode_start | Starting episode |
| episode_end | Ending episode |

## Fact Tables

### fact_bounty

| Column | Description |
|----------|-------------|
| bounty_id | Unique identifier |
| character_id | Character |
| bounty_amount | Bounty value |
| arc_id | Arc |
| snapshot_date | Snapshot date |

### fact_character_arc

| Column | Description |
|----------|-------------|
| character_id | Character |
| arc_id | Arc |
| is_main_character | Flag |
