import unittest
from unittest.mock import patch
import total


class Testtotal(unittest.TestCase):

    def test_cal_total(self):
        with patch('total.read') as mock_read:
            mock_read.return_value = [1, 2, 3]
            res = total.cal_total('')
            self.assertEqual(res, 6)


# python -m unittest test_context_manager.py -v