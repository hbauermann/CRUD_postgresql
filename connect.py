import psycopg2
import json

config_json = open('config.json')
config_connection = json.load(config_json)
config_json.close()

class Conectbd():
    def __init__(self, host = config_connection['host'], database = config_connection['database'], user = config_connection['user'], password = config_connection['password']):
        self.host = host
        self.database = database
        self.user = user 
        self.password = password 


    def conect(self):
        try:
            connection = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            print('Connection Succesfull')
        except:
            print('Connection Error')
            connection = 'Connection Error'
        return connection


    def close_connection(self):
        connection = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        connection.close()
        print('Connection Closed')
        return 'Connection Closed'

