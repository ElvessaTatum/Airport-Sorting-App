import importlib
import os

def fetch_a_criterion(sort_type):
    def format_criterion(sort_type):
        return sort_type.replace(' ', '_')
    
    def load_criterion_module(module_name):
        try:
            return importlib.import_module(module_name).criteria_for_sort
        except ModuleNotFoundError:
            raise Exception("No criterion function found")
        
    module_name = f"sort_criteria.criteria_for_sort_{format_criterion(sort_type)}"

    if 'src' not in os.getcwd().split(os.sep):
        module_name = f"src.{module_name}"

    return load_criterion_module(module_name)

def fetch_criteria():
    return [criteria_file[len("criteria_for_sort_"):-3].replace('_', ' ') for criteria_file in os.listdir(os.path.join(os.path.dirname(__file__), 'sort_criteria')) if criteria_file.endswith(".py")]
