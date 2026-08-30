# Unit Converter

## User and problem

You, when you're cooking from a recipe written in measurements you don't normally use, or want a rough currency estimate before a trip, and don't want to search the web for a converter each time.

## Smallest useful version

Convert a number from one unit to another, for one category of unit you actually use often, such as cups to milliliters or US dollars to a currency you travel with.

## Acceptance criteria

- Given a number, a "from" unit, and a "to" unit within the supported category, returns the converted value
- Given an unsupported unit, shows a clear message naming the units it does support, instead of returning a wrong number
- Rounds the result to a sensible number of decimal places for that unit, rather than a long, unreadable decimal

## Non-goals

- Every possible unit or category, beyond the one you chose to support first
- Live, constantly updated currency exchange rates
- A graphical interface

