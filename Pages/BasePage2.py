from Infra.SeleniumInfraWithAddOn import SeleniumInfraWithAddOn

class BasePage2:
    def __init__(self, seleniumInfra:SeleniumInfraWithAddOn):
        self.seleniumInfra = seleniumInfra


    def moveToSite(self,link):
        self.seleniumInfra.openSite(link=link)

    def clickOnBlockPagesNotInList(self):
        btn = self.seleniumInfra.findElementBy(locatorType='id', locatorValue="app-options-block-pages")
        self.seleniumInfra.clickButton(element=btn)

    def addSiteToWhiteList(self, name):
        textArea = self.seleniumInfra.findElementBy(locatorType='xpath', locatorValue="//textarea[@id='app-options-whitelist']")
        textArea.send_keys(name)
