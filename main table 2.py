


from dash import Dash, dash_table
import pandas as pd

dp = pd.read_csv(r'C:\Users\IT\Pictures\apps.csv')

app = Dash(__name__)

app.layout = dash_table.DataTable(dp.to_dict('records'), [{"name": i, "id": i} for i in dp.columns])

if __name__ == '__main__':
    app.run_server(debug=True)