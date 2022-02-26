"""list

class:

    _LinkedList

functions:

    print()
    len()
    insert_at_begining(data)
    insert_at_end(data)
    insert_at(index, data)
    insert_values(data_list)
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
        
class _LinkedList:
    
    
    def __init__(self):
        self.head = None
        
        
    def print(self):
        if self.head is None:
            print('List is empty')
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)
        
        
    def __len__(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
    
    
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data, None)
        
        
    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception('Invalid Index')
        if index==0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
            
            
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)