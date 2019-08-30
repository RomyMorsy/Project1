import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from PIL import Image
from app import app
import seaborn as sns
import pandas as pd

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has
twelve columns.

There are three main layout components in dash-bootstrap-components: Container,
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column
should take up a third of the width. Since we don't specify behaviour on
smaller size screens Bootstrap will allow the rows to wrap so as not to squash
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
           This app is useful for researchers or for doctors to estimate whether
           or not their patient has a malignant or benign tumor based on different
           parameters. They are normalized on a 1-10 scale and are all to do
           with the size, shape, and qualities of the skin and cells surrounding
           the tumor.


            """
        ),
        dcc.Link(dbc.Button('Make A Prediction!', color='primary'), href='/predictions')
    ],
    md=4,
)
df = pd.read_csv('breast_cancer_dataset.csv')
fig = px.scatter(df,x='clump_thickness',y='single_epithelial_cell_size',color='class');

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])




'''bcancer-pred'''
