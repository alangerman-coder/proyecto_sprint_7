# my_func.py
product_price = 12.0 #variable global
product_qty = 5      #variable global

def total_price():
    product_price = 11.0 #variable local
    product_qty = 4      #variable local
    print(f'Precio total: {product_price * product_qty}')

total_price()