import sys
import pandas as pd

try:
    from ETL.extract import Extractor
    from ETL.transform import Transformer   
    from viewer.viewer import Viewer

except ImportError:
    from code.ETL.extract import Extractor
    from code.ETL.transform import Transformer   
    from code.viewer.viewer import Viewer


def handle_pipeline():
    try:
        exctractor = Extractor(path="data/descarga.xls")
        raw_dataframe = exctractor.extract_general_xls()    
        transformer = Transformer(dataframe=raw_dataframe)

        transformed_data = transformer.handler()
        viewer = Viewer(transformed_data)
        viewer.barplot_monthly_balance()
        viewer.barplot_general()
    except Exception as e:
        raise e

if __name__ == "__main__":
    handle_pipeline()