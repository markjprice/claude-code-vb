# Unit Converter

A tiny command-line converter for the units you actually use often: **volume**
(cooking measures) and **currency**. No dependencies — just Python 3.

## Usage

```
python convert.py <value> <from> <to>
```

Examples:

```
$ python convert.py 1 cup ml
1 cup = 236.59 ml

$ python convert.py 20 usd eur
20 usd = 18.52 eur

$ python convert.py --list
volume (base ml): cup, fl_oz, gallon, l, ml, pint, quart, tbsp, tsp
currency (base usd): aud, cad, eur, gbp, jpy, mxn, usd
```

Unit names are case-insensitive and accept common aliases (`c`, `cups`,
`tablespoon`, `litre`, `euros`, `£`, ...). If a unit isn't recognised, the tool
tells you which units it supports instead of printing a wrong number. Use
`--category volume|currency` to force a category if a unit name is ambiguous.

## Currency rates are static

Exchange rates are hand-entered approximations in `convert.py` (`CURRENCY["units"]`),
not live data. Each value is how many US dollars one unit of that currency is
worth. Edit them there when you want fresher numbers.

## Tests

```
python -m pytest
```
