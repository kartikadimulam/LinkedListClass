

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

        
    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data=newData

    def setNext(self, newNext):
        self.next = newNext

class Linkedlist:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def addToFront(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)

        #insert at front
        if previous == None:
            temp.setNext(self.head)
            self.head = temp

        #insert anywhere else
        else:
            temp.setNext(current)
            previous.setNext(temp)


    def getList(self):
        current = self.head
        output = ''
        while current != None:
            output += str(current.getData()) + ' '
            current = current.getNext()
        output = output[:len(output)-1] # removes end space
        return output

        
            
