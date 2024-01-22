import pandas as pd 
import plotly.express as px 

from dash import Dash, Input, Output, dcc, html

#-----Safely-Managed-Sanitation-Services-----
data_Ssan = (
            pd.read_csv("population_managing_safe_sanitation_services_cleaned.csv")
)

bar_filtered_dSsan = data_Ssan[(data_Ssan['Year'] == 2022) & (data_Ssan['Residence_Area_Type']=='Total')]

top_countries_dSsan = bar_filtered_dSsan.sort_values(by='Fact_Population(%)', ascending=False).head(10).sort_values(by='Fact_Population(%)')

bottom_countries_dSsan = bar_filtered_dSsan.sort_values(by='Fact_Population(%)').head(10).sort_values(by='Fact_Population(%)', ascending=False)

#-----Safely-Managed-Water-Drinking-Services-----
data_Swat = (
            pd.read_csv("population_managing_safe_drinking_water_cleaned.csv")
)

bar_filtered_dSwat = data_Swat[(data_Swat['Year'] == 2022) & (data_Swat['Residence_Area_Type']=='Total')]

top_countries_dSwat = bar_filtered_dSwat.sort_values(by='Fact_Population(%)', ascending=False).head(10).sort_values(by='Fact_Population(%)')

bottom_countries_dSwat = bar_filtered_dSwat.sort_values(by='Fact_Population(%)').head(10).sort_values(by='Fact_Population(%)', ascending=False)

#-----Handwashing-Facilities-at-home-----

data_hand = (
            pd.read_csv("population_basic_handwashing_facilities_cleaned.csv")
)

bar_filtered_hand = data_hand[(data_hand['Year'] == 2022) & (data_hand['Residence_Area_Type']=='Total')]

top_countries_hand = bar_filtered_hand.sort_values(by='Fact_Population(%)', ascending=False).head(10).sort_values(by='Fact_Population(%)')

bottom_countries_hand = bar_filtered_hand.sort_values(by='Fact_Population(%)').head(10).sort_values(by='Fact_Population(%)', ascending=False)


external_stylesheets=[
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]
app=Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "SDG Target 6.2 Analytics"

app.layout = html.Div(
    children=[
        #-----Header-------
        html.Div(
            children=[
                    html.H1(children="SDG Target 6.2 Analytics across Countries", className="header-title"),
                    html.P(
                        children=(
                                    html.P(
                                        children=(
                                            "Welcome to the Sustainable Development Goal (SDG) Target 6.2 Analytics Dashboard. This platform provides a comprehensive analysis of the global progress towards achieving Target 6.2 of SDG 6, focusing on Clean Water and Sanitation. Target 6.2 aims to achieve access to adequate and equitable sanitation and hygiene for all and end open defecation, paying special attention to the needs of women and girls and those in vulnerable situations."
                                        ),
                                    ),
                                    html.Br(),
                                    html.P(
                                        children=(
                                            "As we delve into the analytics, it becomes evident that understanding the current state of sanitation services and access to clean drinking water is paramount in our collective pursuit of sustainable development. The information presented here empowers users to explore population percentages with safely managed sanitation services and access to safely managed drinking water across countries over the years."
                                        )
                                    ),
                                    html.Br(),
                                    html.P(
                                        children=("The Dataset has been taken from: ", html.A("WHO SDG 6.1/6.2/6.A", href="https://www.who.int/data/gho/data/themes/topics/sdg-target-6-ensure-availability-and-sustainable-management-of-water-and-sanitation-for-all")),
                                    ),

                                    
                
                                   ),
                             className="header-description",
                          ),
                    ], 
                     className="header",
            ), 
        
        html.Br(),
        #-----Safely---Managed---Sanitation---Services---Description
        html.Div(
            children=[
                html.H3(children="Population using safely managed sanitation services (%)", className="dashboard-title"),
                html.Br(),
                html.P(
                    children=(
                        html.P(
                            children=(
                                "Explore the percentage of the population that is using safely managed sanitation services across different countries. This graph allows users to select a specific country and observe how the percentage of its population using sanitation services has evolved over time. Users can also compare the percentage of rural population and percentage of urban population of the same country to further understand the situation of that particular country."
                            ),
                        ),
                        html.Br(),
                        html.P(
                            children=(
                                "Still In 2022, 3.5 billion people lacked securely managed sanitation facilities and 2.0 billion people lacked basic hygiene services, despite significant improvements. It will be necessary to significantly accelerate existing worldwide rates of improvement in order to reach universal coverage by 2030. Understanding these trends is crucial for policymakers, researchers, and stakeholders working towards achieving SDG Target 6.2."
                            ),
                        ),
                        html.A("Source: UN Org SDG 6", href="https://www.un.org/sustainabledevelopment/water-and-sanitation/"),
                    ),
                    className="dashboard-description",
                ),
            ],
            className="content-card",
        ),

        #-----Safely---Managed---Sanitation---Services---Menu
        html.Div(
                children=[
                          html.Div(
                                 children=[
                                      html.Div(children="Sub Global Region", className="menu-title"),
                                      dcc.Dropdown(
                                          id="sub-global-region-filter-Ssan",
                                          options=[
                                              {"label": region, "value": region}
                                              for region in data_Ssan['Sub_Global_Regions'].unique()
                                          ],
                                          value= data_Ssan['Sub_Global_Regions'].unique()[0],
                                          clearable=False,
                                          className="dropdown",
                                      ),
                
                                        ],
                                 ),
                            html.Div(
                                    children=[
                                        html.Div(children="Country", className="menu-title"),
                                        dcc.Dropdown(
                                            id="country-filter-Ssan", 
                                            options=[],
                                            value=data_Ssan[data_Ssan['Sub_Global_Regions']==data_Ssan['Sub_Global_Regions'].unique()[0]]['Country'].unique()[0],
                                            clearable=False,
                                            className="dropdown",
                                        ),
                                    ],
                                 ),
                            html.Div(
                                    children=[
                                        html.Div(
                                            children="Residence Area Type", className="menu-title"
                                        ),
                                        dcc.Dropdown(
                                            id="residence-area-type-Ssan",
                                            options=[],
                                            className="dropdown",
                                        ),
                                    ]
                                ),

                        ],
                        className="menu",
                 ), 
                html.Br(),
        #-----Safely---Managed---Sanitation---Services---Graphs
        html.Div(
                    children=[
                        html.Div(
                            children=dcc.Graph(
                                id="population-percentage-graph-Ssan",
                                config={"displayModeBar": False},
                            ),
                            className="card",
                        ),
                        html.Br(),
                        html.Div(
                            children=dcc.Graph(
                                id='top-countries-bar-chart-Ssan',
                                config={"displayModeBar": False},
                                figure=px.bar(
                                    top_countries_dSsan,
                                    x='Fact_Population(%)',
                                    y='Country', 
                                    orientation='h',
                                    labels={'Fact_Population(%)': 'Total Population Percentage'},
                                    title='Top Ten Countries with Highest Population Percentage (2022)',
                                    template='plotly_dark',
                                    color_discrete_sequence=['#00FFD1'],
                                    custom_data=['Fact_Population(%)', 'Country'],
                                ).update_traces(
                                    hovertemplate='%{customdata[0]:.0f}%<br>%{customdata[1]}',
                                ),

                            ),
                            className="card",
                        ),
                        html.Br(),
                        html.Div(
                            children=dcc.Graph(
                                id='bottom-countries-bar-chart-Ssan',
                                config={"displayModeBar": False},
                                figure=px.bar(
                                    bottom_countries_dSsan,
                                    x='Fact_Population(%)',
                                    y='Country', 
                                    orientation='h',
                                    labels={'Fact_Population(%)': 'Total Population Percentage'},
                                    title='Top Ten Countries with Lowest Population Percentage (2022)',
                                    template='plotly_dark',
                                    color_discrete_sequence=['#FFFF00'],
                                    custom_data=['Fact_Population(%)', 'Country'],
                                ).update_traces(
                                    hovertemplate='%{customdata[0]:.0f}%<br>%{customdata[1]}',
                                ),

                            ),
                            className="card",
                            
                        )
                    ],
                    className="wrapper",
                ),
                 #-----Safely---Managed---Water---Drinking---Section
                 html.Br(),
        
        #-----Safely---Managed---Water---Drinking---Description
        html.Div(
            children=[
                html.H3(children="Population using safely managed water drinking services (%)", className="dashboard-title"),
                html.Br(),
                html.P(
                    children=(
                        html.P(
                            children=(
                                "Gain insights into the population percentages that are using safely managed drinking water services in various countries. Users can choose a country of interest to visualize the trends and variations in the percentage of population using clean drinking water services over the years. By analyzing population percentages, we can identify areas that require targeted interventions, measure progress, and align efforts for more effective global cooperation."
                                ),
                        ),
                        html.Br(),
                        html.P(
                            children=(
                                "2.2 billion people still lacked access to safely regulated drinking water services in spite of advancements. 2.4 billion people were living in water-stressed nations in 2020. Access to safe drinking water is foundational for health, well-being, and overall human development, making this analysis a vital component of our SDG exploration."
                               ),
                        ),
                        html.A("Source: UN Org SDG 6", href="https://www.un.org/sustainabledevelopment/water-and-sanitation/"),
                    ),
                    className="dashboard-description",
                ),
            ],
            className="content-card",
        ),

        #-----Safely---Managed---Water---Drinking---Menu
        html.Div(
                children=[
                          html.Div(
                                 children=[
                                      html.Div(children="Sub Global Region", className="menu-title"),
                                      dcc.Dropdown(
                                          id="sub-global-region-filter-Swat",
                                          options=[
                                              {"label": region, "value": region}
                                              for region in data_Swat['Sub_Global_Regions'].unique()
                                          ],
                                          value= data_Swat['Sub_Global_Regions'].unique()[0],
                                          clearable=False,
                                          className="dropdown",
                                      ),
                
                                        ]
                                 ),
                            html.Div(
                                    children=[
                                        html.Div(children="Country", className="menu-title"),
                                        dcc.Dropdown(
                                            id="country-filter-Swat", 
                                            options=[],
                                            value=data_Swat[data_Swat['Sub_Global_Regions']==data_Ssan['Sub_Global_Regions'].unique()[0]]['Country'].unique()[0],
                                            clearable=False,
                                            className="dropdown",
                                        ),
                                    ],
                                 ),
                            html.Div(
                                    children=[
                                        html.Div(
                                            children="Residence Area Type", className="menu-title"
                                        ),
                                        dcc.Dropdown(
                                            id="residence-area-type-Swat",
                                            options=[],
                                            className="dropdown",
                                        ),
                                    ]
                                ),

                        ],
                        className="menu",
                 ), 
                 
                 html.Br(),
        #-----Safely---Managed---Water---Drinking---Graphs
        html.Div(
                     children=[
                         html.Div(
                            children=dcc.Graph(
                                id="population-percentage-graph-Swat",
                                config={"displayModeBar": False},
                            ),
                            className="card",
                        ),
                        html.Br(),
                        html.Div(
                            children=dcc.Graph(
                                id='top-countries-bar-chart-Swat',
                                config={"displayModeBar": False},
                                figure=px.bar(
                                    top_countries_dSwat,
                                    x='Fact_Population(%)',
                                    y='Country', 
                                    orientation='h',
                                    labels={'Fact_Population(%)': 'Total Population Percentage'},
                                    title='Top Ten Countries with Highest Population Percentage (2022)',
                                    template='plotly_dark',
                                    color_discrete_sequence=['#00C4FF'],
                                    custom_data=['Fact_Population(%)', 'Country'],
                                ).update_traces(
                                    hovertemplate='%{customdata[0]:.0f}%<br>%{customdata[1]}',
                                ),

                            ),
                            className="card",
                        ),
                        html.Br(),
                        html.Div(
                            children=dcc.Graph(
                                id='bottom-countries-bar-chart-Swat',
                                config={"displayModeBar": False},
                                figure=px.bar(
                                    bottom_countries_dSwat,
                                    x='Fact_Population(%)',
                                    y='Country', 
                                    orientation='h',
                                    labels={'Fact_Population(%)': 'Total Population Percentage'},
                                    title='Top Ten Countries with Lowest Population Percentage (2022)',
                                    template='plotly_dark',
                                    color_discrete_sequence=['#FFC600'],
                                    custom_data=['Fact_Population(%)', 'Country'],
                                ).update_traces(
                                    hovertemplate='%{customdata[0]:.0f}%<br>%{customdata[1]}',
                                ),

                            ),
                            className="card",
                            
                        ),

                         
                     ],
                     className="wrapper",
                 ),
        
        html.Br(),
        #----Handwashing---Facilities---Description
        html.Div(
            children=[
                html.H3(children="Population with basic handwashing facilities at home (%)", className="dashboard-title"),
                html.Br(),
                html.P(
                    children=(
                        html.P(
                            children=(
                                "Explore the percentage of the population with access to basic handwashing facilities at home across various countries. This dashboard enables users to select a specific country and observe the evolution of the percentage of its population with access to basic hand washing facilities over time. It allows for comparisons with other sanitation indicators, providing a comprehensive understanding of hygiene practices in each country."
                                ),
                        ),
                        html.Br(),
                        html.P(
                            children=(
                                "Millions of people do not have access to even the most basic handwashing facilities at home as of 2022, which highlights the continued need for united efforts to upgrade the world's sanitary infrastructure. A key component of accomplishing SDG Target 6.2 is having access to basic handwashing facilities. Handwashing correctly is essential for stopping the transmission of illness, especially in light of current global health issues. The information provided here provides insight into the steps taken to guarantee that everyone has access to this vital resource."
                                ),
                        ),
                        html.A("Source: UN Org SDG 6", href="https://www.un.org/sustainabledevelopment/water-and-sanitation/"),
                    ),
                    className="dashboard-description",
                ),
            ],
            className="content-card",
        ),
        html.Br(),

        #----Handwashing---Facilities---Menu
        html.Div(
                children=[
                          html.Div(
                                 children=[
                                      html.Div(children="Sub Global Region", className="menu-title"),
                                      dcc.Dropdown(
                                          id="sub-global-region-filter-hand",
                                          options=[
                                              {"label": region, "value": region}
                                              for region in data_hand['Sub_Global_Regions'].unique()
                                          ],
                                          value= data_hand['Sub_Global_Regions'].unique()[0],
                                          clearable=False,
                                          className="dropdown",
                                      ),
                
                                        ],
                                 ),
                            html.Div(
                                    children=[
                                        html.Div(children="Country", className="menu-title"),
                                        dcc.Dropdown(
                                            id="country-filter-hand", 
                                            options=[],
                                            value=data_hand[data_hand['Sub_Global_Regions']==data_hand['Sub_Global_Regions'].unique()[0]]['Country'].unique()[0],
                                            clearable=False,
                                            className="dropdown",
                                        ),
                                    ],
                                 ),
                            html.Div(
                                    children=[
                                        html.Div(
                                            children="Residence Area Type", className="menu-title"
                                        ),
                                        dcc.Dropdown(
                                            id="residence-area-type-hand",
                                            options=[],
                                            className="dropdown",
                                        ),
                                    ]
                                ),

                        ],
                        className="menu",
                 ),
        html.Br(),

        #----Handwashing---Facilities---Graphs
        html.Div(
                    children=[
                        html.Div(
                            children=dcc.Graph(
                                id="population-percentage-graph-hand",
                                config={"displayModeBar": False},
                            ),
                            className="card",
                        ),
                        html.Br(),
                        html.Div(
                            children=dcc.Graph(
                                id='top-countries-bar-chart-hand',
                                config={"displayModeBar": False},
                                figure=px.bar(
                                    top_countries_hand,
                                    x='Fact_Population(%)',
                                    y='Country', 
                                    orientation='h',
                                    labels={'Fact_Population(%)': 'Total Population Percentage'},
                                    title='Top Ten Countries with Highest Population Percentage (2022)',
                                    template='plotly_dark',
                                    color_discrete_sequence=['#9900F0'],
                                    custom_data=['Fact_Population(%)', 'Country'],
                                ).update_traces(
                                    hovertemplate='%{customdata[0]:.0f}%<br>%{customdata[1]}',
                                ),

                            ),
                            className="card",
                        ),
                        html.Br(),
                        html.Div(
                            children=dcc.Graph(
                                id='bottom-countries-bar-chart-hand',
                                config={"displayModeBar": False},
                                figure=px.bar(
                                    bottom_countries_hand,
                                    x='Fact_Population(%)',
                                    y='Country', 
                                    orientation='h',
                                    labels={'Fact_Population(%)': 'Total Population Percentage'},
                                    title='Top Ten Countries with Lowest Population Percentage (2022)',
                                    template='plotly_dark',
                                    color_discrete_sequence=['#FF85B3'],
                                    custom_data=['Fact_Population(%)', 'Country'],
                                ).update_traces(
                                    hovertemplate='%{customdata[0]:.0f}%<br>%{customdata[1]}',
                                ),

                            ),
                            className="card",
                            
                        )
                    ],
                    className="wrapper",
                ),
        html.Br(),
        
        #-----Footer---
        html.Div(
            children=[
                html.Footer(
                    children=(
                    html.P("SDG 6.2 Analytical Dashboard, 2024"),
                    html.Br(),
                    html.P("© 2024 Aqsa Shoeb")
                    ),
                ),
            ],
            className="footer"
        ),

     ],
)

#-----Safely---Managed---Sanitation---Services---callbacks
@app.callback(
    Output('country-filter-Ssan', 'options'),
    [Input('sub-global-region-filter-Ssan', 'value')]
)

def update_country_options_Ssan(selected_sub_global_region_Ssan):
    countries = data_Ssan[data_Ssan['Sub_Global_Regions']== selected_sub_global_region_Ssan]['Country'].unique()
    return [{'label': country, 'value':country} for country in countries]

@app.callback(
        Output('residence-area-type-Ssan', 'options'),
        [Input('country-filter-Ssan', 'value')]
)
def update_residence_area_type_Ssan(selected_country_Ssan):
    residence_areas = data_Ssan[data_Ssan['Country']==selected_country_Ssan]['Residence_Area_Type'].unique()
    return [{'label': area, 'value': area} for area in residence_areas]

@app.callback(
    Output('population-percentage-graph-Ssan', 'figure'),
    [Input('country-filter-Ssan', 'value'),
     Input('residence-area-type-Ssan', 'value')]
)

def update_population_graph_Ssan(selected_country_Ssan, selected_residence_area_Ssan):
    filtered_df = data_Ssan[(data_Ssan['Country']==selected_country_Ssan) & (data_Ssan['Residence_Area_Type']==selected_residence_area_Ssan)]
    
    hover_format = '%{x}, %{y:.2f}%'

    fig =px.line(
        filtered_df, 
        x='Year', 
        y='Fact_Population(%)', 
        title=f'{selected_country_Ssan} Population Trends',
        labels={'Year': 'Year', 'Fact_Population(%)': 'Percentage of Population'},
        hover_data={'Year': True, 'Fact_Population(%)': ':.2f'},
        line_shape='linear',
        line_dash_sequence=['solid'],
        color_discrete_sequence=['#16FF00'],
        template='plotly_dark'
        )
    
    fig.update_traces(hovertemplate=hover_format)
    
    return fig 


#-----Safely---Managed---Water---Drinking---Callbacks 
@app.callback(
    Output('country-filter-Swat', 'options'),
    [Input('sub-global-region-filter-Swat', 'value')]
)

def update_country_options_Swat(selected_sub_global_region_Swat):
    countries = data_Swat[data_Swat['Sub_Global_Regions']== selected_sub_global_region_Swat]['Country'].unique()
    return [{'label': country, 'value':country} for country in countries]

@app.callback(
        Output('residence-area-type-Swat', 'options'),
        [Input('country-filter-Swat', 'value')]
)
def update_residence_area_type_Swat(selected_country_Swat):
    residence_areas = data_Swat[data_Swat['Country']==selected_country_Swat]['Residence_Area_Type'].unique()
    return [{'label': area, 'value': area} for area in residence_areas]

@app.callback(
    Output('population-percentage-graph-Swat', 'figure'),
    [Input('country-filter-Swat', 'value'),
     Input('residence-area-type-Swat', 'value')]
)

def update_population_graph_Swat(selected_country_Swat, selected_residence_area_Swat):
    filtered_df = data_Swat[(data_Swat['Country']==selected_country_Swat) & (data_Swat['Residence_Area_Type']==selected_residence_area_Swat)]
    
    hover_format = '%{x}, %{y:.2f}%'

    fig =px.line(
        filtered_df, 
        x='Year', 
        y='Fact_Population(%)', 
        title=f'{selected_country_Swat} Population Trends',
        labels={'Year': 'Year', 'Fact_Population(%)': 'Percentage of Population'},
        hover_data={'Year': True, 'Fact_Population(%)': ':.2f'},
        line_shape='linear',
        line_dash_sequence=['solid'],
        color_discrete_sequence=['#0014FF'],
        template='plotly_dark'
        )
    
    fig.update_traces(hovertemplate=hover_format)
    
    return fig 

#----Handwashing---Facilities---callbacks

@app.callback(
    Output('country-filter-hand', 'options'),
    [Input('sub-global-region-filter-hand', 'value')]
)

def update_country_options_hand(selected_sub_global_region_hand):
    countries = data_hand[data_hand['Sub_Global_Regions']== selected_sub_global_region_hand]['Country'].unique()
    return [{'label': country, 'value':country} for country in countries]

@app.callback(
        Output('residence-area-type-hand', 'options'),
        [Input('country-filter-hand', 'value')]
)
def update_residence_area_type_hand(selected_country_hand):
    residence_areas = data_hand[data_hand['Country']==selected_country_hand]['Residence_Area_Type'].unique()
    return [{'label': area, 'value': area} for area in residence_areas]

@app.callback(
    Output('population-percentage-graph-hand', 'figure'),
    [Input('country-filter-hand', 'value'),
     Input('residence-area-type-hand', 'value')]
)

def update_population_graph_Swat(selected_country_hand, selected_residence_area_hand):
    filtered_df = data_hand[(data_hand['Country']==selected_country_hand) & (data_hand['Residence_Area_Type']==selected_residence_area_hand)]
    
    hover_format = '%{x}, %{y:.2f}%'

    fig =px.line(
        filtered_df, 
        x='Year', 
        y='Fact_Population(%)', 
        title=f'{selected_country_hand} Population Trends',
        labels={'Year': 'Year', 'Fact_Population(%)': 'Percentage of Population'},
        hover_data={'Year': True, 'Fact_Population(%)': ':.2f'},
        line_shape='linear',
        line_dash_sequence=['solid'],
        color_discrete_sequence=['#E900FF'],
        template='plotly_dark'
        )
    
    fig.update_traces(hovertemplate=hover_format)
    
    return fig 

if __name__ == "__main__":
    app.run_server(debug=True)




