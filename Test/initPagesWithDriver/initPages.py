from Infra.SeleniumInfra import SeleniumInfra
from Infra.SeleniumInfraWithAddOn import SeleniumInfraWithAddOn
from Pages.BasePage import BasePage
from Pages.BasePage2 import BasePage2

class InitPagesWithDriver:
    def __init__(self):
        self.seleniumInfra = SeleniumInfra()
        self.seleniumInfraWithAddOn = SeleniumInfraWithAddOn()
        self.bp = BasePage(self.seleniumInfra)
        self.bp2 = BasePage2(self.seleniumInfraWithAddOn)
