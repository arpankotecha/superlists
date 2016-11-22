from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(FunctionalTest):
  def test_can_start_a_list_and_retrieve_it_later(self):
    # User goes online to check out the home page
    self.browser.get(self.server_url)

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

    # When the user presses enter, taken to a new url
    # the page lists 1: Buy Peacock Feathers as an item in
    # the to-do list table
    inputbox.send_keys(Keys.ENTER)
    list_url = self.browser.current_url
    self.assertRegex(list_url, '/lists/.+')
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

    # Now a new user comes to the site. The previous users
    # list should not be on there.
    self.browser.quit()
    self.browser = webdriver.Chrome()

    # Francis visits the home page. There is no sign of 
    # Ediths list
    self.browser.get(self.server_url)
    page_text = self.browser.find_element_by_tag_name(
        'body').text
    self.assertNotIn('Buy Peacock Feathers', page_text)
    self.assertNotIn('make a fly', page_text)

    # Francis stats a new list
    inputbox = self.browser.find_element_by_id(
        'id_new_item')
    inputbox.send_keys('Buy Milk')
    inputbox.send_keys(Keys.ENTER)

    # Francis gets his own unique url
    francis_list_url = self.browser.current_url
    self.assertRegex(francis_list_url, '/lists/.+')
    self.assertNotEqual(francis_list_url, list_url)

    # This should not have ediths list.
    page_text = self.browser.find_element_by_tag_name(
        'body').text
    self.assertNotIn('Buy Peacock Feathers', page_text)
    self.assertIn('Buy Milk', page_text)
  # end
# end
