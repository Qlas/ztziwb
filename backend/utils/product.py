def get_all_products(category):
    products = []
    products.extend(category.products.all())
    for sub_category in category.sub_category.all():
        products.extend(get_all_products(sub_category))
    return products
