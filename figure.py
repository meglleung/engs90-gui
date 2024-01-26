import io
import panel as pn
import pandas as pd
import plotly.graph_objects as go


pn.extension('plotly')

def graphing(df,ys):
    # df: csv data dataframe
    # y: list of attributes from csv we want to graph (dataframe headers)

    # Only handles up to 4...

    fig = go.Figure()

    i=1
    for column_name in ys:
        fig.add_trace(go.Scatter(
            x=df['Time'],
            y=df[column_name],
            name=column_name,
            yaxis=f"y{i}"
        ))
        i=i+1
    
    fig.update_layout(
        xaxis=dict(domain=[0.2, 0.8], title="Time")
    )

    signal_num = len(ys)

    fig.update_layout(
        yaxis1=dict(
            title=ys[0],
        ),   
    )

    if signal_num >= 2:
        fig.update_layout(
            yaxis2=dict(
                title=ys[1],
                overlaying="y",
                side="right",
            ),   
        )
    
    
    if signal_num >= 3:
        fig.update_layout(
            yaxis3=dict(
                title=ys[2],
                anchor="free", 
                overlaying="y", 
                autoshift=True,
            ),   
        )
    
    if signal_num >= 4:
        fig.update_layout(
            yaxis4=dict(
                title=ys[3],
                anchor="free", 
                overlaying="y", 
                autoshift=True,
                side="right",
            ),   
        )    

    # Update layout properties
    fig.update_layout(
        title_text="multiple y-axes example",
        width=800,
    )

    return fig

df = pd.read_csv('AccelerometerData.csv')
y = ['X Axis Acceleration','Y Axis Acceleration','Z Axis Acceleration','Combined Acceleration']

figure = graphing(df,y)


plotly_pane = pn.pane.Plotly(figure)

# Create a Panel app
app = pn.Column(
    "## Multiple Y-Axes Example",
    plotly_pane
)

# Serve the app
app.servable()


