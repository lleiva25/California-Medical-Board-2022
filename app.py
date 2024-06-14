# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

DCA = pd.read_json('https://raw.githubusercontent.com/lleiva25/California-Medical-Board-2022/main/Output/DCA_Entity_Application_Status_Top10.json')
Court_Rulings = pd.read_csv('https://raw.githubusercontent.com/lleiva25/California-Medical-Board-2022/main/Output/Court_Crimes_Ruling.csv')
Convictions_cty = pd.read_json('/Users/leslieleiva/Documents/GitHub/California-Medical-Board-2022/Output/Disciplinary_Alerts_County.json')
License = pd.read_json('https://raw.githubusercontent.com/lleiva25/California-Medical-Board-2022/main/Output/License_Type_County_DB.json')
Month_daily_metric = pd.read_json('https://raw.githubusercontent.com/lleiva25/California-Medical-Board-2022/main/Output/Monthly_Total_Daily_Case_Alert_Metrics.json')
Med_School = pd.read_csv('https://raw.githubusercontent.com/lleiva25/California-Medical-Board-2022/main/Output/Num_Medical_School_State_Top10.csv')
DisciplinaryAct = pd.read_json('https://raw.githubusercontent.com/lleiva25/California-Medical-Board-2022/main/Output/DisciplinaryAction_Top10.json')

Med_School_df = pd.DataFrame({
    'StateCode': Med_School['StateCode'],
    'No. Med Schools': Med_School['SchoolCode']
})

License_df = pd.DataFrame({
    "License Type" : License["LicenseType"],
    "No. Licenses" : License["COUNTY"]
    })

DCA_df = pd.DataFrame({
    "DCA Entity": DCA["DCA Entity"],
    "Complete":DCA["Complete Applications"],
    "Incomplete":DCA["Incomplete Applications"]
})

Month_daily_metric_df = pd.DataFrame({
    "Month": Month_daily_metric["Month"],
    "Daily No. Alerts": Month_daily_metric["Daily No. Alerts"],
    "Daily No. Cases": Month_daily_metric["Daily No. Cases"],
    "Total No. Alerts": Month_daily_metric["Total No. Alerts"],
    "Total No. Cases": Month_daily_metric["Total No. Cases"]
})

DisciplinaryAct_df = pd.DataFrame({
    "Disciplinary Action" : DisciplinaryAct["Disciplinary Action"],
    "No. Cases" : DisciplinaryAct["No. Cases"]
})

Court_Rulings_df = pd.DataFrame(Court_Rulings)

Convictions_cty_df = pd.DataFrame(Convictions_cty)

#################################################################
# Initialize the app
app = Dash(__name__)
server = app.server

# Create the layout
app.layout = html.Div([
    html.H1('California Medical Board 2022'),
    
    # Bar Chart for Medical Schools in State
    html.Div([
        html.H3('No. of Medical Schools in State'),
        dcc.Graph(
            id="bar-chart",
            figure=px.bar(
                Med_School_df, 
                y="No. Med Schools",  # Replace with your actual data column for values
                x="StateCode",
                #title="No. of Medical Schools in State"
            )
        )
    ], style={'width': '50%', 'display': 'inline-block'}),

    # Pie Chart for Types of Medical Licenses
    html.Div([
        html.H3('Types of Medical Licenses'),
        dcc.Graph(
            id="pie-chart",
            figure=px.pie(
                License_df, 
                values="No. Licenses",  # Replace with your actual data column for values
                names="License Type",  # Replace with your actual data column for labels
                hole=.3,
                #title="Types of Medical Licenses"
            )
        )
    ], style={'width': '50%', 'display': 'inline-block'}),

    # Stacked Bar Chart for DCA Entity Application Status
    html.Div([
        html.H3('DCA Entity Application Status'),
        dcc.Graph(
            id="bar-chart1",
            figure=go.Figure(
                data=[
                    go.Bar(
                        name='Complete',
                        x=DCA_df['DCA Entity'],
                        y=DCA_df['Complete']
                    ),
                    go.Bar(
                        name='Incomplete',
                        x=DCA_df['DCA Entity'],
                        y=DCA_df['Incomplete']
                    )
                ],
                layout=go.Layout(
                    barmode='stack',
                    #title='DCA Entity Application Status',
                    xaxis=dict(title='DCA Entity'),
                    yaxis=dict(title='Count')
                )
            ),
            style={'width': '100vw', 'height': '100vh'}  # Adjust the width and height here
        )
    ]),

     # Line Chart for Total No. Disciplinary Cases & Alerts
    html.Div([
        html.H3('Total No. Disciplinary Cases & Alerts'),
        dcc.Graph(
            id="line-chart1",
            figure=go.Figure(
                data=[
                    go.Scatter(
                        name='No. Cases',
                        x=Month_daily_metric_df["Month"],
                        y=Month_daily_metric_df["Total No. Cases"],
                        mode='lines+markers'
                    ),
                    go.Scatter(
                        name='No. Alerts',
                        x=Month_daily_metric_df["Month"],
                        y=Month_daily_metric_df["Total No. Alerts"],
                        mode='lines+markers'
                    )
                ],
                layout=go.Layout(
                    title='Total No. Disciplinary Cases & Alerts',
                    xaxis=dict(title='Month'),
                    yaxis=dict(title='Count')
                )
            ),
    )], style={'width': '50%', 'display': 'inline-block'}),
    
    

    # Line Chart for Avg No. Disciplinary Cases & Alerts in a DayMonth
        html.Div([
            html.H3('Daily No. Disciplinary Cases & Alerts'),
            dcc.Graph(id="line-chart2",
            figure=go.Figure(
                data=[
                    go.Scatter(
                        name='No. Cases',
                        x=Month_daily_metric_df["Month"],
                        y=Month_daily_metric_df["Daily No. Cases"],
                        mode='lines+markers'
                    ),
                    go.Scatter(
                        name='No. Alerts',
                        x=Month_daily_metric_df["Month"],
                        y=Month_daily_metric_df["Daily No. Alerts"],
                        mode='lines+markers'
                    )
                ],
                layout=go.Layout(
                    #title='Total No. Disciplinary Cases & Alerts',
                    xaxis=dict(title='Month'),
                    yaxis=dict(title='Count')
                )
            ),
    )
    ],style={'width': '50%', 'display': 'inline-block'}),

    # Pie Chart for Types of Medical Licenses
    html.Div([
        html.H3('Disciplinary Actions'),
        dcc.Graph(
            id="pie-chart2",
            figure=px.pie(
                DisciplinaryAct_df, 
                values="No. Cases",  # Replace with your actual data column for values
                names="Disciplinary Action",  # Replace with your actual data column for labels
                hole=.3,
                color_discrete_sequence=px.colors.sequential.RdBu
                #title="Types of Medical Licenses"
            )
        )
    ],style={'width': '50%', 'display': 'inline-block'}),

    # Bar Chart for Types of Convictions
    html.Div([
        html.H3('Convictions'),
        dcc.Graph(
            id="bar-chart2",
            figure=px.bar(
                Court_Rulings_df,
                y="Crime",
                x="Ruling",
                color='Crime',
                #title="Types of Convictions",
                labels={"Ruling": "Number of Rulings", "Crime": "Type of Crime"},
                barmode="group",
               # bargap=0.15,
            ).update_layout(
                legend_title_text='Crime',
                xaxis_title='Type of Crime',
                yaxis_title='No. of Rulings',
                yaxis=dict(
                    showticklabels=False,  # Hide the y-axis tick labels
                    showgrid=False,  # Hide the y-axis grid lines
                    zeroline=False  # Hide the y-axis zero line
                )
                #width=800,  # Adjust width as needed
                #height=500  # Adjust height as needed
            )
        )
    ], style={'width': '50%', 'display': 'inline-block'}),

])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)