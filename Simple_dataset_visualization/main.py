'''
First 3 lines of code are to replicate the dataset taken from scikit library and converting it into .csv format
'''

#from sklearn.datasets import fetch_california_housing
#df = fetch_california_housing(as_frame=True).frame
#df.to_csv('housing.csv', index=False)

import pandas as pd
import plotly.express as px
from dash import Dash, html, dash_table, dcc, callback, Output, Input

df = pd.read_csv('housing.csv')

'''
This code defines the layout of a Dash application (app). It consists of four main components:

1) A Div element displaying the text "Dashboard".
2) A DataTable displaying the data from a Pandas DataFrame (df) with 15 rows per page.
3) A dropdown menu (Dropdown) allowing the user to select a feature from the DataFrame's columns. The selected value is stored in the feature-dropdown component.
4) A graph (Graph) with the ID "histogram", which will be updated dynamically.
'''

app = Dash()

app.layout = [
    html.Div(children='Dashboard'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=15),
    html.Div([
        html.Label('Select Feature:'),
        dcc.Dropdown(
            id = 'feature-dropdown',
            options = [{'label': col, 'value': col} for col in df.columns],
            value = df.columns[0]
        )
    ]),
    dcc.Graph(id='histogram')
]

'''
The code below defines a callback function "update_histogram" in a Dash application.
It updates the 'histogram' graph whenever the value of the 'feature-dropdown' changes.
The function generates a histogram using Plotly Express, with the selected feature as the x-axis, and returns the updated figure.
'''

@app.callback(
    Output('histogram', 'figure'),
    Input('feature-dropdown', 'value')
)
def update_histogram(selected_feature):
    fig = px.histogram(df, x=selected_feature)
    fig.update_layout(title = f'Histogram of {selected_feature}',
                        xaxis_title = selected_feature,
                        yaxis_title = 'Frequency')
    return fig


if __name__ == '__main__':
    app.run(debug=True)
