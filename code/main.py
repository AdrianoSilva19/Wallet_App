import pandas as pd
from ETL.extract import Extractor
from ETL.transform import Transformer   
from viewer.viewer import Viewer

def handle_pipeline():
    exctractor = Extractor(path=r"data/descarga.xls")
    raw_dataframe = exctractor.extract_general_xls()    
    transformer = Transformer(dataframe=raw_dataframe)
    holidays_expenses = transformer.select_holidays_expenses()
    ctw_wages = transformer.extract_wages()

    whole_data = {"wages":ctw_wages,"holidays_expenses":holidays_expenses} 
    #viewer = Viewer(whole_data)
    #viewer.piechart_holidays()


    



if __name__ == "__main__":
    handle_pipeline()