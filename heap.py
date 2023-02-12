##
##
##
## Datastructure:
## Heaps implementation.
##
##
##
##
##



class Node:

    #
    #   Initialise Node with value and right and left
    #   Default:
    #            Parent:None
    #            right:None
    #            left:None
    #
    def __init__(self,value,parent=None,right=None,left=None):
        self.value = value
        self.parent = parent
        self.right = right
        self.left = left

    # String format of node
    def __str__(self):
        return f'Value:{self.value} Parent: {self.parent} left: {self.left}  right: {self.right}'




class Heap:
    '''
            This is implementation of the heap.
            Node:  Act as single leave/branch of heap

    '''    
    
    parentNode = None
##
##intialise the heap with list should be increased
##    
    def __init__(self,heapList):
        self.heapList = heapList
        self.transform()

    '''
        This insert list into heaps
        idea:
        sample: [1,2,3,4,5,6]
            1 ->parentNode
        2->ln       3->rn
       4->ln 5->rn 6->ln

        1. Each node has value, parent node, left node, right node
        2. if Node is None then it is parent
        3. if left or right is None then Not there

        Further development:
            1. Need to understand children insert
            2. Need to check height of the tree concept
    '''
    def transform(self):
        for obj in self.heapList:
            if self.parentNode == None:
                self.parentNode  = Node(obj)
            elif self.parentNode.value != None and self.parentNode.left == None:
                self.parentNode.left = Node(obj,self.parentNode)
            elif self.parentNode.value != None and self.parentNode.left != None and self.parentNode.right == None:
                self.parentNode.right = Node(obj,self.parentNode)
            else:
                print("working on it")

    '''
        Need to insert the array in the heap
    '''
    def insert(self,nodes=self.parent,obj):
        watch = []
        status = []
        nextlevel = []
        watch.insert(nodes)
        while True:
            if watch is None: break
            else:
                node = watch.pop()
                if node is None:
                    self.parent = Node(obj)
                elif node.checkChildren()
        
        
                
     

   def checkThisNodeFirst(node,obj):
       if Node == None:
           node = Node(obj)
        elif Node.value != None and Node.left == None and Node.right == None:
            

                
    '''
        This will print the heaps
    '''
    def printHeap(self,node):
        if node == None:
            return
        else:
            #print(f"Node: {node.value}, left:{str(node.left.value)}, right:{str(node.right.value)}")
            print(f'val :{node.value}')
            if node.left is not None:
                print(f'left: {node.left.value}')
                self.printHeap(node.left)
            if node.right is not None:
                print(f'right:{node.right.value}')
                self.printHeap(node.right)
            
            

    



if __name__ == "__main__":
   test = [1,2,3,4,5,6]
   heap = Heap(test)
   heap.printHeap(heap.parentNode)
