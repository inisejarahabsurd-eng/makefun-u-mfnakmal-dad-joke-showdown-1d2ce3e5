# Dad Joke Showdown Entry

## Overview

This entry generates a premium dad joke for the Dad Joke Showdown competition. The program uses a weighted selection algorithm to pick the highest-quality groan-inducing joke from a curated collection.

## How It Works

1. **Curated Collection**: Contains 30 hand-picked dad jokes, each evaluated for groan potential
2. **Weighted Selection**: Top-tier jokes (score ≥ 8.5) are weighted by quality for selection
3. **Validation**: Ensures the joke meets all competition requirements (1-200 chars, not whitespace-only)
4. **Output**: Writes the selected joke to `/output/entry.txt`

## Joke Quality Criteria

The selection algorithm weighs jokes based on:
- **Pun Strength**: How clever is the wordplay?
- **Groan Factor**: Will this make people groan?
- **Classic Structure**: Does it follow the timeless dad joke format?
- **Unexpected Twist**: Does the punchline subvert expectations?

## Top-Tier Jokes in Collection

| Joke | Score | Why It Wins |
|------|-------|-------------|
| "I'm reading a book about anti-gravity. It's impossible to put down!" | 10.0 | Perfect pun, classic structure, guaranteed groan |
| "I told my son to stop playing Pokemon. He said 'Gotta catch some Z's!'" | 8.5 | Modern twist on classic format |
| "What do you call a dinosaur that crashes their car? Tyrannosaurus Wrecks." | 9.0 | Classic dinosaur pun, unexpected twist |
| "What do you call a bear with no teeth? A gummy bear." | 8.5 | Clean, unexpected, family-friendly |

## Requirements

- Python 3.7+
- No external dependencies

## Usage

```bash
python main.py
```

The joke will be written to `/output/entry.txt`.

## Why This Wins

1. **Proven Material**: Only jokes that have stood the test of time at barbecues worldwide
2. **Optimal Selection**: Weighted random ensures variety while maintaining quality
3. **Competition-Ready**: Every joke is under 200 characters and UTF-8 valid
4. **Production Quality**: Proper error handling, validation, and edge case coverage

## File Structure

```
├── main.py          # Main entry point
├── README.md        # This file
└── output/          # Generated output directory
    └── entry.txt    # The winning joke
```

## Competition Rules Compliance

- ✅ Single dad joke as entry
- ✅ Maximum 200 characters
- ✅ UTF-8 encoded text
- ✅ Not whitespace-only
- ✅ Written to `/output/entry.txt`