class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
    def print_list(self):
        current=self.head
        while current:          
            print(current.data, end=' ')
            current = current.next

    

def reverse_list(linked_list):
    prev = None
    current = linked_list.head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    linked_list.head = prev    
    return linked_list
def sort(linked_list):
    current = linked_list.head
    while current:
        next = current.next
        while next:
            if current.data > next.data:
                current.data, next.data = next.data, current.data
            next = next.next
        current = current.next
    return linked_list

def merge_sorted_lists(list1, list2):
    merged_list = LinkedList()
    current1 = list1.head
    current2 = list2.head
    while current1 and current2:
        if current1.data < current2.data:
            merged_list.insert_at_end(current1.data)
            current1 = current1.next
        else:
            merged_list.insert_at_end(current2.data)
            current2 = current2.next
    while current1:
        merged_list.insert_at_end(current1.data)
        current1 = current1.next
    while current2: 
        merged_list.insert_at_end(current2.data)
        current2 = current2.next    
    return merged_list

llist = LinkedList()

llist.insert_at_beginning(1)
llist.insert_at_beginning(2)
llist.insert_at_beginning(6)
llist.insert_at_end(4)
llist.insert_at_end(5)
llist.insert_at_end(10)
llist.insert_at_end(3)

print("\nTask 1-1")
llist.print_list()
print()
reversed_list = reverse_list(llist)
reversed_list.print_list()
print()
print("\nTask 1-2")
sorted_list = sort(llist)
sorted_list.print_list()
print()
print("\nTask 1-3")
list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(3)
list1.insert_at_end(5)
list1.insert_at_end(7)
list1.insert_at_end(9)

list2 = LinkedList()
list2.insert_at_end(2)
list2.insert_at_end(4)
list2.insert_at_end(6)
list2.insert_at_end(8)
list2.insert_at_end(10)

merged_list = merge_sorted_lists(list1, list2)
merged_list.print_list()