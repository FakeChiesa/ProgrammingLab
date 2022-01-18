import unittest

from lezione7 import CSVFile

class Controllo (unittest.TestCase):
    
    def test_init(self):
        csv_file= CSVFile('shampoo sales.csv')

        self.assertEqual(csv_file.name, 'shampoo sales.csv')
        
    def test_get_data(self):
        csv_file= CSVFile('shampoo sales.csv')
        
        data=csv_file.get_data(1, 10)
        self.assertIsInstance(data, list)

    def test_linee_file(self):
        csv_file= CSVFile('shampoo sales.csv')

        esempio=csv_file.get_data(1, 3)
        self.assertEqual(esempio, [['01-02-2012', 145.9], ['01-03-2012', 183.1], ['01-04-2012', 119.3]] )