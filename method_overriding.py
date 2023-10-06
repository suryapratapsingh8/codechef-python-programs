class Father:
    def sleep(self):
        print('b/w 10 to 12')

    def eat(self):
        print('father eats')

class Son(Father):
    def sleep(self):
        print("sleep from 2 to 4")
        super().sleep()
s=Son()
s.sleep()