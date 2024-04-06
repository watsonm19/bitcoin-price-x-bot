def calculate_percentage_gain_loss(current_price: float, start_price: float) -> float:
    """
    Calculate the percentage gain or loss.

    :param current_price: The current price of Bitcoin.
    :param start_of_year_price: The price of Bitcoin at the start of the current year.
    :return: The percentage gain or loss.
    """
    # Calculate the percentage change
    percentage_change = ((current_price - start_price) / start_price) * 100
    # Update to two decimal places
    percentage_change = round(percentage_change, 1)

    if percentage_change > 0:
        percentage_gain = "+" + str(percentage_change)
        return percentage_gain
    else:
        return str(percentage_change)