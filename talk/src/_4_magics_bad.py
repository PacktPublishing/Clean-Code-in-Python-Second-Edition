"""
magic method example: not called
rewrite of the same example function with the search logic
entwined with the calling code.
"""


def request_product_for_customer(customer, product, current_stock):
    product_available_in_stock = False
    for category in current_stock.categories:
        for prod in category.products:
            if prod.count > 0 and prod.id == product.id:
                product_available_in_stock = True
    if product_available_in_stock:
        requested_product = current_stock.request(product)
        customer.assign_product(requested_product)
    else:
        return "Product not available"
