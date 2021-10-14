# please do not modify the following code
interest_rates = [float(x) for x in input().split(',')]
years = [int(x) for x in input().split(',')]
loan_principles = [int(x) for x in input().split(',')]

for interest_rate, year, loan_principle in zip(interest_rates, years, loan_principles):
    print(int(interest_rate * year * loan_principle))
