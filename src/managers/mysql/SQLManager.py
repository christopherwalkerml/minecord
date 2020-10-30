import mysql.connector
import configparser
import os

class SQLManager:

    def __init__(self):
        self.buffer = []

        config = configparser.ConfigParser()
        config.read(f"{os.path.dirname(os.path.realpath(__file__))}\connection.properties")

        self.db = mysql.connector.connect(
            host=config["mysql"]["host"],
            user=config["mysql"]["user"],
            password=config["mysql"]["password"],
            database=config["mysql"]["database"],
        )

        self.cursor = self.db.cursor()

    def insert(self, table_name, columns, values):
        if len(columns) > 0:
            cols = f"({', '.join(columns)})"
        else:
            cols = ""

        print(f"INSERT INTO {table_name} {cols} VALUES {tuple(values)} ON DUPLICATE KEY UPDATE")

        self.cursor.execute(f"INSERT INTO {table_name} {cols} VALUES {tuple(values)} ON DUPLICATE KEY UPDATE")
        self.db.commit()

    def select(self, selector, table_name):
        self.cursor.execute(f"SELECT {selector} FROM {table_name}")
        result = self.cursor.fetchall()
        return result

    def select_where(self, selector, table_name, column, value):
        self.cursor.execute(f"SELECT {selector} FROM {table_name} WHERE {column} = {value}")
        result = self.cursor.fetchall()
        return result

    def get_channels(self):
        return [int(c[0]) for c in self.select("channel_id", "enabled_channels")]

    def get_users(self):
        return [int(u[0]) for u in self.select("user_id", "user_properties")]

    def get_user(self, uid):
        user = self.select_where("*", "user_properties", "user_id", str(uid))
        print(user)
