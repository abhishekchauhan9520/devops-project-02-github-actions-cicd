import unittest

from sample_app.app import build_message


class BuildMessageTests(unittest.TestCase):
    def test_default_message(self):
        self.assertEqual(build_message(), "Hello, DevOps!")

    def test_custom_name(self):
        self.assertEqual(build_message("GitHub Actions"), "Hello, GitHub Actions!")

    def test_blank_name_uses_default(self):
        self.assertEqual(build_message("   "), "Hello, DevOps!")


if __name__ == "__main__":
    unittest.main()
