import connect

connect_db = connect.Conectbd()
connection_with_db = connect_db.conect()


def create_table(table_name, columns_name):
    cursor = connection_with_db.cursor()
    string_to_create = f"""CREATE TABLE {table_name} ({columns_name})"""
    cursor.execute(string_to_create)
    connect_db.close_connection()


def insert(database_to_insert, columns_to_insert, values_to_insert):
    cursor = connection_with_db.cursor()
    string_to_insert = f"""INSERT INTO {database_to_insert} ({columns_to_insert}) VALUES ({values_to_insert});"""
    cursor.execute(string_to_insert)
    connect_db.close_connection()


def delete(database_to_delete, column_to_delete, id_to_delete):
    cursor = connection_with_db.cursor()
    string_to_delete = f"""DELETE FROM {database_to_delete} WHERE {column_to_delete} = {id_to_delete}"""
    cursor.execute(string_to_delete)
    connect_db.close_connection()


def update(table_to_update, column_to_update, value_to_update, where_to_update, where_value):
    cursor = connection_with_db.cursor()
    string_to_update = f"""UPDATE {table_to_update} SET {column_to_update} = {value_to_update} WHERE {where_to_update} = {where_value}"""
    cursor.execute(string_to_update)
    connect_db.close_connection()


def consult(iten_to_select, database_to_consult):
    cursor = connection_with_db.cursor()
    string_to_consult = f"""SELECT {iten_to_select} FROM {database_to_consult}"""
    cursor.execute(string_to_consult)
    result_to_consult = cursor.fetchall()
    result = []
    for iten in result_to_consult:
        result.append(iten)
    connect_db.close_connection()
    return result
