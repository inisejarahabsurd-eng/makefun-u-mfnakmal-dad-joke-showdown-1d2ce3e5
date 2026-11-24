#!/usr/bin/env python3
"""
Dad Joke Showdown Entry Generator

This program generates a top-tier dad joke for the competition.
The joke is selected from a curated collection of groan-worthy classics.
"""

import os
import random

# Curated collection of premium dad jokes
DAD_JOKES = [
    "I'm reading a book about anti-gravity. It's impossible to put down!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "I'm on a seafood diet. I see food and I eat it.",
    "I used to hate facial hair, but then it grew on me.",
    "I'm reading a book about teleportation. It's bound to get me somewhere.",
    "I used to be a banker, but I lost interest.",
    "I'm great at multitasking. I can waste time, be unproductive, and procrastinate all at once.",
    "I told my son I was reading a book about anti-gravity. He couldn't put it down either.",
    "What do you call a fake noodle? An impasta.",
    "I used to hate funerals, but now I'm working on them.",
    "I'm reading a book about frozen yogurt. It's cool, but I'm not that into it.",
    "I have a few jokes about unemployed people, but none of them work.",
    "I'm reading a book about a three-headed monster. It's impossible to put down!",
    "What do you call a bear with no teeth? A gummy bear.",
    "I used to play piano by ear. Now I use my hands.",
    "I'm reading a book about an alligator. It's snapping good!",
    "I told my doctor I broke my arm in two places. He told me to stop going to those places.",
    "I'm reading a book about a haunted house. It gave me goosebumps!",
    "What do you call a dog that does magic? A Labracadabrador.",
    "I used to think I was a bad golfer. Then I realized I was just having a bad game.",
    "I'm reading a book about mummies. It's wrapped up in mystery!",
    "I told my wife she was talking in her sleep. She denied everything.",
    "What do you call a fish without eyes? A fsh.",
    "I'm reading a book about a limping dog. It's a page-turner!",
    "I have a joke about construction, but I'm still working on it.",
    "I'm reading a book about a badger. It really grew on me!",
    "What do you call a dinosaur that crashes their car? Tyrannosaurus Wrecks.",
    "I told my son to stop playing Pokemon. He said 'Gotta catch some Z's!'",
    "I'm reading a book about a broken pencil. It's pointless, but I can't stop.",
    "I used to be a personal trainer, but I couldn't get anyone to follow me.",
]

OUTPUT_PATH = "/output/entry.txt"


def select_best_joke(jokes: list[str]) -> str:
    """Select the optimal dad joke using weighted quality scoring."""
    # Quality weights based on groan potential, pun strength, and classic structure
    # Higher weight = better joke for the competition
    joke_scores = {
        0: 10.0,   # Anti-gravity - absolute classic, perfect pun
        1: 9.5,    # Eyebrows - unexpected twist, relatable
        2: 9.0,    # Seafood diet - simple but effective
        3: 9.0,    # Facial hair - classic wordplay
        4: 8.5,    # Teleportation - book pun variant
        5: 8.5,    # Banker - short and punchy
        6: 8.0,    # Multitasking - relatable exaggeration
        7: 9.5,    # Son + anti-gravity - family twist on classic
        8: 9.0,    # Impasta - classic pun
        9: 7.5,    # Funerals - dark humor
        10: 8.0,   # Frozen yogurt - food pun
        11: 7.0,   # Unemployed - self-deprecating
        12: 9.0,   # Three-headed monster - book pun variant
        13: 8.5,   # Gummy bear - cute pun
        14: 8.0,   # Piano by ear - wordplay
        15: 8.5,   # Alligator - snap pun
        16: 8.0,   # Broken arm - unexpected twist
        17: 8.5,   # Haunted house - spooky pun
        18: 9.0,   # Labracadabrador - magical dog pun
        19: 7.5,   # Bad golfer - relatable
        20: 8.5,   # Mummies - wrap pun
        21: 8.0,   # Sleep talking - marital humor
        22: 8.5,   # Fsh - minimalist pun
        23: 8.0,   # Limping dog - book pun
        24: 7.0,   # Construction - self-aware
        25: 8.5,   # Badger - grow pun
        26: 9.0,   # T-Rex - crash pun
        27: 8.5,   # Pokemon - sleep pun
        28: 8.0,   # Broken pencil - pointless pun
        29: 7.5,   # Personal trainer - follow pun
    }
    
    # Weighted random selection from top-tier jokes
    top_tier_indices = [i for i, score in joke_scores.items() if score >= 8.5]
    weights = [joke_scores[i] for i in top_tier_indices]
    
    selected_index = random.choices(top_tier_indices, weights=weights, k=1)[0]
    return jokes[selected_index]


def validate_joke(joke: str) -> bool:
    """Validate the joke meets competition requirements."""
    if not joke:
        return False
    if len(joke) > 200:
        return False
    if joke.strip() == "":
        return False
    return True


def write_entry(joke: str) -> None:
    """Write the joke to the output file."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(joke)


def main() -> int:
    """Main entry point."""
    joke = select_best_joke(DAD_JOKES)
    
    if not validate_joke(joke):
        raise ValueError(f"Invalid joke generated: {joke!r}")
    
    write_entry(joke)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())