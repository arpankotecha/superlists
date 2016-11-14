from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
  def setUp(self):
    self.browser = webdriver.Firefox()
    self.browser.implicitly_wait(3)
  # end

  def tearDown(self):
    self.browser.quit()
  # end

  def test_can_start_a_list_and_retrieve_it_later(self):
    # User goes online to check out the home page
    self.browser.get('http://localhost:8000')

    # Notice page title and header mention to-do lists
    self.assertIn('To-Do', self.browser.title)
    self.fail("Finish this test")
  # end
# end

if __name__ == "__main__":
  unittest.main()

assert 'To-Do' in browser.title


