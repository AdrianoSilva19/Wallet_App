import unittest
import pandas as pd
from code.ETL.extract import Extractor  
from unittest.mock import MagicMock, patch, Mock, call, PropertyMock, ANY


class TestExtractor(unittest.TestCase):
    def setUp(self) -> None:
        """Setting up the test case"""
        self.py_file = "code.ETL.extract"
        self.path = "data/descarga.xls"
        self.wrong_path = int(1334)

    def test_Extractor(self):
        """Testing if the Extractor class is correctly instantiated"""
        extractor = Extractor(path=self.path)
        self.assertIsInstance(extractor, Extractor)
        self.assertEqual(extractor.path, self.path)
    
    @patch('code.ETL.extract.logging_decorator_factory')
    def test_extract_general_xls(self,mock_logging_decorator_factory):
        """Testing if the method extract_general_xls is correctly extracting data"""
        extractor = Extractor(path=self.path)
        raw_dataframe = extractor.extract_general_xls()
        self.assertIsInstance(raw_dataframe, pd.DataFrame)
