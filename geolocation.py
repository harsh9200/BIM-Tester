
class GeoLocation:
    def value(self):
        '''
        Scenario: Geometry is georeferenced to a coordinate reference system

        The description of the CRS must be "{value}"
        
        Example: 
            The description of the CRS must be "Anything"
        
        Description: 
            Any arbitrary value if it adds meaning required by the project.
        '''
        pass

    def coordinate_reference_name(self):
        '''
        Scenario: Geometry is georeferenced to a coordinate reference system

        The geodetic datum must be "{coordinate_reference_name}"
        
        Example: 
            The geodetic datum must be "{coordinate_reference_name}"
        
        Description: 
            If this exists in the EPSG registry, the EPSG identifier must be provided. 
            If not, it may be arbitrarily specified as a custom text name.
        '''
        pass

    def unit(self):
        '''
        Scenario: Geometry is georeferenced to a coordinate reference system

        The map unit must be "{unit}"
        
        Example: 
            The map unit must be "Metre"
        
        Description: 
            This case insensitive text value may contain an optional prefix followed 
            by an SI unit or an converted unit
        
        '''
        pass

    def number(self):
        '''
        Scenario: Global coordinates of the project origin are provided for convenient
        reference

        The site "{guid}" has an elevation of "{number}"
        
        Example: 
            The site "28q3AgmxP5cepIweO5Of$o" has an elevation of "42.12"
        
        Description: 
            Any numerical value you expect for a particular attribute or property.
        '''
        pass
    
    def longlat(self):
        '''
        Scenario: Global coordinates of the project origin are provided for convenient
        reference

        The site "{guid}" has a longitude of "{longlat}"
        
        Example: 
            The site "28q3AgmxP5cepIweO5Of$o" has a longitude of "42.12"
        
        Description: 
            Either a longitude or latitude expressed in a decimal degrees.
        '''
        pass
