from src.repository import AirportsRepository


def test_airports_repository():
    repo = AirportsRepository()
    gdf = repo.get_data()

    assert gdf is not None
