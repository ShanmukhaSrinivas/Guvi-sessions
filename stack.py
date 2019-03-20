l = []

class Stack:

    def push(self):
        l.append(int(input()))

    def pop1(self):
        if len(l) == 0:
            print("Can't pop the element")
        else:
            print(l.pop())


obj = Stack()
[obj.push() for i in range(3)]
[obj.pop1() for j in range(4)]
