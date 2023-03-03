import pandas as pd
import sqlite3 as sq

#create connection
con = sq.connect("Data.db")
cur = con.cursor()

#creating the table
cur.execute('''Create table if not exists Student(SNo primary key, Name, Symbol,Date,High,Low,Open,Close,Volume,Marketcap)''')
print('table created....')

#load csv file
data = pd.read_csv('coin_Bitcoin.csv')
df = pd.DataFrame(data)

#insert into database:
df.to_sql('Student', con, if_exists="replace", index=False)
print('data inserted successfully...')

cur.execute('select * from Student')

#displaying the data
records = cur.fetchall()

for row in records:
    print(row)

#updating the table:
