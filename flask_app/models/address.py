from flask_app.configs.mysqlconnection import connectToMySQL


class Addresses():

    schema = "esport_schema"

    def __init__(self, data):
        self.id = data['id']
        self.street = data["street"]
        self.city = data["city"]
        self.state = data["state"]
        self.zip = data["zip"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def insert_address(cls, data):
        query = """
      INSERT INTO addresses (street, city, state, zip, created_at, updated_at)
      VALUES (%(street)s, %(city)s, %(state)s, %(zip)s, NOW(), NOW());
      """
        return connectToMySQL(cls.schema).query_db(query, data)
