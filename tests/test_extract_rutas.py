import unittest
from unittest.mock import patch, MagicMock
from src.extract_rutas import extract_rutas

class TestExtractRutas(unittest.TestCase):
    
    @patch('src.extract_rutas.MongoClient')
    def test_extract_rutas(self, MockMongoClient):
        # Setup del mock
        mock_client = MagicMock()
        MockMongoClient.return_value = mock_client
        mock_db = mock_client.__getitem__.return_value
        mock_collection = mock_db.__getitem__.return_value
        mock_collection.find.return_value = [
            {"origen": "A", "destino": "B", "duracion": 60},
            {"origen": "C", "destino": "D", "duracion": 120}
        ]
        
        # Capturar la salida estándar
        with patch('builtins.print') as mocked_print:
            extract_rutas()
            mocked_print.assert_any_call("Ruta de A a B, duración: 60")
            mocked_print.assert_any_call("Ruta de C a D, duración: 120")

if __name__ == '__main__':
    unittest.main()
