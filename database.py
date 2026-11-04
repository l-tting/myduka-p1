import psycopg2

# establishing a db connection
conn = psycopg2.connect(host='localhost',port=5432, user='postgres',password='6979',dbname='myduka_db')

# creating a cur object to perform db operations
cur = conn.cursor()


def get_products():
    cur.execute("select * from products")
    products_data = cur.fetchall()
    return products_data


print(10)


def insert_products():
    cur.execute("insert into products(name,buying_price,selling_price)values('asus laptop',40000,50000)") 
    conn.commit()


insert_products()
products_data = get_products()
print(products_data) 






