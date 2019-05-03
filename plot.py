import altair as alt
import geopandas as gpd
import pandas as pd

# read the data and extract the features that is directly usable by altair
dt = gpd.read_file('harvest.shp')
json_f = dt.to_json()
json_features = json.loads(json_f)
data_geo = alt.Data(values=json_features['features'])

#plot the graphic 
scen_list = ['1', '65', '129', '193', '257', '321', '385', '449']
selectScen = alt.selection_single(
    name='Select', 
    fields=['scenario'],  # this fails when I specify that I want 'properties.scenario'
    bind=alt.binding_select(options=scen_list) 
)
alt.Chart(data_geo).mark_geoshape(
    fill='lightgray',
    stroke='white',
).encode(
    color=alt.Color('properties.harvest:N', title='Period'),
    tooltip=['properties.AREAAC:Q', 'properties.StandAge:Q']
).properties(
    width=500,
    projection={'type':'mercator'}
).add_selection(
    selectScen
).transform_filter(selectScen)