year = 0

# Ensure investment is positive
while True:
    investment = float(input('Enter your initial investment amount: '))
    if investment > 0:
        break
    else:
        print("Please enter a positive amount.")

# Ensure interest rate is positive
while True:
    interest_input = float(input('Enter the interest rate (%): '))
    if interest_input > 0:
        interest_rate = 1 + (interest_input / 100)
        break
    else:
        print("Please enter a positive interest rate.")

target = float(input('Enter your target amount: '))

print(f'Year {year} - Investment: {investment:.2f}')

while investment < target:
    year += 1
    investment *= interest_rate
    print(f'Year {year} - Investment: {investment:.2f}')
