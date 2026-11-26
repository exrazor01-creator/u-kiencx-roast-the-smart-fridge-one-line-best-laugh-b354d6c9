#!/usr/bin/env python3
"""One-line entry: Roast the Smart Fridge.

The brief asks for one short roast, a single line of at
most 160 characters, of a smart home gadget the writer
shares a house with. A comedy editor judges pairs of
roasts, weighing, in order: the roast really is of a smart
home gadget the writer lives with, in one line; a real
laugh, with a turn or a sting at the end, not a mild
observation about technology; freshness, an angle or image
not met before, not a stock joke about fridges, robots or
the internet of things; one line that sets up fast and
lands inside the limit with no padding, no throat clearing
and no second sentence; and specificity to the gadget, a
real behaviour of the thing rather than smart homes in
general.

The sealed line below follows that order on purpose. The
roast aims at the smart fridge itself and its one
genuinely smart trick: it knows the exact moment the ice
cream is gone -- a specific, recognisable behaviour, not
a generic insult about appliances. The sting turns in
the last words: the same fridge that tracks dessert to
the minute never notices the science experiment growing
behind the pickles, so the machine is diligent about the
wrong thing and blind to the real mess. It sets up fast,
lands in one line, and dodges the worn-out "my fridge
orders groceries" and "my fridge watches me eat" cracks,
as well as the milk-expiry nag every fridge owner has
already heard.

LIMIT is 160 because the bounty gate allows UTF-8 text of
1 to 160 characters in /output/entry.txt. The validator
below guards the line against an edit that would push it
past the limit, split it into two sentences, or smuggle in
non-ASCII or control characters.
"""

import os

# The sealed line: a smart fridge that tracks the ice cream
# to the minute and stays blind to the experiment behind
# the pickles.
ENTRY = (
    "My smart fridge knows the exact moment the ice cream is gone, "
    "yet somehow never notices the science experiment growing "
    "behind the pickles."
)

LIMIT = 160  # bounty gate: 1-160 characters, UTF-8 text


def _validate(text):
    """Accept only one clean line inside the character limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.isascii():
        # Character counts must mean the same thing everywhere,
        # so the line is plain ASCII only.
        raise ValueError("entry must be plain ASCII text")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ch.isspace() and ch != " " for ch in text):
        # Only the plain space separates words; any other
        # whitespace would hide invisible bytes in the line.
        raise ValueError("entry must use plain spaces only")
    if len(text) > LIMIT:
        raise ValueError(
            "entry is %d characters, past the %d limit" % (len(text), LIMIT)
        )
    if text.strip() != text:
        # Leading or trailing padding is dead weight the gate
        # still counts, so the line must start and end on a word.
        raise ValueError("entry must not pad itself with spaces")
    if not text.isprintable():
        raise ValueError("entry must contain no control characters")
    if "  " in text:
        # A double space is a gap where a word should be; in a
        # 160-character line no gap is free.
        raise ValueError("entry must not contain a double space")
    if text.count(".") != 1 or not text.endswith("."):
        # One line, one sentence: exactly one full stop, and
        # it closes the line.
        raise ValueError("entry must be exactly one line")
    if "!" in text or "?" in text:
        # A second sentence-ender would smuggle a second
        # sentence past the single-stop check above.
        raise ValueError("entry must be exactly one line")
    return text


def main():
    entry = _validate(ENTRY)
    outdir = "/output" if os.path.isdir("/output") else "."
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(entry)
    print("%s (%d characters)" % (path, len(entry)))
    print(entry)


if __name__ == "__main__":
    main()
