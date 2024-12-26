import sys
import pandas as pd

try:
    from .ETL.extract import Extractor
    from .ETL.transform import Transformer

except ImportError:
    from app.code.ETL.extract import Extractor
    from app.code.ETL.transform import Transformer



def handle_pipeline():
    try:
        exctractor = Extractor(path="app/data/descarga.xls")
        raw_dataframe = exctractor.extract_general_xls()
        transformer = Transformer(dataframe=raw_dataframe)

        transformed_data = transformer.handler()
        return transformed_data

    except Exception as e:
        raise e

if __name__ == "__main__":
    handle_pipeline()