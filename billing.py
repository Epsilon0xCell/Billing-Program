# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 12:58:54 2023

@author: cy83r-3x71nc710n
"""

# Three functions

# This function inputs a cost and then outputs the dollar amount of tax to be paid (5.5 of the input)

cost = float(input("\n What is the cost of the item? \n"))
 

def tax_paid(cost:float) -> float:
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


# This function should input a total cost and a a tip percent then output the amount of tip to be paid.

tip_percent = float(input("\n What is the tip percent? \n"))

def total_percent_paid(total_cost:float, tip_percent:float) -> float:
 """
    This function should input a total cost and a a tip percent then output the amount of tip to be paid.
    
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
 return total_cost * tip_percent/100

total_cost = cost + tax_paid(cost) + total_percent_paid(tax_paid(cost), tip_percent)

# This function should take in a number representing cost and output
def overalltotalcost(overall_cost:float) -> str:
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
  return str("$") + str(overall_cost)

# Call the functions with respective values and print into a reciept
receipt = str("\n Your receipt is: \n")
receipt_tax =  str("\n Tax Paid \n") + str(tax_paid(cost))
receipt_percent = str("\n Tip percentage \n") + str(total_percent_paid(tax_paid(cost), tip_percent))
receipt_total_cost = str("\n Your overall cost is: \n") + str(overalltotalcost(total_cost))
print(receipt + receipt_tax + receipt_percent + receipt_total_cost)
