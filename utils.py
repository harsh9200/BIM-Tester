import re
import inspect
from collections import defaultdict


class Formatter:
    def __init__(self):
        self.start_html = '<code name="Code" value="HI" id="None" contenteditable>'
        self.end_html = '</code>'

    def get_methods(self, class_name):
        members = inspect.getmembers(class_name, predicate=inspect.isfunction)
        function_calls = list(map(lambda z: z[1], members))
        return function_calls
    
    def remove_new_lines(self, text):
        return ' '.join(text.split())

    def add_html_tag(self, text):
        for s in re.findall('"([^"]*)"', text):
            text = text.replace(s, f'{self.start_html}{s}{self.end_html}')
        return text

    def style_doc(self, data):
        Scenario = data[0].split(' ', 1)[1]
        Text = self.add_html_tag(data[1])
        Example = data[2].split(' ', 1)[1]
        Description = data[3].split(' ', 1)[1]
        return Scenario, Text, Example, Description
    
    def format(self, class_name):
        fun_calls = self.get_methods(class_name)

        Final_Docs = defaultdict(list)
        for call in fun_calls:
            docs = inspect.getdoc(call).split('\n\n')
            docs_list = list(map(self.remove_new_lines, docs))
            scen, text, example, description = self.style_doc(docs_list)
            
            Final_Docs[scen].append((text, example, description))
        
        Final_Docs = sorted(Final_Docs.items(), key=lambda z: len(z[1]))
        return Final_Docs