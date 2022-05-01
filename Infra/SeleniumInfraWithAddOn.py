from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as actions
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumInfraWithAddOn:
    TIME_TO_WAIT = 60

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('disable-notifications')
        chrome_options.add_extension("//Tools/Whitelist.crx")
        self.driver = webdriver.Chrome("//Tools/chromedriver", options=chrome_options)

    def openSite(self, link):
        self.driver.get(link)
        self.driver.maximize_window()

    def close(self):
        try:
            self.driver.quit()
        except:
            print("There is no option to quit")

    def clickButton(self, locatorType: By = None, locatorValue: str = None, element: WebElement = None,
                    fromElement: WebElement = None, timeToWait: int = TIME_TO_WAIT):
        if not element:
            element = self.findElementBy(locatorType=locatorType, locatorValue=locatorValue, fromElement=fromElement,
                                         timeToWait=timeToWait)
        try:
            element.click()
            print("[Pressed]- element " + str(locatorValue) + " is pressed")
        except Exception as e:
            assert False, "the element " + str(locatorValue) + " found but we cant click on it!"

    def findElementBy(self, locatorType=None, locatorValue=None, fromElement=None,
                      timeToWait=TIME_TO_WAIT) -> WebElement:
        retries = 1
        wait = WebDriverWait(self.driver, timeToWait)
        while retries > 0:
            try:
                self.waitUntil(timeToWait)
                timeToWait = None
                if (not fromElement):
                    if (locatorType == "id"):
                        element = wait.until(EC.visibility_of_element_located((By.ID, locatorValue)))
                    elif (locatorType == "xpath"):
                        element = wait.until(EC.visibility_of_element_located((By.XPATH, locatorValue)))
                    elif (locatorType == "class_Name"):
                        element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, locatorValue)))
                    elif locatorType == "ids":
                        element = self.driver.find_elements(locatorValue)
                else:
                    if (locatorType == "id"):
                        element = fromElement.find_element_by_id(locatorValue)
                    elif (locatorType == "xpath"):
                        element = fromElement.find_element_by_xpath(locatorValue)
                    elif (locatorType == "class_Name"):
                        element = fromElement.find_elements_by_class_name(locatorValue)
                print("[findElementBy]- Element Does FOUND with:" + str(locatorType) + " " + str(locatorValue))
                return element
            except:
                raise Exception("[findElementBy]- Element Does NOT FOUND with:" + str(locatorType) + " " + str(
                    locatorValue) + " check this warning its can be a bug!!!")