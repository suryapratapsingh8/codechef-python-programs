class Demo:
    def add(self,*args):
        t=0
        for i in args:
            t+=i  
        return t
    
    
d=Demo()
print(d.add(2,3,4,5,6,7))


        