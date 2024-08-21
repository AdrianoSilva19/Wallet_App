import pandas as pd
from ETL.extract import Extractor
from ETL.transform import Transformer   
from viewer.viewer import Viewer

def handle_pipeline():
    exctractor = Extractor(path=r"data/descarga.xls")
    raw_dataframe = exctractor.extract_general_xls()    
    transformer = Transformer(dataframe=raw_dataframe)

    transformed_data = transformer.handler()
    viewer = Viewer(transformed_data)
    viewer.barplot_monthly_balance()
    viewer.barplot_general()



    



if __name__ == "__main__":
    handle_pipeline()