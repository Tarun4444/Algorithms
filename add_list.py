class SinglyLinkedListNode:
    def __init__(self,node_data):
        self.data=node_data
        self.next=None

class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert_node(self,node_data):
        node=SinglyLinkedListNode(node_data)

        if not self.head:
            self.head=node
        else:
            self.tail.next=node

        self.tail=node

    def printLinkedList(self):
        while(self.head):
            print(self.head.data)
            self.head=self.head.next

    def reverseAdd(self):
        head=self.head
        prev=None
        curr=head

        """while(curr):
            print(curr.data)
            curr=curr.next"""
        while(head):
            curr=curr.next
            head.next=prev
            prev=head
            head=curr

        self.head=prev

    def add(self,head2):
        head1 = self.head

        while(head2):
            head1.data=head1.data + head2.data
            head2=head2.next
            head1=head1.next

        while(head1):
            head1 = head1.next

def main():
    llist1_count = 3
    llist2_count = 2

    llist1 = SinglyLinkedList()
    llist2 = SinglyLinkedList()
    llist3 = SinglyLinkedList()

    for _ in range(llist1_count):
        llist_item = int(input())
        llist1.insert_node(llist_item)

    for _ in range(llist2_count):
        llist_item = int(input())
        llist2.insert_node(llist_item)

    #llist1.printLinkedList()
    #llist2.printLinkedList()

    #print(llist1.head.data)

    #add(llist1.head,llist2.head,llist3.head)

    llist1.reverseAdd()
    llist2.reverseAdd()

    llist1.add(llist2.head)
    llist1.reverseAdd()
    llist1.printLinkedList()
main()