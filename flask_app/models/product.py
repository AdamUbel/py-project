from flask_app.configs.mysqlconnection import connectToMySQL


class Products():

    schema = "esport_schema"

    def __init__(self, data):
        self.id = data['id']
        self.name = data["name"]
        self.category_id = data["category_id"]
        self.price = data["price"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


# NOTE CLASS METHODS


    @classmethod
    def insert_product(cls, data):
        query = """
      INSERT INTO products (name, category_id, price, created_at, updated_at)
      VALUES (%(name)s, %(category_id)s, %(price)s, NOW(), NOW());
      """
        return connectToMySQL(cls.schema).query_db(query, data)

    @classmethod
    def get_all_products(cls):
        query = "SELECT * FROM products;"

        results = connectToMySQL(cls.schema).query_db(query)

        products = []
        for row in results:
            products.append(cls(row))

        return products

    @classmethod
    def get_by_category(cls, data):
        query = "SELECT * FROM products WHERE category_id = %(id)s;"

        results = connectToMySQL(cls.schema).query_db(query, data)

        products = []
        for row in results:
            products.append(cls(row))

        return products

    @classmethod
    def add_to_cart(cls, data):
        query = "INSERT INTO users_carts (user_id, product_id) VALUES (%(user_id)s, %(product_id)s);"
        return connectToMySQL(cls.schema).query_db(query, data)

    @classmethod
    def remove_from_cart(cls, data):
        query = "DELETE FROM users_carts WHERE product_id = %(product_id)s LIMIT 1;"
        return connectToMySQL(cls.schema).query_db(query, data)
