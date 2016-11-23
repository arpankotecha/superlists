from .base import FunctionalTest
from unittest import skip

class ItemValidationTest(FunctionalTest):
  def test_cannot_add_empty_list_items(self):
    # Edit goes to the home page and accidentally tries to
    # submit an empty list item. She hits enter on the 
    # empty input box
    self.browser.get(self.server_url)
    self.browser.find_element_by_id(
        'id_new_item').send_keys('\n')

    # The home page refreshes, and there is an error message
    # saying that list items cannot be blank
    error = self.browser.find_element_by_css_selector(
        '.has_error')
    self.assertEqual(error.text,
        "You can't have an empty list item")

    # She tries again with some text for the item, which
    # works
    self.browser.find_element_by_id(
        'id_new_item').send_keys('Buy Milk\n')
    self.check_for_row_in_list_table(
        '1: Buy Milk')

    # Perversely she now tries again to submit a second
    # blank list item
    self.browser.find_element_by_id(
        'id_new_item').send_keys('\n')

    # She receives a similar warning on the list page
    self.check_for_row_in_list_table(
        '1: Buy Milk')
    error = self.browser.find_element_by_css_selector(
        '.has_error')
    self.assertEqual(error.text,
        "You can't have an empty list item")

    # And she can correct it by filling text in
    self.browser.find_element_by_id(
        'id_new_item').send_keys('Make Tea\n')
    self.check_for_row_in_list_table(
        '1: Buy Milk')
    self.check_for_row_in_list_table(
        '2: Make Tea')
  # end
# end

