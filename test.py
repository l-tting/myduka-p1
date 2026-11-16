from database import get_products


products = get_products()
# print(products)

# x = (1, 'milk', Decimal('50.00'), Decimal('60.00')),



for i in products:
    print(i[0])
