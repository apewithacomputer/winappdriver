import unittest, os, time
from appium import webdriver


os.startfile("C:\Program Files\Aronium\Aronium.Pos.exe")
os.startfile("C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe")

time.sleep(0.3)


class TypeTest(unittest.TestCase):

    @classmethod

    def setUpClass(self):
        desired_caps = {}
        desired_caps["app"] = "C:\\Program Files\\Aronium\\Aronium.Pos.exe"
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities= desired_caps)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test(self):
        self.driver.find_element_by_xpath("//Pane[@Name=\"Aronium.Pos.Presentation;component/Views/Login.xaml\"][@AutomationId=\"mainFrame\"]").click()
        self.driver.find_element_by_xpath("//Edit[@AutomationId=\'passwordBox\']").send_keys("Future@123")
        self.driver.find_element_by_xpath("//Button[@ClassName=\"Button\"]").click()
        self.driver.find_element_by_xpath("//Edit[@AutomationId=\"PART_TextBox\"]").send_keys("test")
        self.driver.find_element_by_xpath("//Text[@ClassName=\"TextBlock\"][@Name=\"test\"]").click()
        self.driver.find_element_by_xpath("//Button[@ClassName=\"Button\"]/Text[@ClassName=\"TextBlock\"][@Name=\"F10\"]").click()
        self.driver.find_element_by_xpath("//Button[@ClassName=\"Button\"]/Text[@ClassName=\"TextBlock\"][@Name=\"Cash\"]").click()
        self.driver.find_element_by_xpath("//Button[@ClassName=\"Button\"]/Text[@ClassName=\"TextBlock\"][@Name=\"Buttons.SavePdf\"]").click()
        self.driver.find_element_by_xpath("//TreeItem[@Name=\"winappdriver (pinned)\"]").click()
        self.driver.find_element_by_xpath("//Button[@ClassName=\"Button\"][@Name=\"Save\"]").click()
        self.driver.find_element_by_xpath("//Button[@ClassName=\"Button\"][@Name=\"Buttons.Done\"]/Text[@ClassName=\"TextBlock\"][@Name=\"Buttons.Done\"]").click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TypeTest)
    unittest.TextTestRunner(verbosity=2).run(suite) 

time.sleep(5)
