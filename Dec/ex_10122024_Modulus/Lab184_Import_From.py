from browserPackage.OpenBrowser import start_browser
from browserPackage.CloseBrowser import stop_browser

class TestCases:
    def test_case(self):
        start_browser()
        print("Hello Running TC")
        stop_browser()

obj_tc = TestCases()
obj_tc.test_case()