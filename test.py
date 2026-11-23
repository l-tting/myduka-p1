from database import get_sales_per_product, get_sales_per_day

product_sales = get_sales_per_product()

daily_sales = get_sales_per_day()


print(product_sales)

# [('milk', Decimal('1200.00')), ('bread', Decimal('4800.00')), ('macbook', Decimal('120000.00'))]


product_names = []

for i in product_sales:
    product_names.append(i[0])

print(product_names)


product_names = [i[0] for i in product_sales]
print(product_names)


sale_values = [ float(i[1]) for i in product_sales]
print(sale_values)


daily_sales = get_sales_per_day()

days = [str(i[0]) for i in daily_sales ]
print(days)

# [datetime.date(2026, 9, 14), datetime.date(2026, 9, 21), datetime.date(2026, 11, 5)] 


