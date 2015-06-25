__author__ = 'cabavs'

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest


class SeleniumTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_main(self):
        driver = self.driver
        driver.get('localhost:8081/')
        self.assertEqual(driver.title, "__SERVER__", "Wrong page name!")
        page_body = driver.find_element_by_tag_name('body').text
        alert = driver.switch_to_alert()

        assert "Server" in page_body
        assert "Percent" in page_body
        assert "Clients" in page_body
        assert "Result" in page_body

        driver.get('localhost:8081/client')
        self.assertEqual(driver.title, "__CLIENT__", "Wrong page name!")
        page_body = driver.find_element_by_tag_name('body').text
        alert = driver.switch_to_alert()

        assert "Client" in page_body
        assert "Sub" in page_body
        assert "Full" in page_body
        assert "len" in page_body

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()