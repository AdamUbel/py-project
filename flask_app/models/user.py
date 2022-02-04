from flask_app.configs.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models import product, address
from flask_bcrypt import Bcrypt
import re

bcrypt = Bcrypt(app)

# NOTE  PASSWORD AND EMAIL REGULAR EXPRESSIONS
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$!&*?])[\w\d@#$]{8,16}$')


class Users():

    schema = "esport_schema"

    def __init__(self, data):
        self.id = data['id']
        self.full_name = data["full_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.cart = []
        self.cart_total = 0
        self.address = []


# NOTE CLASS METHODS


    @classmethod
    def insert_user(cls, data):
        query = """
      INSERT INTO users (full_name, email, password, created_at, updated_at)
      VALUES (%(full_name)s, %(email)s, %(password)s, NOW(), NOW());
      """
        return connectToMySQL(cls.schema).query_db(query, data)

    @classmethod
    def user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        user_with_email = connectToMySQL(cls.schema).query_db(query, data)

        if len(user_with_email) < 1:
            return False
        return cls(user_with_email[0])

    @classmethod
    def user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        user_by_id = connectToMySQL(cls.schema).query_db(query, data)
        if user_by_id:
            return cls(user_by_id[0])

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users"

        results = connectToMySQL(cls.schema).query_db(query)

        users = []
        for row in results:
            users.append(cls(row))

        return users

    @classmethod
    def users_cart(cls, user_id):
        query = "SELECT * FROM users LEFT JOIN users_carts ON users.id = users_carts.user_id LEFT JOIN products ON users_carts.product_id = products.id WHERE users.id = %(id)s;"

        results = connectToMySQL(cls.schema).query_db(query, user_id)

        users_cart = cls(results[0])

        for row in results:
            cart_data = {
                "id": row['products.id'],
                "category_id": row['category_id'],
                "name": row['name'],
                "price": row['price'],
                "created_at": row['products.created_at'],
                "updated_at": row['products.updated_at']
            }
            users_cart.cart.append(product.Products(cart_data))
            if row["price"] != None:
                users_cart.cart_total += row['price']

        return users_cart

    @classmethod
    def users_with_address(cls, user_id):
        query = "SELECT * FROM users LEFT JOIN addresses ON users.address_id = addresses.id WHERE users.id = %(id)s;"

        results = connectToMySQL(cls.schema).query_db(query, user_id)

        users_with_add = cls(results[0])

        for row in results:
            address_data = {
                "id": row["addresses.id"],
                "street": row['street'],
                "city": row['city'],
                "state": row['state'],
                "zip": row['zip'],
                "created_at": row['addresses.created_at'],
                "updated_at": row['addresses.updated_at']
            }

            users_with_add.address.append(address.Addresses(address_data))

        return users_with_add


# NOTE STATIC METHODS/VALIDATORS

    @staticmethod
    def validate_register(post_data):
        is_valid = True
        print(post_data)

        if len(post_data["first_name"]) < 3:
            flash("First Name Must Be Longer Then Two Characters", "register")
            is_valid = False

        if len(post_data["last_name"]) < 3:
            flash("Last Name Must Be Longer Then Two Characters", "register")
            is_valid = False

        if not EMAIL_REGEX.match(post_data['email']):
            flash('Please Enter Valid Email', "register")
            is_valid = False

        if not PASSWORD_REGEX.match(post_data['password']):
            flash("Please Enter Valid Password", "register")
            is_valid = False

        if Users.user_by_email({"email": post_data["email"].lower()}):
            flash("Email Already In Use, Please Sign In", "register")
            is_valid = False

        if post_data['password'] != post_data['confirm_password']:
            flash("Passwords Dont Match", "register")
            is_valid = False

        return is_valid

    @staticmethod
    def validate_login(user, input_pw):
        is_valid = True

        print(user, input_pw)
        if not user:
            flash("Invalid Email or Password", "login")
            is_valid = False
            return is_valid

        if not bcrypt.check_password_hash(user.password, input_pw["input_pw"]):
            flash("Invalid Password", "login")
            is_valid = False

        return is_valid
