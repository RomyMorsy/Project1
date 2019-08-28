
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from app import app
from joblib import load

pipeline = load('pipeline.joblib')

column1 = dbc.Col(
    [
        dcc.Markdown('#Predictions'),

        dcc.Markdown('Clump Thickness'),
        dcc.Slider(
          id='clump_thickness',
            min=1,
            max=10,
            step=1,
            value=1,
            marks={n: str(n) for n in range(0,10,1)},
            className='mb-5',
        ),

        dcc.Markdown('Uniformity Of Cell Size'),
        dcc.Slider(
          id='uniformity_of_cell_size',
            min=1,
            max=10,
            step=1,
            value=3,
            marks={n: str(n) for n in range(0,10,1)},
            className='mb-5',
          ),

            dcc.Markdown('Uniformity Of Cell Shape'),
            dcc.Slider(
              id='uniformity_of_cell_shape',
                min=1,
                max=10,
                step=1,
                value=5,
                marks={n: str(n) for n in range(0,10,1)},
                className='mb-5',
            ),

            dcc.Markdown('Marginal Adhesion'),
            dcc.Slider(
              id='marginal_adhesion',
                min=1,
                max=10,
                step=1,
                value=5,
                marks={n: str(n) for n in range(0,10,1)},
                className='mb-5',
            ),

            dcc.Markdown('Single Epithelial Cell Size'),
            dcc.Slider(
              id='single_epithelial_cell_size',
                min=1,
                max=10,
                step=1,
                value=8,
                marks={n: str(n) for n in range(0,10,1)},
                className='mb-5',
            ),

            dcc.Markdown('Bare Nuclei'),
            dcc.Slider(
              id='bare_nuclei',
                min=1,
                max=10,
                step=1,
                value=5,
                marks={n: str(n) for n in range(0,10,1)},
                className='mb-5',
            ),

            dcc.Markdown('Bland Chromatin'),
            dcc.Slider(
              id='bland_chromatin',
                min=1,
                max=10,
                step=1,
                value=5,
                marks={n: str(n) for n in range(0,10,1)},
                className='mb-5',
            ),

            dcc.Markdown('Normal Nucleoli'),
            dcc.Slider(
              id='normal_nucleoli',
                min=1,
                max=10,
                step=1,
                value=5,
                marks={n: str(n) for n in range(0,10,1)},
                className='mb-5',
            ),

            dcc.Markdown('Mitosis'),
            dcc.Slider(
              id='mitosis',
                min=1,
                max=10,
                step=1,
                value=5,
                marks={n: str(n) for n in range(0,10,1)},
                className='mb-5',
            ),
],
md=4,
)

column2 = dbc.Col(
    [
        html.H2('Benign/Malign Tumor', className='mb-5'),
        html.Div(id='prediction-content', className='lead')
    ]
)

layout = dbc.Row([column1, column2])



@app.callback(
    Output('prediction-content', 'children'),
    [Input('clump_thickness', 'value'), Input('uniformity_of_cell_size', 'value'),
     Input('uniformity_of_cell_shape','value'),Input('marginal_adhesion','value'),
     Input('single_epithelial_cell_size','value'),Input('bare_nuclei','value'),
     Input('bland_chromatin','value'),Input('normal_nucleoli','value'),
     Input('mitosis','value')],
)
def predict(clump_thickness,uniformity_of_cell_size,uniformity_of_cell_shape,
            marginal_adhesion,single_epithelial_cell_size,bare_nuclei,
            bland_chromatin,normal_nucleoli,mitosis):
    df = pd.DataFrame(
        columns=['clump_thickness', 'uniformity_of_cell_size',
                 'uniformity_of_cell_shape','marginal_adhesion',
                 'single_epithelial_cell_size','bare_nuclei',
                 'bland_chromatin','normal_nucleoli','mitosis'],
        data=[[clump_thickness,uniformity_of_cell_size,uniformity_of_cell_shape,
        marginal_adhesion,single_epithelial_cell_size,bare_nuclei,
        bland_chromatin,normal_nucleoli,mitosis]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'{y_pred:.0f} class'


'''Variable Names:
clump_thickness
uniformity_of_cell_size
uniformity_of_cell_shape
marginal_adhesion
single_epithelial_cell_size
bare_nuclei
bland_chromatin
normal_nucleoli
mitosis'''
