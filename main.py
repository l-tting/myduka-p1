from flask import Flask, render_template, request
from database import get_products, fetch_sales

#flask instance
app = Flask(__name__)


@app.route('/') #decorator func
def home(): #view func
    name = "Jane"
    return render_template('index.html',)



@app.route('/products')
def products():
    products_data = get_products()
    return render_template('products.html',products_data = products_data)


@app.route('/add_products',methods=['GET','POST'])
def add_products():
    if request.method == "POST":
        product_name = request.form['p_name']
        buying_price = request.form['b_price']
        selling_price = request.form['s_price'] 



@app.route('/sales')
def sales():
    sales_data = fetch_sales()
    return render_template('sales.html',sales_data = sales_data)



@app.route('/stock')
def stock():
    return render_template('stock.html')



@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')



@app.route('/register')
def register():
    return render_template('register.html')



@app.route('/login')
def login():
    return render_template('login.html')



# starts server to run app
app.run(debug=True)



