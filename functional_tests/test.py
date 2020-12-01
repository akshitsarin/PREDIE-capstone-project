from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
import time


class PredieApp(StaticLiveServerTestCase):
    def set_up(self):
        self.browser = webdriver.Chrome()

    def tear_down(self):
        self.browser.close()

    def test_home_page(self):
        self.browser = webdriver.Chrome()
        self.browser.get(self.live_server_url)
        el = self.browser.find_element_by_id("extraline")
        self.assertEquals(
            el.text, "start exploring right now!")
        self.tear_down()

    def test_login_redirect(self):
        self.browser = webdriver.Chrome()
        self.browser.get(self.live_server_url)
        time.sleep(1)
        my_url = self.browser.current_url
        self.browser.find_element_by_id("login-btn").send_keys(Keys.RETURN)
        self.assertEquals(
            self.browser.current_url, my_url + "login/"
        )
        self.tear_down()

    def test_signup_redirect(self):
        self.browser = webdriver.Chrome()
        self.browser.get(self.live_server_url)
        my_url = self.browser.current_url
        self.browser.find_element_by_id("signup-btn").send_keys(Keys.RETURN)
        time.sleep(1)
        self.assertEquals(
            self.browser.current_url, my_url + "register/"
        )
        self.tear_down()

    def test_navbar_links(self):
        nav_links = [('team', 'the team'),
                     ('about', 'about PREDIE.'), ('contact', 'contact us')]
        self.browser = webdriver.Chrome()
        self.browser.get(self.live_server_url)
        time.sleep(1)
        for link in nav_links:
            self.browser.find_element_by_link_text(
                link[0]).send_keys(Keys.RETURN)
            heading = self.browser.find_element_by_tag_name("h1")
            self.assertEquals(heading.text, link[1])
            time.sleep(1)

        self.tear_down()

    # def test_login(self):
    #     usr = "aaryamann"
    #     pswd = "oreo171171"
    #     self.browser = webdriver.Chrome()
    #     self.browser.get(self.live_server_url)
    #     self.browser.find_element_by_id("login-btn").send_keys(Keys.RETURN)
    #     self.browser.find_element_by_name("username").send_keys(usr)
    #     self.browser.find_element_by_name("password").send_keys(pswd)
    #     self.browser.find_element_by_name("password").send_keys(Keys.RETURN)
    #     time.sleep(1)
        # self.tear_down()
