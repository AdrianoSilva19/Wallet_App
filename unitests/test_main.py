import unittest
from code.main import handle_pipeline
from unittest.mock import MagicMock, patch, Mock, call, PropertyMock, ANY

class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        """Setting up the test case"""
        self.py_file = "code.main"

    def test_handle_pipeline(self):
        """Mocking the Extractor, Transformer and Viewer classes 
        and testing if the methods are called correctly in the handling of data pipeline.
        """
        
        with patch(f"{self.py_file}.Extractor") as mock_extractor, \
            patch(f"{self.py_file}.Transformer") as mock_transformer, \
            patch(f"{self.py_file}.Viewer") as mock_viewer:
            
            handle_pipeline()
            mock_extractor.assert_called_once()
            mock_transformer.assert_called_once()
            mock_viewer.assert_called_once()
            mock_viewer().barplot_monthly_balance.assert_called_once()
            mock_viewer().barplot_general.assert_called_once()
    
    