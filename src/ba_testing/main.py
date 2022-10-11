from functools import lru_cache

from arcgis.gis import GIS


class BusinessAnalyst(object):
    """
    Business Analyst object to provide access to introspection capabilities.
    """

    def __init__(self, gis: GIS, **kwargs):

        self.gis = gis

        # add any additional keyword arguments as properties
        for key, val in kwargs:
            setattr(self, key, val)

    @property
    @lru_cache(16)
    def geoenrichment_url(self):
        """The url string for the Geoenrichment services."""
        return self.gis.properties.helperServices.geoenrichment.url

    @property
    def countries_url(self):
        """Geoenrichment Countries url."""
        return self.geoenrichment_url + '/Geoenrichment/Countries'

    @property
    def data_collections_url(self):
        """Data collections url."""
        return self.geoenrichment_url + '/Geoenrichment/DataCollections'

    @lru_cache(16)
    def get_countries(self):
        """List of ``Country`` objects with properties."""
        # get the list of countries from
        cntry_res = self.gis._con.get(self.geoenrichment_url + '/Geoenrichment/Countries')

        # get this list of countries out of the JSON
        cntry_lst = [Country(cntry_dict, self) for cntry_dict in cntry_res['countries']]

        return cntry_lst


class Country(object):
    """
    Business Analyst Country.
    """

    def __init__(self, cntry_dict: dict, business_analyst: BusinessAnalyst) -> None:
        self.dict = cntry_dict
        self.ba = business_analyst
        self.name = self.dict['name']
        self.iso3 = self.dict['abbr3']
        self.hierarchies = [CountryHierarchy(h) for h in self.dict['hierarchies']]

    @lru_cache(16)
    def get_data_collection_json(self) -> dict:
        """JSON response from data collection REST endpoint."""
        dc_res = self.ba.gis._con.get(self.ba.data_collections_url + f'/{self.iso3}')
        return dc_res

    @lru_cache(16)
    def get_enrich_variables(self) -> list:
        """Enrich variables available for country."""

        # get a list of enrich variables
        dc_res = self.get_data_collection_json()

    @property
    def enrich_variables(self) -> list:
        """Property alias for ``get_enrich_variables``."""
        return self.get_enrich_variables()


class CountryHierarchy(object):
    """
    Business Analyst Country data hierarchy for data organization.
    """

    def __init__(self, hrchy_dict: dict, business_analyst: BusinessAnalyst) -> None:
        self.dict = hrchy_dict
        self.ba = business_analyst
        self.id = self.dict['ID']
