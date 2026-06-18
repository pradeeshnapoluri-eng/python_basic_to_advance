class Father:
    def show(self):
        print("I am the father")
    def sleep(self):
        print("Father is sleeping")
class Son(Father):
    def show(self):
        print("I am the son")
        super().show()  # Call the show method of the Father class
john = Son()
john.show()
john.sleep() 