class Parent:

    def home(self):
        print("2BHK")

class son(Parent):
    def town(self):
        print("3BHK")

ob_Ref = son()
ob_Ref.home()
ob_Ref.town()