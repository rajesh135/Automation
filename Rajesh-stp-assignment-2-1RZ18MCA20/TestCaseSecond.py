from selenium import webdriver
import unittest
import HtmlTestRunner
import time
timestr = time.strftime("%y%m%d-%H%M%S")

class LaunchFacebook(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/home/rajesh/Documents/MCA/4Sem/STP/Automation/chromedriver")
        
        cls.driver.implicitly_wait(1)
        cls.driver.maximize_window()


        
   

    def test_search_automationstepbystep(self):
        
        self.driver.get("https://www.facebook.com/")
        self.driver.find_element_by_name("email").send_keys("rajesh@gmail.com")
        self.driver.find_element_by_name("pass").send_keys("rajesh@gmail.com")

        self.driver.find_element_by_id("loginbutton").click()
        

        self.driver.get("https://www.facebook.com/")

			#Uname empty, password valid and login failed because wrong  user details
        self.driver.find_element_by_name('email').send_keys('')  # Enter empty Name
        self.driver.find_element_by_name('pass').send_keys('root123')  # Enter Password
        self.driver.find_element_by_id("loginbutton").click()
        self.driver.save_screenshot('/home/rajesh/Documents/AssignmentSecond/reports/failed.png')
        time.sleep(2)
        
        self.driver.get("https://www.facebook.com/")
		# Uname valid, password empty and login failed because wrong  user details
        self.driver.find_element_by_name('email').send_keys('admin')  # Enter correct Name
        self.driver.find_element_by_name('pass').send_keys('')  # Enter empty Password
        self.driver.find_element_by_id("loginbutton").click()
        self.driver.save_screenshot('/home/rajesh/Documents/AssignmentSecond/reports/failedpwdempty.png')
        time.sleep(2)

        self.driver.get("https://www.facebook.com/")
		# Uname empty, password empty and login failed because wrong  user details
        self.driver.find_element_by_name('email').send_keys('')  # Enter correct Name
        self.driver.find_element_by_name('pass').send_keys('')  # Enter empty Password
        self.driver.find_element_by_id("loginbutton").click()
        self.driver.save_screenshot('/home/rajesh/Documents/AssignmentSecond/reports/failedunameempty.png')
        time.sleep(2)
        
        self.driver.get("https://www.facebook.com/")
		# Uname , password  and login failed because wrong element id  details
        self.driver.find_element_by_name('email').send_keys('rajesh')  # Enter correct Name
        self.driver.find_element_by_name('pass').send_keys('rajesh')  # Enter empty Password
        self.driver.find_element_by_id("loginbutton").click()#wrong element id
        self.driver.save_screenshot('/home/rajesh/Documents/AssignmentSecond/reports/failedwrongelementid.png')
        time.sleep(2)


  
	
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/rajesh/Documents/MCA/4Sem/STP/Automation/report1'))