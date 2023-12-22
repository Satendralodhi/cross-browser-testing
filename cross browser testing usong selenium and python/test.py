from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
class SeleniumCrossBrowserTest(unittest.TestCase):
 
   def setUp(self):
       '''
       Start the Selenium WebDriver in a browser of your choice.
       We use Chrome here but you can replace Chrome with one of the other options.
       '''
       # self.driver = webdriver.Safari()
        #self.driver = webdriver.Edge()
       # self.driver = webdriver.Firefox()
       #self.driver = webdriver.Chrome()
 
   def tearDown(self):
       '''Quit the browser session once you are finished'''
       self.driver.quit()
   def test_sauce_labs(self):
       '''
       The setUp function initializes the right virtual machine browsers  on Sauce Labs
       Tests for a[text()] elements within the Sauce Labs' Homepage Platforms and Pricing
       '''
       self.browser.get("https://www.saucelabs.com")
       element = self.browser.find_element(By.XPATH, '//a[text()="Platform"]')
       self.assertTrue(element.is_displayed())
       element.click()
       pricing_link = self.browser.find_element(By.XPATH, '//a[text()="Pricing"]')
       self.assertTrue(pricing_link.is_displayed())
if __name__ == '__main__':
   unittest.main(verbosity=2)