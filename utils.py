import os
import re
import ast
import json
import inspect
import importlib
from glob import glob
from itertools import chain
from collections import OrderedDict


def create_requirement(info_dict, path):
    text = ''
    intro = info_dict.get("feature_intro").replace('\r', '')
    text += f'{info_dict.get("feature_name")}\n\n{intro}\n\n'
    for scenario_dict in json.loads(info_dict['scenario']):
        if scenario_dict['scenario']:
            text += f"{scenario_dict['name']}\n*"
            text += '\n*'.join(scenario_dict['scenario']) + '\n\n'

    with open(path.rsplit('.')[0] + '.feature', 'w') as f:
        f.write(text)


class Format:
    def __init__(self, file_name):
        self.file_docs = inspect.getdoc(file_name)
        self.file_source = inspect.getsource(file_name)
        self.file_tree_struct = ast.parse(self.file_source).body[1:]

    def extract_vendors_info(self, vendors_docs):
        vendors_info = re.findall('(\w*)\s*: (.*), (.*)', vendors_docs)
        vendors_info_dict = {
            k: (v1, v2) for k, v1, v2 in vendors_info
        }
        return vendors_info_dict

    def insert_html(self, text):
        text = text.replace("'", '')
        for s in re.findall('"([^"]*)"', text):
            text = text.replace(
                s, f'<code contenteditable>{s}</code>')
        return text

    def extract_steps_info(self):
        steps_dict = OrderedDict()

        for node in self.file_tree_struct:
            if isinstance(node, ast.FunctionDef):
                # This section is for processing Funtions
                value = node.decorator_list[0].args[0].value
                steps_dict[key][-1].insert(0, self.insert_html(value))

            elif isinstance(node, ast.Expr):
                # This section is for processing docstring
                value = node.value.s
                if "Scenario:" in value:
                    key = value
                    steps_dict[key] = list()
                else:
                    steps_dict[key].append(value.split('\n\n'))
        return steps_dict

    def save_as_json(self, save_path):
        feat_name, feat_info, *vendors_info = self.file_docs.split('\n\n')
        vendors_imp, vendors_exp = tuple(
            map(self.extract_vendors_info, vendors_info))

        json_data = {
            'featureName': feat_name,
            'featureInfo': feat_info,
            'vendorsImport': vendors_imp,
            'vendorsExport': vendors_exp,
            'scenarios': self.extract_steps_info()
        }

        with open(save_path, 'w') as f:
            json.dump(json_data, f)


class Generate_JSON:
    def __init__(self):
        self.features_path = 'features/steps/*'

    def subfolder_list(self, ext):
        folders = [glob(f'{folder}/*{ext}')
                   for folder in glob(self.features_path) if os.path.isdir(folder)]
        return list(chain(*folders))

    def generate(self):
        for subfolder in self.subfolder_list('py'):
            subfolder = subfolder.rsplit('.')[0].replace('\\', '/')
            mod = importlib.import_module(subfolder.replace('/', '.'))
            Format(mod).save_as_json(f"{subfolder}.json")

    def json_list(self):
        return self.subfolder_list('json')

    def features_dict(self):
        feat_list = self.json_list()
        feat_dict = dict(zip(map(lambda t: os.path.basename(
            os.path.dirname(t)), feat_list), feat_list))
        return feat_dict


