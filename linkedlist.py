class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def taking_input():
    l=[int(ele) for ele in input().split()]
    head=None
    for ele in l:
        new_node=Node(ele)
        if head is None:
            head=new_node
        else:
            curr=head
            while curr.next is not None:
                curr=curr.next
            curr.next=new_node
    return head
def printLL(Head):
   while Head is not None:
        print(Head.data,end=" ")
        Head=Head.next
