# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 12:58:54 2023

@author: cy83r-3x71nc710n
"""

# One item, one receipt. I take a cost and a tip percent, apply the
# fixed 5.5 percent tax, and print tax, tip, and total. Nothing is
# saved and there is no loop, so one run handles exactly one item.
# The prompts now run inside main() so the money functions can be
# imported and tested without the program asking questions first.

import math
import sys

TAX_RATE = 0.055


def read_non_negative(prompt):
    # I read both answers through this one helper so the cost prompt
    # and the tip prompt fail in exactly the same way. It exits
    # instead of returning a sentinel because a bad value leaves
    # nothing sensible to print on a receipt.
    try:
        value = float(input(prompt))
    except (ValueError, EOFError):
        print("Please enter a number.")
        sys.exit(1)
    # float() accepts "inf" and "nan" as well as plain decimals. An
    # earlier note in this file left that hole open on purpose; a
    # receipt that prints $inf or $nan is a bug, not a quirk, so I
    # close it here with the same exit as any other bad number.
    if not math.isfinite(value):
        print("Please enter a number.")
        sys.exit(1)
    if value < 0:
        print("Please enter a number that is not negative.")
        sys.exit(1)
    return value


def tax_paid(cost: float) -> float:
    """Tax on cost at the fixed 5.5 percent rate in TAX_RATE."""
    return cost * TAX_RATE


def total_percent_paid(total_cost: float, tip_percent: float) -> float:
    """Tip amount: tip_percent percent of total_cost.

    The tip is a percent of the item cost, not of the tax. An earlier
    version passed the tax in here, so a 20 percent tip on a cost of
    100 printed 1.10 instead of 20.00. Both call sites below pass the
    cost, and they have to stay in agreement or the tip line and the
    total will disagree with each other.
    """
    return total_cost * tip_percent / 100


def overalltotalcost(overall_cost: float) -> str:
    """Format a total with a dollar sign and two decimal places."""
    return f"${overall_cost:.2f}"


def build_receipt(cost: float, tip_percent: float) -> str:
    """Build the receipt text for one item.

    Pulled out of the print path so a test can check the exact tax,
    tip, and total for known inputs without capturing prompts.
    """
    total_cost = cost + tax_paid(cost) + total_percent_paid(cost, tip_percent)
    receipt = str("\n Your receipt is: \n")
    receipt_tax = str("\n Tax Paid \n") + f"{tax_paid(cost):.2f}"
    receipt_percent = str("\n Tip amount \n") + f"{total_percent_paid(cost, tip_percent):.2f}"
    receipt_total_cost = str("\n Your overall cost is: \n") + str(overalltotalcost(total_cost))
    return receipt + receipt_tax + receipt_percent + receipt_total_cost


def main():
    cost = read_non_negative("\n What is the cost of the item? \n")
    # I ask for the tip as a plain percent number, so 20 means 20
    # percent. The dividing by 100 happens inside total_percent_paid.
    tip_percent = read_non_negative("\n What is the tip percent? \n")
    print(build_receipt(cost, tip_percent))
    return 0


if __name__ == "__main__":
    sys.exit(main())
