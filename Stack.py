class stack:
    def __init__(self):  # Constructor Function
        self.lst = []

    def push(self,value):
        self.lst.append(value)

    def isempty(self):
        if len(self.lst) == 0:
            return True
        return False


    def pop(self):
        if self.isempty() == True:
            return "Underflow" 
        else:
            self.lst.pop()
    def peek(self,value):
        return self.lst[value-1]
    def count(self): 
        return len(self.lst)
    def change(self,position,value):
        self.lst[position]=value 
    def display(self):
        for i in range(1,len(self.lst)):
            print(self.lst[len(self.lst)-i])
            if i==len(self.lst)-1: 
                i=i+1
                print(self.lst[len(self.lst)-i]) 




s = stack()
# peek(): It returns the element at the given position.
# ● count(): It returns the total number of elements available in a stack.
# ● change(): It changes the element at the given position.
# ● display(): It prints all the elements available in the stack.
while True: 
    print("1: push\n 2:pop \n 3:isempty \n 4:peek \n 5:count \n 6:change \n 7:display")
    print("\n")
    x=int(input())
    if x==1:
        print("\n")
        value=int(input('Enter the number you want to push: ')) 
        s.push(value)
    elif x==2: 
        print("\n")
        print(s.pop())
    elif x==3:
        print("\n")
        print(s.isempty())
    elif x==4:
        print("\n")
        val=int(input("Enter a position: "))
        print(s.peek())
    elif x==5: 
        print("\n")
        print(s.count())
    elif x==6: 
        print("\n")
        position=int(input("Enter a position: "))
        v=int(input("Enter a value"))
        s.change(position,value)
    elif x==7:
        print("\n")
        s.display()
