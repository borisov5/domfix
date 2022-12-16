from domfix.domfix_products.models import Product


def get_product_by_name(product_slug, username):
    return Product.objects\
        .filter(slug=product_slug, user__username=username)\
        .get()
