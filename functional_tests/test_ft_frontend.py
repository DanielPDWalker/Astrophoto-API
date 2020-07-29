from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time


MAX_WAIT = 10


class FrontendTest(LiveServerTestCase):
    # Edythe turns on her home edition of AstroPhoto for the first time.
    # (The database will be empty due to LiveServerTestCase)
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_moving_around_the_front_end(self):
        # She opens up the browser and gets to the home page of the AstroPhoto.
        self.browser.get(self.live_server_url)
        self.assertIn("AstroPhoto", self.browser.title)

        # She notices a list of links.
        self.list_of_links = self.browser.find_element_by_tag_name("h3").text
        self.assertIn("Messier Objects", self.list_of_links)

        # Edythe decided to click on the Messier Objects link.

        self.fail('Finish the test_functional_tests.py')
