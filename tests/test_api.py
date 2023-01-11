from fastapi.testclient import TestClient
from api.api import api
import geopandas as gpd
import json


client = TestClient(api)


def test_read_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'msg': 'Hi!'}


def test_get_airports():
    response = client.get('/data/airports')
    data = json.loads(response.json())
    gdf = gpd.GeoDataFrame.from_features(data['features'])

    assert response.status_code == 200
    assert len(gdf) == 3187
    assert gdf.loc[535, 'name'] == 'Copernicus Wrocław Airport'
