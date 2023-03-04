#import sqlite and pandas
import sqlite3 as sq
import pandas as pd

#create Data.db file automatically    
connection = sq.connect('Data.db')
curs = connection.cursor()

# create table with same parameters as in .csv has 
curs.execute("create table if not exists coin" + "(SNo,Name,Symbol,Date,High,Low,Open,Close,Volume,Marketcap)")
 
# Load CSV data into Pandas DataFrame
student = pd.read_csv('coin_Bitcoin.csv')
table=pd.DataFrame(student)
print(table)


table.to_sql('coin', connection, if_exists='replace', index=False)
print('Data inserted successfully..!')

# Run select sql query
curs.execute('select * from coin')
records = curs.fetchall()
 
# Display result 
for row in records:
    # show row
    print(row)
print('\n',type(records),'\n')
print(records[15])


#updating

curs.execute('''UPDATE coin SET Open = '500'  WHERE Open ='144' ''')
print('updated successfully...!')

curs.execute('select * from coin')
 

records = curs.fetchall()

# Display result 
for row in records:
    # show row
    print(row)
    

#Delete
curs.execute('''DELETE FROM coin WHERE High = '115' ''')
print('Delete successfully...!')

curs.execute('select * from coin')

records = curs.fetchall()

# Display result 
for row in records:
    # show row
    print(row)
    


rec=pd.DataFrame(records)
print('\n', rec)
connection.close()