import unittest
import pandas as pd
from code.ETL.transform import Transformer  
from unittest.mock import MagicMock, patch, Mock, call, PropertyMock, ANY


class TestTransformer(unittest.TestCase):
    def setUp(self) -> None:
        """Setting up the test case"""
        self.py_file = "code.ETL.transform"
        self.transformer = Transformer("dataframe")

    def test_handler(self):
        """Testing if the method handler is correctly transforming the data"""
           
        with patch(f"{self.py_file}.Transformer.select_holidays_expenses") as mock_select_holidays_expenses, \
            patch(f"{self.py_file}.Transformer.extract_wages") as mock_extract_wages, \
            patch(f"{self.py_file}.Transformer.extract_house_expenses") as mock_extract_house_expenses:
            
            self.transformer.handler()
            mock_select_holidays_expenses.assert_called_once()
            mock_extract_wages.assert_called_once()
            mock_extract_house_expenses.assert_called_once()