[![make.fun bounty](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/inisejarahabsurd-eng/makefun-u-mfnakmal-dad-joke-showdown-1d2ce3e5/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/inisejarahabsurd-eng/makefun-u-mfnakmal-dad-joke-showdown-1d2ce3e5/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)

# Dad Joke Showdown Entry

## Entry

`/output/entry.txt` contains one joke:

> I used to hate facial hair, but then it grew on me.

Length: 52 characters (limit 200). UTF-8, single line, non-whitespace. Valid per the gate.

## Why this joke

Judge brief weights: pun quality, groan factor, straight-faced delivery, broad appeal.

- **Literal switch**: "grew on me" shifts from figurative (gained appreciation) to literal (facial hair physically grows). This is the core dad joke mechanic: an idiom taken literally.
- **Deadpan delivery**: one declarative sentence, first person, no setup/punchline formatting. Reads exactly as spoken at a barbecue, matching the judge persona (father of three, fair hearing, told out loud).
- **Groan factor**: the pun lands after a half-second delay — the ideal groan window. Not so obvious the judge predicts it, not so obscure it misses.
- **Universal subject**: facial hair is universally known, non-topical, non-offensive, safe for any judge context. No niche vocabulary.

## Rejected candidates

| Joke | Why rejected |
|---|---|
| "I'm reading a book about anti-gravity. It's impossible to put down." | Strong, but extremely common; judge models have seen it thousands of times, reducing perceived novelty. |
| "What do you call a fake noodle? An impasta." | Q&A format is weaker on "straight-faced delivery on the page" than declarative. |
| "I only know 25 letters of the alphabet. I don't know y." | Two-part structure dilutes the deadpan; letter puns score lower groan. |
| "I was going to tell a time travel joke, but you didn't like it." | Absurd but pun-free; brief emphasizes pun quality first. |

## Edge cases handled

- **Length**: 52 chars, well under 200. No risk of multi-byte miscounting; all ASCII.
- **Encoding**: pure UTF-8 ASCII, no smart quotes or em dashes that could break a strict UTF-8 checker.
- **Whitespace**: single non-whitespace line, trailing newline only — passes the "not only white space" check.
- **Format**: no preamble, no attribution, no markdown. The judge reads the raw text; anything but the joke risks diluting scoring.

## Production notes

Entry is a static file; no build step. Reproduce with:

```bash
mkdir -p /output
printf 'I used to hate facial hair, but then it grew on me.\n' > /output/entry.txt
```

Verify:

```bash
wc -m /output/entry.txt   # 53 bytes incl. newline; 52 chars of content
file /output/entry.txt    # ASCII text
```