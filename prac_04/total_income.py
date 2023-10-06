"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

incomes = []  # move this outside of main so that it doesn't need to be called again by print report


def main():
    """Display income report for incomes over a given number of months."""
    number_of_months = int(input("How many months? "))
    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    print_report(number_of_months)


def print_report(number_of_months):
    """Print income per month with an accumulate total."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f}        Total: ${:10.2f}".format(month, income, total))


main()
