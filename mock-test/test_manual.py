import unittest
from unittest.mock import patch
import total


class TestTotal(unittest.TestCase):

    def test_cal_total(self):

        patcher = patch('total.read')

        # crate mock obj
        mock_read = patcher.start()

        mock_read.return_value = [1, 2, 3]
        res = total.cal_total('')
        self.assertEqual(res, 6)

        patcher.stop()


# python -m unittest test_manual.py -v