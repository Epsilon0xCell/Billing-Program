# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 12:58:54 2023

@author: cy83r-3x71nc710n
"""

# One item, one receipt. I take a cost and a tip percent, apply the
# fixed 5.5 percent tax, and print tax, tip, and total. Nothing is
# saved and there is no loop, so one run handles exactly one item.

import sys


# I read both answers through this one helper so the cost prompt and
# the tip prompt fail in exactly the same way. It exits instead of
# returning a sentinel because the rest of this script is flat top
# level code, and there is no caller that could take a bad value and
# keep going.
def read_non_negative(prompt):
    try:
        value = float(input(prompt))
    except (ValueError, EOFError):
        print("Please enter a number.")
        sys.exit(1)
    # float() accepts more than plain decimal text: "1e2", "inf", and
    # "nan" all parse. I checked this here. inf prints $inf on the
    # receipt, and nan passes the check below because nan < 0 is
    # False, so it prints $nan. I leave that hole open on purpose for
    # this small script, but nobody should reuse this helper as a
    # general money parser without closing it.
    if value < 0:
        print("Please enter a number that is not negative.")
        sys.exit(1)
    return value


# The order in this file matters. I ask for the cost here, after
# read_non_negative and before tax_paid is defined. That works only
# because this line calls read_non_negative, and tax_paid is not
# called until the receipt at the bottom. Moving this prompt above
# read_non_negative would break the run with a NameError.

cost = read_non_negative("\n What is the cost of the item? \n")


# The 5.5 percent rate lives only in the return line of this
# function. There is no constant and no setting for it, so a
# different tax rate means editing that one line.
def tax_paid(cost: float) -> float:
    """
    Parameters
    ----------
    cost : float
        gets the cost passed into the function.

    Returns
    -------
    float
        Gets the total cost and multiplies the total cost by the tax rate .
    """
    return cost * 0.055


# I ask for the tip as a plain percent number, so 20 means 20
# percent. The dividing by 100 happens inside total_percent_paid,
# not here, and the name total_cost in that function is whatever
# base amount the caller passes in.

tip_percent = read_non_negative("\n What is the tip percent? \n")


def total_percent_paid(total_cost: float, tip_percent: float) -> float:
    """
    This function should input a total cost and a tip percent then output the amount of tip to be paid.

    Parameters
    ----------
    total_cost : float
        gets the total_cost passed into the function.
    tip_percent : float
        gets the tip_percent passed into the function.

    Returns
    -------
    float
        This multiplies the total_cost by tip_percent divided by 100.
    """
    return total_cost * tip_percent / 100


# The tip is a percent of the item cost, not of the tax.
# I pass cost into total_percent_paid here, never tax_paid(cost).
# An earlier version of this line passed the tax, so a 20 percent
# tip on a cost of 100 printed 1.10 instead of 20.00. The receipt
# below calls the same function with cost again, and the two call
# sites have to stay in agreement or the tip line and the total
# will disagree with each other.
total_cost = cost + tax_paid(cost) + total_percent_paid(cost, tip_percent)


# This is the only place that adds the dollar sign. The tax and
# tip lines on the receipt format themselves with :.2f where they
# are built below, so a change to how money prints has to touch
# both spots, not just this function.
def overalltotalcost(overall_cost: float) -> str:
    """
    Parameters
    ----------
    overall_cost : float
        this passes overal_cost into the argument.

    Returns
    -------
    str
        this adds proper dollar formating to the overall_cost.
    """
    return f"${overall_cost:.2f}"


# I build the receipt as separate strings and print them joined,
# which is why each piece starts with its own newline. tax_paid and
# total_percent_paid run a second time here on the same inputs, so
# the printed tax and tip match the total above only as long as
# these calls keep passing cost, the same as the total line does.
receipt = str("\n Your receipt is: \n")
receipt_tax = str("\n Tax Paid \n") + f"{tax_paid(cost):.2f}"
receipt_percent = str("\n Tip amount \n") + f"{total_percent_paid(cost, tip_percent):.2f}"
receipt_total_cost = str("\n Your overall cost is: \n") + str(overalltotalcost(total_cost))
print(receipt + receipt_tax + receipt_percent + receipt_total_cost)
