"""
magic methods: __contains__

Reimplementation of the request function, but this time calling the magic method
implemented in the class, to make the code more readable.
"""

def request_product_for_customer(customer, product, current_stock):
    if product in current_stock:
        requested_product = current_stock.request(product)
        customer.assign_product(requested_product)
    else:
        return "Product not available"
