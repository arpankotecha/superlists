from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from django.contrib.staticfiles.testing import \
        StaticLiveServerTestCase
from unittest import skip
import sys

class FunctionalTest(StaticLiveServerTestCase):
  @classmethod
  def setUpClass(cls):
    for arg in sys.argv:
      if 'liveserver' in arg:
        cls.server_url = "http://" + arg.split('=')[1]
        return 
    super().setUpClass()
    cls.server_url = cls.live_server_url
  #end

  @classmethod
  def tearDownClass(cls):
    if cls.server_url == cls.live_server_url:
      super().tearDownClass()
  #end

  def setUp(self):
    self.browser = webdriver.Chrome()
    self.browser.implicitly_wait(5)
  # end

  def tearDown(self):
    self.browser.quit()
  # end

  def check_for_row_in_list_table(self, row_text):
    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertIn(row_text, [row.text for row in rows])
  # end
# end 
