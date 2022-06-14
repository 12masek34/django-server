from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    """Test new visit"""

    def setUp(self) -> None:
        """install"""
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        """uninstall"""
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """Test todo list"""
        self.browser.get('http://localhost:8000/')

        self.assertIn('To-Do', self.browser.title)
        self.fail('End test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
