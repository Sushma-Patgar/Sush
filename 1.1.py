class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList :
    def __init__(self):
        self.head=None

    def prepend (self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode

    def traversal (self):
        curNode=self.head
        while curNode is not None:
            print(curNode.data)
            curNode=curNode.next

    def nodeSearch(self,target):
        curNode=self.head
        while curNode != None and curNode.data != target :
            curNode=curNode.next
        return curNode is not None     

    def remove (self,target):
        predNode=None
        curNode=self.head
        while curNode is not None and curNode.data !=target:
            predNode=curNode
            curNode=curNode.next
        if curNode is not None:
            if curNode is self.head:
                self.head=curNode.next
            else:
                predNode.next=curNode.next
            return True    
        return False    

def main():
        lst1=LinkedList()      
    
        lst=[25,14,36,85,96]
       # ls=["Ravi","25","50000"]
       # print(ls)
            # ls=["Ravi","50","50000"]
        for x in lst:
            lst1.prepend(x)
        lst1.traversal()
        target=int(input("Enter search key:"))
        if (lst1.nodeSearch(target)):
            print("node found in list")
        else:
            print("not Node  found in list")
        target=int(input("Enter node to remove:"))
        if (lst1.remove(target)):
            print("Target removed from list")
        else:
            print(target,"not removed in the list")
        print(lst)
        print("Single linked list traversal")
        lst1.traversal()

if __name__=="__main__":
    main()            

