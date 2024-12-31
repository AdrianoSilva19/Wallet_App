import sys
import pandas as pd

try:
    from generic_utils._utils import logging_decorator_factory
except ImportError:
    from app.code.generic_utils._utils import logging_decorator_factory

class Extractor:
    def __init__(self, path:str):
        self.path = path

    @logging_decorator_factory("High","Path should be str",ValueError,service="Extractor")
    def extract_general_xls(self):
        try:
            print(self.path)
            raw_dataframe = pd.read_excel(self.path,skiprows=range(0, 6))
            print(raw_dataframe.head())
            return raw_dataframe 
        except ValueError as e:
            raise e    