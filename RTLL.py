# cook your dish here
'''n=int(input())
l=list(map(int,input().split()))

print(*l[::-1])'''

class node:
    def __init__(self,value):
        self.data=value
        self.next=None
        
        
    
class linked_list:
    def __init__(self):
        self.head=None
        
    def insert(self,value):
        new_node=node(value)
        new_node.next=self.head
        self.head=new_node
        
    def output(self):
        curr=self.head
        while curr!=None:
            print(curr.data,end=' ')
            curr=curr.next
            
obj=linked_list()

n =int(input())
l= list(map(int,input().split()))
for i in range(n):
    obj.insert(l[i])
obj.output()

