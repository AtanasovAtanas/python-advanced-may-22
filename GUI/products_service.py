from json import loads
from auth_service import get_current_user


def get_all_products():
    with open('./products.txt', 'r') as products_file:
        return [loads(line.strip()) for line in products_file]

def buy_product(product_id):
    user = get_current_user()
