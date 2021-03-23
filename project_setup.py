class ProjectSetup:
    def schema(self):
        '''
        Scenario: Receiving a file

        The data must use the "{schema}" schema
        
        Example: 
            The data must use the "IFC4" schema
        
        Description: 
            BIM data may be structured using a particular version of IFC, 
            known as the "schema" version. Newer versions add lots of capabilities like 
            extra parameters, new data relationships, and improved data classification. 
            The version you choose will affect what data can be stored, and which programs
            have support for reading and writing that version. At the moment, you are
            likely to specify either "IFC2X3" or "IFC4".
        '''
        pass

    def file_name(self):
        '''
        Scenario: Exempt files

        The IFC file "{file}" is exempt from being provided
        
        Example: 
            The IFC file "PROJECT.ifc" is exempt from being provided
        
        Description: 
            Sometimes, projects may create BIM data that is purely temporary, or as a workaround
            that is needed as part of their workflow, but not required from a contractual 
            perspective. In this case, it is advisable for the requirements to explicitly exclude
            these BIM files so that the client knows what is included in the scope of requirements.
            Simply specify the name of the file that you know is not required as a deliverable.
        '''
        pass

    def reason(self):
        '''
        Scenario: Exempt files

        No further requirements are specified because "{reason}"
        
        Example: 
            No further requirements are specified because "it will be superseded in a
            future project phase"
        
        Description: 
            The recipient may not necessarily wish to specify more BIM requirements to audit.
            Scenarios
            when this is the case may be when the recipient does not have processes in place to use
            the
            BIM data or does not know how to use the BIM data, or when the BIM data is temporary or
            irrelevant for any reason. In this scenario, it may be useful to specify the reason why
            no
            further audits will take place. This is the contractual equivalent to "this page is
            intentionally left blank".
        
        '''
        pass

    def guid(self):
        '''
        Scenario: Project metadata is organised and correct

        The project must have an identifier of "{guid}"
        
        Example: 
            The project must have an identifier of "28q3AgmxP5cepIweO5Of$o"
        
        Description: 
            This is a 22 character GlobalId for a particular IFC element.
        '''
        pass
    
    def name(self):
        '''
        Scenario: Project metadata is organised and correct

        The project name, code, or short identifier must be "{name}"
        
        Example: 
            The project name, code, or short identifier must be "123FOO"
        
        Description: 
            A short project code or name used to uniquely identify the project, either 
            specified by the client or the BIM author
        '''
        pass

    def long_name(self):
        '''
        Scenario: Project metadata is organised and correct
        
        The project must have a longer form name of "{long_name}"
        
        Example: 
            The project must have a longer form name of "123 Foo Street, Tower B Redevelopment"
        
        Description: 
            The full project name used to uniquely identify the project, either 
            specified by the client or the BIM author
        '''
        pass

    def description(self):
        '''
        Scenario: Project metadata is organised and correct
        
        The project must be described as "{description}"
        
        Example:
            The project must be described as "Redesign of southwest atrium of Tower B
            to a two-storey space with new interior fitout"
        
        Description:
            A description of what the project is about, to help clarify the project scope.
        '''
        pass

    def object_type(self):
        '''
        Scenario: Project metadata is organised and correct

        The project must be categorised under "{object_type}"
        
        Example:
            The project must be categorised under "Commercial"
        
        Description:
            If the project is categorised as a particular arbitrary type, it may be described 
            here. Example categories could be "Residential", "Retail", "Commercial", "Health"
            and "Defence". Alternatively, it could be categorised as "Civic", "Infrastructure".
        '''
        pass

    def phase(self):
        '''
        Scenario: Project metadata is organised and correct
        
        The project must contain information about the "{phase}" phase
        
        Example:
            The project must contain information about the "A" phase
        
        Description:
            If the project is phased or staged, the phase or stage name may be placed here.
        '''
        pass