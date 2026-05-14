def calculate_amortization(principal, annual_rate, term_months):
    schedule = []
    r = annual_rate / 12 / 100
    balance = principal

    # check if the annual rate is 0, if so, return a simple division of principal by term_months
    if annual_rate == 0:
        m = principal / term_months
        for i in range(term_months):
            payment = m
            balance -= payment
            schedule.append({
                'month': i + 1,
                'payment': round(payment, 2),
                'interest': 0,
                'principal': round(payment, 2),
                'balance': round(balance, 2)
            })
    else:
        # Calculate the monthly payment using the amortization formula
        m = principal * (r * (1 + r) ** term_months) / \
            ((1 + r) ** term_months - 1)

        for i in range(term_months):
            interest = balance * r
            payment = m
            principal_payment = payment - interest
            balance -= principal_payment
            schedule.append({
                'month': i + 1,
                'payment': round(payment, 2),
                'interest': round(interest, 2),
                'principal': round(principal_payment, 2),
                'balance': round(balance, 2)
            })

    return ({
        'monthly_payment': round(m, 2),
        'total_paid': round(m * term_months, 2),
        'total_interest': round((m * term_months) - principal, 2),
        'schedule': schedule
    })


# Example usage (for testing purposes)
if __name__ == "__main__":
    result = calculate_amortization(25000, 7.0, 60)
    print(f"Original amount: $25,000")
    print(f"Monthly payment: ${result['monthly_payment']}")
    print(f"Total paid: ${result['total_paid']}")
    print(f"Total interest: ${result['total_interest']}")
    print(f"First month: {result['schedule'][0]}")
    print(f"Last month: {result['schedule'][-1]}")


# all just returning data in format for API response, different data points as well as schedule with data points inside of it as well
