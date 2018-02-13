import unittest
from mock import patch

from lbryum.util import format_satoshis, user_dir


class TestSatoshis(unittest.TestCase):

    def test_format_satoshis(self):
        result = format_satoshis(1234)
        expected = "0.00001234"
        self.assertEqual(expected, result)

    def test_format_satoshis_diff_positive(self):
        result = format_satoshis(1234, is_diff=True)
        expected = "+0.00001234"
        self.assertEqual(expected, result)

    def test_format_satoshis_diff_negative(self):
        result = format_satoshis(-1234, is_diff=True)
        expected = "-0.00001234"
        self.assertEqual(expected, result)


class TestUserDir(unittest.TestCase):

    def test_user_dir(self):
        with patch.dict('os.environ', {'HOME': '/home/joe/'}, clear=True):
            self.assertEqual('/home/joe/.lbryum', user_dir())
        with patch.dict('os.environ', {'APPDATA': '/home/joe/'}, clear=True):
            self.assertEqual('/home/joe/LBRYum', user_dir())
        with patch.dict('os.environ', {'LOCALAPPDATA': '/home/joe/'}, clear=True):
            self.assertEqual('/home/joe/LBRYum', user_dir())
        with patch.dict('os.environ', {}, clear=True):
            self.assertEqual(None, user_dir())
