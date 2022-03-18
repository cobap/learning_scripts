import sqlite3 as sql
import os
import pandas as pd

os.chdir('C:\\Users\\Antonio Coelho\\Codigos\\learning_python')

connection = sql.connect('database.db')

with connection:
    connection.execute(
        """
        CREATE TABLE USER (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        );
        """
    )

dataminer = pd.read_excel('dados_dataminer.xlsx', index_col=0)
dataminer.to_sql('DATAMINER', connection)
