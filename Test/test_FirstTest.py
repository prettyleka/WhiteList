import pytest as pytest
from Test.initPagesWithDriver import init
import psutil


class TestFirstTest:
    def setup_class(self):
        self.initial = init.pageWithDriver()

    def test_CPUTest(self):
        self.initial.goTo.bp.moveToSite("https://translate.google.com/")
        cpu1= psutil.cpu_percent()
        self.initial.goTo.seleniumInfra.close()

        self.initial.goTo.bp2.moveToSite("https://translate.google.com/")
        cpu2 = psutil.cpu_percent()
        self.initial.goTo.seleniumInfraWithAddOn.close()
        print(f"without whitelist CPU is {cpu1}, with - {cpu2}")


    def test_BlockPagesWhiteList(self):
        self.initial.goTo.bp2.moveToSite("chrome-extension://dopjoipaenahonjgpdijmgbdilehfkbl/options.html")
        self.initial.goTo.bp2.clickOnBlockPagesNotInList()
        self.initial.goTo.bp2.moveToSite("https://youtube.com/")


    def test_AddSiteToWhiteList(self):
        self.initial.goTo.bp2.moveToSite("chrome-extension://dopjoipaenahonjgpdijmgbdilehfkbl/options.html")
        self.initial.goTo.bp2.addSiteToWhiteList("smth")
        self.initial.goTo.bp2.moveToSite("https://smth.com/")







if __name__ == '__main__':
    import sys, inspect, os

    clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    class_name = getattr(sys.modules[__name__], clsmembers[0][0])
    module_name = os.path.splitext(os.path.basename(__file__))[0]
    method_list = [func for func in dir(class_name) if
                   callable(getattr(class_name, func)) and not func.startswith("__") and func.startswith("test")]
    function_dict = {}
    function_dict["0"] = "run all tests"
    for i in range(1, len(method_list) + 1):
        function_dict[str(i)] = method_list[i - 1]
    print(function_dict)
    txt = input("please choose test you want to run or debug and then press enter")
    command = "-v " + module_name + ".py::" + clsmembers[0][0] + "::" + function_dict[txt] + ""
    if txt != "0":
        pytest.main(command.split(" "))
    else:
        pytest.main(["-v", module_name + ".py"])