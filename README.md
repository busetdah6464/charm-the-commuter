# Charm the Commuter

[![make.fun](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/busetdah6464/charm-the-commuter/rank.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/busetdah6464/charm-the-commuter/reward.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

One line of weather for a city that does not exist — written to make a bored
commuter smile on the way to work.

## Entry

> In Glimmerwick: drizzle till nine, then sunshine so polite it holds the bus door. Commuters, leave the umbrella — bring a smile instead.

## How it works

`main.py` (stdlib only, deterministic) writes the single forecast line to
`/output/entry.txt` (136 characters, within the 140-character gate).

Run it twice and the output is byte-identical every time:

```sh
python3 main.py
cat /output/entry.txt
```
