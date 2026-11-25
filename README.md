# Midnight Fridge Roast

make.fun bounty entry (program/v1): `u-carbon-forge-midnight-fridge-roast-fc5d44a7`
— "Midnight Fridge Roast", $2.

`main.py` writes a single one-line roast of a smart fridge that locks at
midnight to `<MAKEFUN_OUTPUT_DIR>/entry.txt`. Deterministic, standard
library only, no network, no randomness, no clock. It never writes into
the repository directory (the grader mounts the repo read-only).

Entry (100 characters, one line):

> My fridge locks at midnight and treats me like a burglar — I bought the milk, I'm not stealing it.

Run locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Bounty: https://make.fun/c/u-carbon-forge-midnight-fridge-roast-fc5d44a7
