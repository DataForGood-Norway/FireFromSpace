from mapbox_dash import Mapbox_dash
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(__name__)

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

app.layout = html.Div([
    Mapbox_dash(
        id = 'id',
        mouse_position=None,
    viewport = {
            'width': 800,
            'height': 800,
            'latitude': 37.7577,
            'longitude': -122.4376,
            'zoom': 8
        },
MAPBOX_TOKEN = "pk.eyJ1IjoiYWxpc2hvYmVpcmkiLCJhIjoiY2ozYnM3YTUxMDAxeDMzcGNjbmZyMmplZiJ9.ZjmQ0C2MNs1AzEBC_Syadg"

    ),
    dcc.Input(id='mouse_position',value='value')
])

@app.callback(Output('mouse_position','value'),[Input('id','mouse_position')],[State('id','viewport')])
def x_prop(mouse_position,viewport):
    print(mouse_position)
    if mouse_position is not None:
        output = 'lat='+str(mouse_position['x_prop']+viewport['latitude']) \
                 + ', long=' + str(mouse_position['y_prop']+viewport['longitude'])
    else:
        output = None
    return output

if __name__ == '__main__':
    app.run_server(debug=True)
