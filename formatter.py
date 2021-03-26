import re
import inspect
from utils import remove_arrows, remove_spaces, insert_html


class Formatter:
    def __init__(self, filename):
        self.file_docs = inspect.getdoc(filename).split('\n\n')
        self.file_source = inspect.getsource(filename)
        self.vendor_pattern = '\[(.*?)\]'
        self.step_pattern = '@step\((.*?)\)'
    
    def get_intro(self) -> list:
        return list(map(remove_spaces, self.file_docs[0].split('\n')[2:]))

    def get_vendors(self) -> list:
        v = re.findall(self.vendor_pattern, ''.join(self.file_docs[2:4]))
        vendors = v[0].split(', ') + v[1].split(', ')
        return vendors
    
    def get_headings(self, req=False) -> list:
        steps = re.findall(self.step_pattern, self.file_source)
        steps = [insert_html(step, req=req) for step in  steps]
        return steps
    
    def get_scenarios(self) -> dict:
        Data = {}
        for scenario in self.file_docs[4:]:
            scenario = list(map(remove_spaces, scenario.split('\n    \n')))
            Examples = list(map(remove_arrows, scenario[1::2]))
            Description = scenario[2::2]
            Data[scenario[0]] = list(zip(Examples, Description))
        return Data
