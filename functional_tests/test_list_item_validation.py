from .base import FunctionalTest
from unittest import skip

class ItemValidationTest(FunctionalTest):
  def test_cannot_add_empty_list_items(self):
    # Edit goes to the home page and accidentally tries to
    # submit an empty list item. She hits enter on the 
    # empty input box

    # The home page refreshes, and there is an error message
    # saying that list items cannot be blank

    # She tries again with some text for the item, which
    # works

    # Perversely she now tries again to submit a second
    # blank list item

    # She receives a similar warning on the list page

    # And she can correct it by filling text in

    self.fail('write me')
  # end
# end

