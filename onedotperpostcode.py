#%%
import altair as alt
from altair.expr import datum, substring
from vega_datasets import data
alt.renderers.enable('notebook')

zipcodes = "https://raw.githubusercontent.com/92Matt/hunpostcodes/master/hu_postal_codes.csv"

alt.Chart(zipcodes).mark_circle(size=5).encode(
    longitude='Longitude:Q',
    latitude='Latitude:Q',
    color='digit:N'
).project(
    type='albers',
    rotate=[325,0,0]
).properties(
    width=650,
    height=400
).transform_calculate(
    "digit", substring(datum.PostalCode, 0, 1)
)