from selenium import webdriver
import unittest
import HtmlTestRunner
import time
timestr = time.strftime("%y%m%d-%H%M%S")

class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/home/rajesh/Documents/MCA/4Sem/STP/Automation/chromedriver")
        
        cls.driver.implicitly_wait(1)
        cls.driver.maximize_window()


        
   

    def test_search_google(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("RVCE")
        self.driver.find_element_by_name("btnK").click()
	
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/rajesh/Documents/MCA/4Sem/STP/Automation/report1'))