import unittest
from datetime import datetime
from bson import ObjectId

from repositories import PasteBinRepository
from infrastructure import EnvironmentManager
from models import PasteBin


class PasteBinRepositoryTest(unittest.TestCase):
    def setUp(self):
        self.repo = PasteBinRepository()

    def tearDown(self):
        del self.repo

    def test_insert_one(self):
        dt = datetime(2019, 2, 3, 12, 31, 52)
        attrs = {'title': 'NoTitle', 'data': 'NoData', 'datetime': dt}
        pastebin = PasteBin(attrs)

        result = self.repo.insert_one(pastebin)

        self.assertIsInstance(result, ObjectId)

        self.repo.collection.delete_one({'_id': result})

    def test_find_one(self):
        dt = datetime(2019, 2, 3, 12, 31, 52)
        attrs = {'title': 'NoTitle', 'data': 'NoData', 'datetime': dt}
        pastebin = PasteBin(attrs)

        to_db = self.repo.insert_one(pastebin)

        from_db = self.repo.find_one({'_id': to_db})

        self.assertIsInstance(from_db, PasteBin)
        self.assertEqual(from_db._id, str(to_db))
        self.assertEqual(from_db.title, attrs['title'])
        self.assertEqual(from_db.data, attrs['data'])
        self.assertEqual(from_db.datetime, attrs['datetime'])

        self.repo.collection.delete_one({'_id': to_db})
