import sqlite3 as sqlite

import pandas as pd

from sqlalchemy import create_engine

#create the table
with sqlite.connect('venv/population.db') as con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Population(id INTEGER PRIMARY KEY, country TEXT, population INT)")
    cur.execute("INSERT INTO Population VALUES(NULL,'Germany',81197537)")
    cur.execute("INSERT INTO Population VALUES(NULL,'France', 66415161)")
    cur.execute("INSERT INTO Population VALUES(NULL,'Spain', 46439864)")
    cur.execute("INSERT INTO Population VALUES(NULL,'Italy', 60795612)")
    cur.execute("INSERT INTO Population VALUES(NULL,'Spain', 46439864)")
connection = create_engine('sqlite:///population.db')

#read sql query
sql = 'SELECT * FROM Population'

with create_engine('sqlite:///population.db').connect() as con:
    df = pd.read_sql_query(sql, con)
#read sql table
# table name
table = 'Population'

with create_engine('sqlite:///population.db').connect() as con:
    df = pd.read_sql_table(table, con)


#read sql - can be done two ways. by referencing a table or a full sql query
#read sql - can be done two ways. by referencing a table or a full sql query
# create SQL query
sql = 'SELECT * FROM Population'

with create_engine('sqlite:///population.db').connect() as con:
    df = pd.read_sql(sql, con)
df

# table name
table = 'Population'

with create_engine('sqlite:///population.db').connect() as con:
    df = pd.read_sql(table, con)
print(df)