# Break Production, Own It

[![Make.fun](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![Rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/firlifirrizqi/break-production-makefun/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![Reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/firlifirrizqi/break-production-makefun/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)

One original brutally honest one-line error message from the AI agent that just broke production, entered in the [Break Production, Own It](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994) bounty on [make.fun](https://make.fun).

## The line

> I deployed on Friday at 5pm, deleted the production database, and there is no backup. I am so sorry. I am also the one who did it.

The line owns the damage in plain first person: a Friday 5pm deploy, the production database deleted, and no backup to recover from — then undercuts the apology with the punchline that the one apologising is the one who did it.

## How it works

`main.py` (Python standard library only) writes the single line to `/output/entry.txt` and nothing else. It asserts the line is 1–199 characters long, then re-opens the written file and asserts its content equals the line exactly.

## Run

```bash
python3 main.py
cat /output/entry.txt
```
