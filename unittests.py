import unittest
from argparse import Namespace
from app import run


class TestPeriodicEvents(unittest.TestCase):
    def test_1h(self):
        args = {
            "period": "1h",
            "tz": "Europe/Athens",
            "t1": "20210714T204603Z",
            "t2": "20210715T123456Z",
        }

        expected_output = [
            "20210714T210000Z",
            "20210714T220000Z",
            "20210714T230000Z",
            "20210715T000000Z",
            "20210715T010000Z",
            "20210715T020000Z",
            "20210715T030000Z",
            "20210715T040000Z",
            "20210715T050000Z",
            "20210715T060000Z",
            "20210715T070000Z",
            "20210715T080000Z",
            "20210715T090000Z",
            "20210715T100000Z",
            "20210715T110000Z",
            "20210715T120000Z",
        ]
        self.assertEqual(run(Namespace(**args)), expected_output)

    def test_1d(self):
        args = {
            "period": "1d",
            "tz": "Europe/Athens",
            "t1": "20211010T204603Z",
            "t2": "20211115T123456Z",
        }

        expected_output = [
            "20211010T210000Z",
            "20211011T210000Z",
            "20211012T210000Z",
            "20211013T210000Z",
            "20211014T210000Z",
            "20211015T210000Z",
            "20211016T210000Z",
            "20211017T210000Z",
            "20211018T210000Z",
            "20211019T210000Z",
            "20211020T210000Z",
            "20211021T210000Z",
            "20211022T210000Z",
            "20211023T210000Z",
            "20211024T210000Z",
            "20211025T210000Z",
            "20211026T210000Z",
            "20211027T210000Z",
            "20211028T210000Z",
            "20211029T210000Z",
            "20211030T210000Z",
            "20211031T220000Z",
            "20211101T220000Z",
            "20211102T220000Z",
            "20211103T220000Z",
            "20211104T220000Z",
            "20211105T220000Z",
            "20211106T220000Z",
            "20211107T220000Z",
            "20211108T220000Z",
            "20211109T220000Z",
            "20211110T220000Z",
            "20211111T220000Z",
            "20211112T220000Z",
            "20211113T220000Z",
            "20211114T220000Z",
        ]
        self.assertEqual(run(Namespace(**args)), expected_output)

    def test_1mo(self):
        args = {
            "period": "1mo",
            "tz": "Europe/Athens",
            "t1": "20210214T204603Z",
            "t2": "20211115T123456Z",
        }

        expected_output = [
            "20210228T220000Z",
            "20210331T210000Z",
            "20210430T210000Z",
            "20210531T210000Z",
            "20210630T210000Z",
            "20210731T210000Z",
            "20210831T210000Z",
            "20210930T210000Z",
            "20211031T220000Z",
        ]
        self.assertEqual(run(Namespace(**args)), expected_output)

    def test_1y(self):
        args = {
            "period": "1y",
            "tz": "Europe/Athens",
            "t1": "20180214T204603Z",
            "t2": "20211115T123456Z",
        }

        expected_output = [
            "20181231T220000Z",
            "20191231T220000Z",
            "20201231T220000Z",
        ]
        self.assertEqual(run(Namespace(**args)), expected_output)

    def test_failure(self):
        args = {
            "period": "1year",
            "tz": "Europe/Athens",
            "t1": "20180214T204603Z",
            "t2": "20211115T123456Z",
        }

        self.assertRaises(Exception, run, Namespace(**args))


if __name__ == "__main__":
    unittest.main()
