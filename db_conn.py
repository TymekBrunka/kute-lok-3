'''
Connetor to database Postgresql
'''
from configparser import ConfigParser
import psycopg2
from psycopg2 import connect
form psycopg2.extras import DictConnection

class dbConnection:
    def __init__(self, filename="database.ini", section='postgresql'):
        self.parser = ConfigParser()
        self.parser.read(filename)
        self.db = {}
        if self.parser.has_section(section):
            self.params = self.parser.items(section)
            for i in self.params:
                self.db[i[0]] = i[1]
            print(self.db)
        else:
            raise Exception (f"Sekcja {section} w pliku {filename} nie istnieje cwelu.")
    
    def connect(self):
        self.conn = None
        try:
            # self.conn = psycopg2
            pass
        except Exception:
            print("jej")