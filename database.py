import psycopg2

# establishing a db connection
conn = psycopg2.connect(host='localhost',port=5432, user='postgres',password='6979',dbname='myduka_db')

# creating a cur object to perform db operations
cur = conn.cursor()


def get_products():
    cur.execute("select * from products")
    products_data = cur.fetchall()
    return products_data


def insert_products(prod_details):
    cur.execute("insert into products(name,buying_price,selling_price)values(%s,%s,%s)",prod_details) 
    conn.commit()



def fetch_sales():
    cur.execute("select * from sales")
    sales_data = cur.fetchall()
    return sales_data


def insert_sales(sale_details):
    cur.execute("insert into sales(pid,quantity)values(%s,%s)",sale_details)
    conn.commit()





def get_sales_per_product():
    cur.execute(
    """
        select products.name as p_name,sum(products.selling_price * sales.quantity) as total_sales
        from sales join products on products.id = sales.pid group by p_name;
    """)
    sales_per_product = cur.fetchall()
    return sales_per_product



def get_sales_per_day():
    cur.execute(
    """
        select date(sales.created_at) as day,sum(products.selling_price * sales.quantity) as total_sales
        from sales join products on products.id = sales.pid group by day;
    """)
    sales_per_day = cur.fetchall()
    return sales_per_day



def get_profit_per_product():
    cur.execute(
    """
        select products.name as p_name,sum((products.selling_price - products.buying_price) * sales.quantity)
          as t_profit from sales join products on products.id = sales.pid group by p_name;
    """)
    profit_per_product = cur.fetchall()
    return profit_per_product


def get_profit_per_day():
    cur.execute(
    """
        select date(sales.created_at) as day,sum((products.selling_price - products.buying_price) * sales.quantity)
          as t_profit from sales join products on products.id = sales.pid group by day;
    """)
    profit_per_day = cur.fetchall()
    return profit_per_day


