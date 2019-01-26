class LinkedList:
    def __init__(self,x):
        self.val = x
        self.next = None

def create():
    temp = LinkedList(1)
    temp.next = LinkedList(-2)

    while temp:
        print(temp.val)
        temp = temp.next

if __name__ == '__main__':
    create()