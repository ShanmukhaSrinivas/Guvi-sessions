class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.temp = None
        self.pre = None
        self.count = 0

    def add_node(self,n):
        self.temp = Node(n)
        if self.head == None:
            self.head = self.temp
            self.tail = self.temp
        else:
            self.tail.next = self.temp
            self.tail = self.tail.next
        self.count+=1

    def delRev(self,n):
        if n>self.count:
            print("Limit exceeded")
            return
        else:
            self.res = self.count-(n-1)
            z = self.head
            for _ in range(self.res-1):
                z = z.next
            self.delete_node(z.data)

    def delBeg(self,n):
        if n>self.count:
            print("Limit exceeded")
            return
        else:
            z = self.head
            for _ in range(self.count-1):
                z = z.next
            self.delete_node(z.data)
    
    def delete_node(self,n):
        z = self.head
        if z is not None:
            if z.data == n:
                self.head = z.next
                z = None
                self.count-=1
                return
        while z is not None:
            if z.data==n:
                break
            self.pre = z
            z = z.next
        if z == None:
            self.count-=1
            return
        self.pre.next = z.next
        z = None
        self.count-=1
    def valu(self):
        z = self.head
        while z is not  None:
            print(z.data)
            z = z.next

obj1 = LinkedList()
[obj1.add_node(int(input())) for i in range(5)]
print("Inserted elements:")
obj1.valu()
print("After deleting given value:")
obj1.delete_node(1)
obj1.valu()
print("After deleting value at given index in reverse:")
obj1.delRev(2)
obj1.valu()
print("After deleting value at given index:")
obj1.delBeg(1)
obj1.valu()
