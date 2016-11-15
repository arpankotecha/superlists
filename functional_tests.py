from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
  def setUp(self):
    self.browser = webdriver.Firefox()
    self.browser.implicitly_wait(3)
  # end

  def tearDown(self):
    self.browser.quit()
  # end

  def check_for_row_in_list_table(self, row_text):
    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertIn(row_text, [row.text for row in rows])
  # end

  def test_can_start_a_list_and_retrieve_it_later(self):
    # User goes online to check out the home page
    self.browser.get('http://localhost:8000')

    # Notice page title and header mention to-do lists
    self.assertIn('To-Do', self.browser.title)
    header_text = self.browser.find_element_by_tag_name(
            'h1').text
    self.assertIn('To-Do', header_text)

    # Invited to enter a to-do item right away
    inputbox = self.browser.find_element_by_id(
      'id_new_item')
    self.assertEqual(
      inputbox.get_attribute('placeholder'),
      'Enter a to-do item')

    # The user enters "Buy Peacock Feathers" into a text
    # box
    inputbox.send_keys('Buy Peacock Feathers')

    # When the user presses enter, the page updates and now
    # the page lists 1: Buy Peacock Feathers as an item in
    # the to-do list table
    inputbox.send_keys(Keys.ENTER)
    self.check_for_row_in_list_table(
        '1: Buy Peacock Feathers')

    # The user enters another item and clicks enter
    inputbox = self.browser.find_element_by_id(
        'id_new_item')
    inputbox.send_keys("Use Peacock Feathers to make a fly")
    inputbox.send_keys(Keys.ENTER)

    # The page updates again, now shows both items
    self.check_for_row_in_list_table(
        '1: Buy Peacock Feathers')
    self.check_for_row_in_list_table(
        '2: Use Peacock Feathers to make a fly')

    self.fail("Finish this test")
  # end
# end

if __name__ == "__main__":
  unittest.main()

assert 'To-Do' in browser.title


