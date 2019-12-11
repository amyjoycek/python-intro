prices = (20, 6, 9, 14, 5)

tax_percent = (0.13)

def get_total(prices, tax_percent):
	total = prices * (tax_percent + 1)
	total_rounded = round(total, 2)
	return total_rounded

first_total = get_total(prices[0], tax_percent)
second_total = get_total(prices[1], tax_percent)

print("The first two totals are $" + str(first_total) + " and $" + str(second_total) + " respectively.")

# The first two totals are $22.6 and $6.78 respectively.