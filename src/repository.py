from abc import ABC, abstractmethod
import geopandas as gpd


class Repository(ABC):

    @abstractmethod
    def get_data(self):
        pass


class GeoRepository(Repository):

    @abstractmethod
    def get_data(self) -> gpd.GeoDataFrame:
        pass


class AirportsRepository(GeoRepository):

    def get_data(self) -> gpd.GeoDataFrame:
        url = 'https://raw.githubusercontent.com/andrea-ballatore/'\
            'open-geo-data-education/'\
            'a9f68c60b0088e1b34cfc35b985513cfdcaba05e/'\
            'datasets/airports/airports_2020.geojson'
        self.airports = gpd.read_file(url, driver='GeoJSON')

        return self.airports
