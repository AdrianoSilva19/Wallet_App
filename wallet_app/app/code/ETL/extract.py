import sys
import os
import pandas as pd

try:
    from generic_utils._utils import logging_decorator_factory
except ImportError:
    from app.code.generic_utils._utils import logging_decorator_factory

class Extractor:
    def __init__(self, path:str):
        self.path = path

    #@logging_decorator_factory("High","Path should be str",ValueError,service="Extractor")
    def extract_general_xls(self):
        try:
            path = os.getcwd()
            files = os.listdir(path +"/app/data")
            files_xls = [f for f in files if f[-3:] == 'xls']
            dataframes = []
            for file in files_xls:
                raw_dataframe = pd.read_excel(self.path + file,skiprows=range(0, 6))
                dataframes.append(raw_dataframe)
            if len(dataframes) == 1:
                return dataframes[0]
            return self.concat_multiple_dataframes(dataframes) 
        except ValueError as e:
            raise e    
    
    @staticmethod
    def concat_multiple_dataframes(dataframe:pd.DataFrame):
        final_dataframe = pd.DataFrame()
        
        for df in dataframe:
            final_dataframe = pd.concat([final_dataframe,df]).drop_duplicates().reset_index(drop=True)
        return final_dataframe