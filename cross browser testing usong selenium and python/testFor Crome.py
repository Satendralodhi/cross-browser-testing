from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import os
class SauceCrossBrowserTest(unittest.TestCase):
   def setUp(self):
       '''
       Start the Selenium WebDriver as a RemoteDriver connecting to Sauce Labs.
       '''
       username = os.environ.get('SAUCE_USERNAME')
       access_key = os.environ.get('SAUCE_ACCESS_KEY')
 
       caps = webdriver.ChromeOptions()
       sauce_caps = {
           "browserName": "Chrome",
           "browserVersion": "latest",
           "platformName": "Windows 10"
       }
       caps.set_capability('sauce:options', sauce_caps)
 
       sauce_url = "https://{}:{}@ondemand.us-west-1.saucelabs.com/wd/hub/".format(username, access_key)
      
       self.driver = webdriver.Remote(
           command_executor=sauce_url,
           options=caps
       )
 
   def tearDown(self):
       '''Quit the browser session once you are finished'''
       self.driver.quit()
 
   def test_sauce_labs(self):
       '''
       The setUp function initializes the right virtual machine browsers  on Sauce Labs
       Tests for a[text()] elements within the Sauce Labs' Homepage Platforms and Pricing
       '''
       self.driver.get("https://www.saucelabs.com")
       element = self.driver.find_element(By.XPATH, '//a[text()="Platform"]')
       self.assertTrue(element.is_displayed())
       element.click()
       pricing_link = self.driver.find_element(By.XPATH, '//a[text()="Pricing"]')
       self.assertTrue(pricing_link.is_displayed())
 
if __name__ == '__main__':
   unittest.main(verbosity=2)