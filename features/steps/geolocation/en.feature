Feature: Geolocation

In order to query data in real world coordinates
As a recipient expecting to integrate BIM and GIS datasets
Geolocation data must be stored correctly in received files

Scenario: Geometry is georeferenced to a coordinate reference system
*There must be at least one "{ifc_class}" element
*The project must have coordinate reference system data
*The name of the CRS must be "{coordinate_reference_name}"
*The description of the CRS must be "{value}"
*The geodetic datum must be "{coordinate_reference_name}"
*The vertical datum must be "{coordinate_reference_name}"
*The map projection must be "{coordinate_reference_name}"
*The map zone must be "{coordinate_reference_name}"
*The map unit must be "{unit}"

Scenario: Local coordinate systems are specified relative to a global system
*The project must have coordinate transformations to convert from local to global coordinates
*The eastings of the model must be offset by "{number}" to derive its global coordinates
*The northings of the model must be offset by "{number}" to derive its global coordinates
*The height of the model must be offset by "{number}" to derive its global coordinates
*The model must be rotated clockwise by "{number}" to derive its global coordinates
*The model must be scaled along the horizontal axis by "{number}" to derive its global coordinates

Scenario: A true north rotation of the project origin is provided for convenient reference
*The model must be rotated clockwise by "{number}" for true north to point up

Scenario: Global coordinates of the site origins are provided for convenient reference
*The site "{guid}" has a longitude of "{number}"
*The site "{guid}" has a latitude of "{number}"
*The site "{guid}" has an elevation of "{number}"

