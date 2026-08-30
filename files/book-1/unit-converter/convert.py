#!/usr/bin/env python3
"""Convert a number from one unit to another, for volume or currency.

Usage:
    python convert.py <value> <from> <to>
    python convert.py 1 cup ml
    python convert.py 20 usd eur
    python convert.py --list
"""

import argparse
import sys

# --- Data -------------------------------------------------------------------
#
# Each category maps canonical unit -> factor to the category's base unit
# (value_in_base = value * factor). Aliases map friendly spellings to a
# canonical unit. `decimals` is how far to round results for display.
#
# Volume uses US customary cooking measures; base unit is the millilitre.
# Currency rates are STATIC, hand-entered approximations - NOT live rates.
# Edit CURRENCY["units"] below to refresh them; base unit is USD.

VOLUME = {
    "base": "ml",
    "decimals": 2,
    "units": {
        "ml": 1.0,
        "l": 1000.0,
        "tsp": 4.92892159375,
        "tbsp": 14.78676478125,
        "fl_oz": 29.5735295625,
        "cup": 236.5882365,
        "pint": 473.176473,
        "quart": 946.352946,
        "gallon": 3785.411784,
    },
    "aliases": {
        "milliliter": "ml", "millilitre": "ml", "millilitres": "ml",
        "milliliters": "ml", "cc": "ml",
        "liter": "l", "litre": "l", "liters": "l", "litres": "l",
        "teaspoon": "tsp", "teaspoons": "tsp", "t": "tsp",
        "tablespoon": "tbsp", "tablespoons": "tbsp", "tbs": "tbsp", "tbl": "tbsp",
        "floz": "fl_oz", "fl-oz": "fl_oz", "oz": "fl_oz",
        "fluid_ounce": "fl_oz", "fluid_ounces": "fl_oz",
        "c": "cup", "cups": "cup",
        "pt": "pint", "pints": "pint",
        "qt": "quart", "quarts": "quart",
        "gal": "gallon", "gallons": "gallon",
    },
}

# Approximate rate = how many USD one unit of the currency is worth.
CURRENCY = {
    "base": "usd",
    "decimals": 2,
    "units": {
        "usd": 1.0,
        "eur": 1.08,
        "gbp": 1.27,
        "jpy": 0.0067,
        "cad": 0.73,
        "aud": 0.66,
        "mxn": 0.054,
    },
    "aliases": {
        "dollar": "usd", "dollars": "usd", "us": "usd", "$": "usd",
        "euro": "eur", "euros": "eur", "€": "eur",
        "pound": "gbp", "pounds": "gbp", "sterling": "gbp", "£": "gbp",
        "yen": "jpy", "¥": "jpy",
        "loonie": "cad",
        "peso": "mxn", "pesos": "mxn",
    },
}

CATEGORIES = {"volume": VOLUME, "currency": CURRENCY}


class ConversionError(Exception):
    """Raised when a unit is unknown or the two units are not comparable."""


# --- Core -----------------------------------------------------------------

def normalize_unit(unit, category):
    """Return the canonical unit name within `category`, or None if unknown."""
    key = unit.strip().lower().replace(" ", "_")
    key = category["aliases"].get(key, key)
    return key if key in category["units"] else None


def _find_category(unit):
    """Return list of (name, category) whose tables recognise `unit`."""
    hits = []
    for name, cat in CATEGORIES.items():
        if normalize_unit(unit, cat) is not None:
            hits.append((name, cat))
    return hits


def _supported(name):
    return ", ".join(sorted(CATEGORIES[name]["units"]))


def convert(value, from_unit, to_unit, category_name=None):
    """Convert `value` from `from_unit` to `to_unit`.

    Returns (result, category_name). Raises ConversionError with a message
    that names the supported units when something does not line up.
    """
    if category_name is not None:
        if category_name not in CATEGORIES:
            raise ConversionError(
                f"Unknown category '{category_name}'. "
                f"Supported: {', '.join(sorted(CATEGORIES))}."
            )
        candidates = [(category_name, CATEGORIES[category_name])]
    else:
        from_hits = {n for n, _ in _find_category(from_unit)}
        to_hits = {n for n, _ in _find_category(to_unit)}
        shared = from_hits & to_hits
        if not shared:
            if not from_hits:
                bad = from_unit
            elif not to_hits:
                bad = to_unit
            else:
                raise ConversionError(
                    f"'{from_unit}' and '{to_unit}' are not the same kind of unit, "
                    f"so they can't be converted."
                )
            names = ", ".join(f"{n} ({_supported(n)})" for n in CATEGORIES)
            raise ConversionError(
                f"Don't know the unit '{bad}'. Supported units by category: {names}."
            )
        candidates = [(n, CATEGORIES[n]) for n in shared]

    name, cat = candidates[0]
    src = normalize_unit(from_unit, cat)
    dst = normalize_unit(to_unit, cat)
    if src is None or dst is None:
        bad = from_unit if src is None else to_unit
        raise ConversionError(
            f"Don't know the {name} unit '{bad}'. Supported: {_supported(name)}."
        )

    result = value * cat["units"][src] / cat["units"][dst]
    return round(result, cat["decimals"]), name


# --- CLI ------------------------------------------------------------------

def _format_number(n):
    text = f"{n:.10f}".rstrip("0").rstrip(".")
    return text if text else "0"


def _list_text():
    lines = []
    for name, cat in CATEGORIES.items():
        lines.append(f"{name} (base {cat['base']}): {_supported(name)}")
    if CURRENCY in CATEGORIES.values():
        lines.append("note: currency rates are static approximations, not live.")
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="convert.py",
        description="Convert a number between units (volume or currency).",
    )
    parser.add_argument("value", nargs="?", type=float, help="the number to convert")
    parser.add_argument("from_unit", nargs="?", help="unit to convert from")
    parser.add_argument("to_unit", nargs="?", help="unit to convert to")
    parser.add_argument("--category", choices=sorted(CATEGORIES),
                        help="force a category if a unit is ambiguous")
    parser.add_argument("--list", action="store_true",
                        help="list supported categories and units")
    args = parser.parse_args(argv)

    if args.list:
        print(_list_text())
        return 0

    if args.value is None or args.from_unit is None or args.to_unit is None:
        parser.error("need VALUE FROM TO (or use --list)")

    try:
        result, _ = convert(args.value, args.from_unit, args.to_unit, args.category)
    except ConversionError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"{_format_number(args.value)} {args.from_unit} = "
          f"{_format_number(result)} {args.to_unit}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
