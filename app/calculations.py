def calculate_scenarios(initial_investment, expected_return, years_of_investment):
    """
    Calculate investment scenarios: base, optimistic, and pessimistic.
    
    Args:
        initial_investment (float): Starting investment amount.
        expected_return (float): Expected annualreturn as a percentage (e.g., 7 for 7%).
        years_of_investment (int): Number of years to invest.

    Returns:
        tuple: (base_result, optimistic_result, pessimistic_result)
    """
    swing = 0.05
    base_rate = expected_return / 100
    optimistic_rate = base_rate + swing
    pessimistic_rate = base_rate - swing

    base_result = round(initial_investment * ((1 + base_rate) ** years_of_investment), 2)
    optimistic_result = round(initial_investment * ((1 + optimistic_rate) ** years_of_investment), 2)
    pessimistic_result = round(initial_investment * ((1 + pessimistic_rate) ** years_of_investment), 2)

    return base_result, optimistic_result, pessimistic_result
