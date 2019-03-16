import unittest
from datetime import datetime

from models import PasteBin


class PasteBinTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        attrs = {'data': 'test_data'}
        pastebin = PasteBin(attrs)

        self.assertEqual(pastebin.data, 'test_data')
        self.assertIsNone(pastebin.datetime)

    def test_get_model_keys(self):
        attrs = {}
        pastebin = PasteBin(attrs)

        model_keys = ['title', 'data', 'datetime']

        result = pastebin.get_model_keys()

        self.assertEqual(result, model_keys)

    def test_to_doc(self):
        attrs = {'data': 'test_data'}
        pastebin = PasteBin(attrs)

        doc = {}
        for key in pastebin.get_model_keys():
            doc[key] = None
        doc['data'] = attrs['data']

        result = pastebin.to_doc()

        self.assertEqual(result, doc)

    def test_to_json(self):
        attrs = {'title': 'No', 'data': 'No data', '_id': '12345',
                 'datetime': datetime(2019, 2, 3, 12, 31, 16)}
        pastebin = PasteBin(attrs)

        json = {'title': 'No', 'data': 'No data', 'id': '12345',
                'datetime': '2019-02-03 12:31:16'}

        result = pastebin.to_json()

        self.assertEqual(result, json)
