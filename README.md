<p align="center"><img src="intro-banner.png" alt="Billing-Program introduction" width="800"></p>

<p align="center"><img src="logo.png" alt="Billing-Program logo" width="200"></p>

# Billing-Program

**The Chalk Receipt**
_A long receipt unrolls in white chalk on a black board, and tax and tip tally into one circled total marked once in red._

A single-file interactive Python program that builds a simple receipt for
one item: it applies tax, adds a tip, and prints the overall cost.

![Billing Program banner](assets/banner.png)

![The Chalk Receipt, animated blackboard scene](scene.svg)

![Heading plate](plate.svg)

![Major separator](separator-major.svg)

## Contents

- [Requirements](#requirements)
- [Running it](#running-it)
- [How the total is calculated](#how-the-total-is-calculated)
- [Worked example (verified)](#worked-example-verified)
- [Input errors](#input-errors)
- [Files](#files)

## Requirements

- Python 3, standard library only.

![Heading plate](plate.svg)

![Major separator](separator-major.svg)

## Running it

```bash
python3 billing.py
```

The program prompts, in order:

1. `What is the cost of the item?`
2. `What is the tip percent?` (a percent, so `20` means 20 percent)

![Heading plate](plate.svg)

![Major separator](separator-major.svg)

## How the total is calculated

- Tax is 5.5 percent of the item cost: `tax_paid(cost)` returns
  `cost * 0.055`.
- The tip is the tip percent of the item cost: `total_percent_paid(cost,
  tip_percent)` returns `cost * tip_percent / 100`.
- The overall cost is `cost + tax + tip`.
- Tax, tip, and overall cost are printed to two decimal places, and the
  overall cost is prefixed with `$` by `overalltotalcost`.

![Heading plate](plate.svg)

![Major separator](separator-major.svg)

## Worked example (verified)

Input cost `100` and tip percent `20` prints:

```text
Tax Paid: 5.50
Tip amount: 20.00
Your overall cost is: $125.50
```

Input cost `19.99` and tip percent `15` prints tax `1.10`, tip `3.00`,
and an overall cost of `$24.09`.

![Heading plate](plate.svg)

![Major separator](separator-major.svg)

## Input errors

- Non-numeric input, the non-finite values `inf` and `nan`, or closed
  input (EOF), prints `Please enter a number.` and exits with status
  1, with no traceback.
- A negative cost or tip percent prints `Please enter a number that is
  not negative.` and exits with status 1.
- Zero is accepted for both prompts.

Tests: `python3 -m unittest` covers the money functions and scripted
runs, including the rejected `inf` and `nan` cases.

![Heading plate](plate.svg)

![Major separator](separator-major.svg)

> Observation note, clipped to the chart edge: Non-numeric input, inf, nan, or closed input prints `Please enter a number.` and ends with status 1, with no traceback.
> Observation note: A negative cost or tip prints `Please enter a number that is not negative.`, also status 1.
> Observation note: Zero is accepted at both prompts.

## Files

- `billing.py` - the program.
- `assets/banner.png`, `assets/logo.png` - project branding.
- `LICENSE` - GPL-3.0.
