def compound_interest(principle, interest_rate, number_of_years):
    """
    Compute the interest as a function of principle and interest rate.
    The function should return the amount of time it will take to pay
    interest based on the principle and interest rate.
    """
    # Write your code here
    return (principle * (interest_rate / 100) ** number_of_years)

# This is the main function that calls the above function.
compound_interest(principle=100,