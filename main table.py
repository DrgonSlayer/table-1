# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import sqlite3
from dash import Dash, dash_table
import pandas as pd
import sqlite3
conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()
c.execute("insert or replace into Filmlocation(stu, name, major) values(5, 'tomas', 'math')")
conn.commit()
c.execute('''create table FilmLocation(stu INT,name VARCHAR(20),major VARCHAR(20),primary key(stu))
             ''')
df = pd.read_sql("Select * From FilmLocation", conn)

app = Dash(__name__)

app.layout = dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])

if __name__ == '__main__':
    app.run_server(debug=True)
