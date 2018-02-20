import database_manager
import os

@database_manager.connection_handler
def add_new_user(cursor, username, password):
    cursor.execute("""INSERT INTO users(user_name, password)
                          VALUES (%(user_name)s, %(password)s);""",
                   {'username': username,
                    'password': password})