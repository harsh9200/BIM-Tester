"""Feature: Geolocation

In order to query data in real world coordinates
As a recipient expecting to integrate BIM and GIS datasets
Geolocation data must be stored correctly in received files

Import:
    ArchiCAD: Partial, https://foobar1.com 
    BlenderBIM: Full, https://foobar2.com
    FreeCAD: Partial, https://foobar3.com
    Revit: Broken, https://foobar4.com
    Tekla: Unknown, https://foobar5.com

Export:
    ArchiCAD: Partial, https://foobar6.com
    BlenderBIM: Full, https://foobar7.com
    FreeCAD: Partial, https://foobar8.com
    Revit: Full, https://foobar9.com 
    Tekla: Unknown, https://foobar10.com
"""


from behave import step


"""Scenario: Geometry is georeferenced to a coordinate reference system"""

"""There must be at least one "ifc_site" element

Description
"""

@step(u'There must be at least one "{ifc_class}" element')
def step_impl(context, ifc_class):
    pass


"""The project must have coordinate reference system data

Description
"""


@step(u"The project must have coordinate reference system data")
def step_impl(context):
    pass


"""The name of the CRS must be "EPSG:7856"

Description
"""


@step(u'The name of the CRS must be "{coordinate_reference_name}"')
def step_impl(context, coordinate_reference_name):
    pass


"""The description of the CRS must be "Anything"

Description
"""


@step(u'The description of the CRS must be "{value}"')
def step_impl(context, value):
    pass


"""The geodetic datum must be "EPSG:7856"

Description
"""


@step(u'The geodetic datum must be "{coordinate_reference_name}"')
def step_impl(context, coordinate_reference_name):
    pass


"""The vertical datum must be "EPSG:7856"

Description
"""


@step(u'The vertical datum must be "{coordinate_reference_name}"')
def step_impl(context, coordinate_reference_name):
    pass


"""The map projection must be "EPSG:7856"

Description
"""


@step(u'The map projection must be "{coordinate_reference_name}"')
def step_impl(context, coordinate_reference_name):
    pass


"""The map zone must be "EPSG:7856"

Description
"""


@step(u'The map zone must be "{coordinate_reference_name}"')
def step_impl(context, coordinate_reference_name):
    pass


"""The map unit must be  "Metre"

Description
"""


@step(u'The map unit must be "{unit}"')
def step_impl(context, unit):
    pass


"""Scenario: Local coordinate systems are specified relative to a global system"""

"""The project must have coordinate transformations to convert from local to global coordinates

Description
"""


@step(u"The project must have coordinate transformations to convert from local to global coordinates")
def step_impl(context):
    pass


"""The eastings of the model must be offset by "42.12" to derive its global coordinates

Description
"""


@step(u'The eastings of the model must be offset by "{number}" to derive its global coordinates')
def step_impl(context, number):
    pass


"""The northings of the model must be offset by "42.12" to derive its global coordinates

Description
"""


@step(u'The northings of the model must be offset by "{number}" to derive its global coordinates')
def step_impl(context, number):
    pass


"""The height of the model must be offset by "42.12" to derive its global coordinates

Description
"""


@step(u'The height of the model must be offset by "{number}" to derive its global coordinates')
def step_impl(context, number):
    pass


"""The model must be rotated clockwise by "42.12" to derive its global coordinates

Description
"""


@step(u'The model must be rotated clockwise by "{number}" to derive its global coordinates')
def step_impl(context, number):
    pass


"""The model must be scaled along the horizontal axis by "42.12" to derive its global coordinates

Description
"""


@step(u'The model must be scaled along the horizontal axis by "{number}" to derive its global coordinates')
def step_impl(context, number):
    pass


"""Scenario: A true north rotation of the project origin is provided for convenient reference"""

"""The model must be rotated clockwise by "42.12" for true north to point up

Description
"""


@step(u'The model must be rotated clockwise by "{number}" for true north to point up')
def step_impl(context, number):
    pass


"""Scenario: Global coordinates of the site origins are provided for convenient reference"""

"""The site "28q3AgmxP5cepIweO5Of$o" has a longitude of "42.12"

Description
"""


@step(u'The site "{guid}" has a longitude of "{number}"')
def step_impl(context, guid, number):
    pass


"""The site "28q3AgmxP5cepIweO5Of$o" has a latitude of "42.12"

Description
"""


@step(u'The site "{guid}" has a latitude of "{number}"')
def step_impl(context, guid, number):
    pass


"""The site "28q3AgmxP5cepIweO5Of$o" has an elevation of "42.12"

Description
"""


@step(u'The site "{guid}" has an elevation of "{number}"')
def step_impl(context, guid, number):
    pass
