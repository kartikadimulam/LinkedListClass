from linkedlist import Node
from linkedlist import Linkedlist

def test_insertIntoOrderedList():
    ll = Linkedlist()
    ll.add(35)
    ll.add(50)
    ll.add(10)
    ll.add(40)
    ll.add(20)
    ll.add(30)
    assert ll.getList() == '10 20 30 35 40 50'
    ll.add(5)
    assert ll.getList()== '5 10 20 30 35 40 50'
    
