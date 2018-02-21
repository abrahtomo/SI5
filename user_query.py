import database_manager
import os
import bcrypt


def hash_password(plain_text_password):
    # By using bcrypt, the salt is saved into the hash itself
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def verify_password(plain_text_password, hashed_password):
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)


@database_manager.connection_handler
def register(cursor, register, hash):
    cursor.execute("""
        INSERT INTO users (username, password)
        VALUES (%(register)s, %(hash)s);
        """, {'hash': hash, 'register': register})


@database_manager.connection_handler
def check_user(cursor,login):
    cursor.execute("""
            SELECT username FROM users
            WHERE  username= %(login)s;
            """, {'login': login})
    data = cursor.fetchall()
    return data


@database_manager.connection_handler
def login(cursor,username):
    cursor.execute("""
        SELECT password FROM users
        WHERE  username= %(login)s;
        """,{'login':username})
    data=cursor.fetchall()
    return data


@database_manager.connection_handler
def get_id_by_user_name(cursor, username):
    cursor.execute("""
                    SELECT id FROM users
                    WHERE username = %(username)s; 
                   """,
                   {'username': username})
    received_id = cursor.fetchone()
    return received_id
