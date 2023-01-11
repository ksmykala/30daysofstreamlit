import streamlit as st
# import geopandas as gpd
from src.repository import AirportsRepository
import pydeck as pdk


def first_week():
    # st.write('Results of the first week')

    # gdf = from_data_file()
    # # st.write(gdf)
    # st.pydeck_chart(pdk.Deck(
    #     initial_view_state=pdk.ViewState(
    #         latitude=50.17,
    #         longitude=17.50,
    #         zoom=11,
    #         pitch=50
    #     ),
    #     layers=[
    #         pdk.Layer(
    #             'GeoJsonLayer',
    #             data=gdf,
    #             pickable=True,
    #             extruded=True
    #         )
    #     ]
    # ))
    # gdf_polygon = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
    gdf_polygon = from_data_file()
    # gdf_polygon = 'https://d2ad6b4ur7yvpq.cloudfront.net/'\
    #     'naturalearth-3.3.0/ne_10m_geography_regions_points.geojson'
    layers = [
        pdk.Layer(
            type="GeoJsonLayer",
            data=gdf_polygon,
            point_type='circle+text',
            filled=True,
            get_fill_color=[151, 196, 15, 200],
            radius_scale=10000,
            get_radius=10000,
            # get_text='name',
            # get_color=[0, 0, 0, 200],
            # get_size=15,
            # get_alignment_baseline="'bottom'",
            # get_position="geometry.coordinates",
            # width_scale=20,
            # width_min_pixels=5,
            # get_width=5,
            # radius_scale=2000,
            # get_fill_color=[180, 0, 200, 140],
            # pickable=True,
            ),
        ]
    view_state = pdk.ViewState(
            latitude=50,
            longitude=17,
            zoom=6,
            pitch=40.5)
    st.pydeck_chart(
        pdk.Deck(
            layers=layers,
            initial_view_state=view_state
        )
    )


def from_data_file():
    return AirportsRepository().get_data()


def app():
    first_week()


if __name__ == '__main__':
    app()
