import pandas as pd

class Extractor:
    def __init__(self, path:str):
        self.path = path

    def extract_general_xls(self):
        raw_dataframe = pd.read_excel(self.path,skiprows=range(0, 6))
        return raw_dataframe 
