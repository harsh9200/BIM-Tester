"""Feature: Project setup

In order to ensure quality of the digital built environment
As a responsible digital citizen
We expect compliant OpenBIM deliverables

Import:
    ArchiCAD: Full, https://foobar1.com 
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

"""Scenario: Receiving a file"""

"""IFC data must use the "IFC4" schema

BIM data may be structured using a particular version of IFC, 
known as the "schema" version. Newer versions add lots of capabilities like 
extra parameters, new data relationships, and improved data classification. 
The version you choose will affect what data can be stored, and which programs
have support for reading and writing that version. At the moment, you are
likely to specify either "IFC2X3" or "IFC4".
"""


@step('IFC data must use the "{schema}" schema')
def step_impl(context, schema):
    pass


"""Scenario: Exempt files"""

"""The IFC file "PROJECT.ifc" is exempt from being provided

Sometimes, projects may create BIM data that is purely temporary, or as a workaround
that is needed as part of their workflow, but not required from a contractual
perspective. In this case, it is advisable for the requirements to explicitly exclude
these BIM files so that the client knows what is included in the scope of requirements.
Simply specify the name of the file that you know is not required as a deliverable.
"""


@step('The IFC file "{file}" is exempt from being provided')
def step_impl(context, file):
    pass


"""No further requirements are specified because "it will be superseded in a future project phase"

The recipient may not necessarily wish to specify more BIM requirements to audit. Scenarios 
when this is the case may be when the recipient does not have processes in place to use
the BIM data or does not know how to use the BIM data, or when the BIM data is temporary or
irrelevant for any reason. In this scenario, it may be useful to specify the reason why
no further audits will take place. This is the contractual equivalent to "this page is
intentionally left blank".
"""


@step('No further requirements are specified because "{reason}"')
def step_impl(context, reason):
    pass


"""Scenario: Project metadata is organised and correct"""

"""The project must have an identifier of "28q3AgmxP5cepIweO5Of$o"

This is a 22 character GlobalId for a particular IFC element.
"""


@step('The project must have an identifier of "{guid}"')
def step_impl(context, guid):
    pass


"""The project name, code, or short identifier must be "123FOO"

A short poject code or name used to uniquely identify the project, either 
specified by the client or the BIM author
"""


@step('The project name, code, or short identifier must be "{name}"')
def step_impl(context, name):
    pass


"""The project must have a longer form name of "123 Foo Street, Tower B Redevelopment"

The full project name used to uniquely identify the project, either 
specified by the client or the BIM author
"""


@step('The project must have a longer form name of "{long_name}"')
def step_impl(context, long_name):
    pass


"""The project must be described as "Redesign of southwest atrium of Tower B
    to a two-storey space with new interior fitout"

A description of what the project is about, to help clarify the project scope.
"""


@step('The project must be described as "{description}"')
def step_impl(context, description):
    pass


"""The project must be categorised under "Commercial"

If the project is categorised as a particular arbitrary type, it may be described 
here. Example categories could be "Residential", "Retail", "Commercial", "Health"
and "Defence". Alternatively, it could be categorised as "Civic", "Infrastructure".
"""


@step('The project must be categorised under "{object_type}"')
def step_impl(context, object_type):
    pass


""" The project must contain information about the "A" phase

If the project is phased or staged, the phase or stage name may be placed here.
"""


@step('The project must contain information about the "{phase}" phase')
def step_impl(context, phase):
    pass

