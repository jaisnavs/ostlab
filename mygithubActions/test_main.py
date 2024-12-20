import unittest

from main import bye, hello


class TestMain(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "hi")

    def test_bye(self):
        self.assertEqual(bye(), "bye")


if __name__ == "__main__":
    unittest.main()
