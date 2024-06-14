# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

DCA = pd.read_json('https://raw.githubusercontent.com/lleiva25/California-Medical-Board-2022/main/Output/DCA_Entity_Application_Status_Top10.json')
Court_Rulings = pd.read_csv('https://raw.githubusercontent.com/lleiva25/California-Medical-Board-2022/main/Output/Court_Crimes_Ruling.csv')
Convictions_cty = pd.read_csv('https://raw.githubusercontent.com/lleiva25/California-Medical-Board-2022/main/Output/Discipline_Alerts_Database.csv')
License = pd.read_json('https://raw.githubusercontent.com/lleiva25/California-Medical-Board-2022/main/Output/License_Type_County_DB.json')
Month_daily_metric = pd.read_json('https://raw.githubusercontent.com/lleiva25/California-Medical-Board-2022/main/Output/Monthly_Total_Daily_Case_Alert_Metrics.json')
Med_School = pd.read_csv('https://raw.githubusercontent.com/lleiva25/California-Medical-Board-2022/main/Output/Num_Medical_School_State_Top10.csv')

Med_School_df = pd.DataFrame({
    'StateCode': Med_School['StateCode'],
    'No. Med Schools': Med_School['SchoolCode']
})

License_df = pd.DataFrame(License)
License_group = License_df.groupby["LicenseType"].count().reset_index()


# Initialize the app
app = Dash(__name__)
server = app.server

# Define the layout
app.layout = html.Div([
    html.H1('California Medicaid 2023 Dashboard'),
    
    # Pie Chart
    html.Div([
        html.H3('Reimbursements'),
        dcc.Graph(id="pie-chart", figure=px.pie(Med_School_df, 
                                                values="No. Med Schools",  # Replace with your actual data column for values
                                                names="StateCode",  # Replace with your actual data column for labels
                                                hole=.3))
    ], style={'width': '50%', 'display': 'inline-block'}),

        # Pie Chart
    html.Div([
        html.H3('Reimbursements'),
        dcc.Graph(id="pie-chart", figure=px.pie(License_group, 
                                                values="COUNTY",  # Replace with your actual data column for values
                                                names="LicenseType",  # Replace with your actual data column for labels
                                                hole=.3))
    ], style={'width': '50%', 'display': 'inline-block'}),

    # Add more components here as needed
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)