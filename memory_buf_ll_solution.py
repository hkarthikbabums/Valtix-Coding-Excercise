i
# Node class
class Node():

    # Constructor to initialize the node object
    def __init__(self, data,buf_size):
        self.data = data         # Node ID
        self.mem = buf_size      # Memory Size
        self.next = None         # Initialize next as null

# Linked List class
class LL():

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def add(self,data,buf_size):
        if not self.head:
            self.head = Node(data,buf_size)
        else:
            newnode = Node(data,buf_size)
            newnode.next = self.head
            self.head = newnode

    # Function to traverse the linked list and print their id and memory allocated
    def print(self):
        temp = self.head
        while temp:
            if temp.next:
                print(f"{temp.data}: {temp.mem}", end=" -> ")
            else:
                print(f"{temp.data}: {temp.mem}\n")
            temp = temp.next

    # Function to print the head of the linked list
    def printhead(self):
        print(f"\nHead of the linked list is {self.head.data}\n")

    # Function to find the node to be split
    def find_the_node_to_split(self, splitpoint):
        curr = self.head
        sum = 0

        while curr:
            if sum <= splitpoint and curr.mem + sum <= splitpoint:
                sum += curr.mem
                curr = curr.next
            else:
                break
        return curr, abs(sum-splitpoint)

    # Function to
    #   1, Split the memory
    #   2, Create a new node with the remaining memory
    #   3, Insert the new node next to the split node in the linked list
    #   4, Update the new splitted memory value in the split node

    def mem_split(self, splitpoint):
        node_to_split, sum_to_split = self.find_the_node_to_split(splitpoint)

        if sum_to_split + splitpoint == splitpoint:
            print("Able to allocate the memory for the given mem len without node split\n")
            return

        print("To Allocate the needed memory we need to be splitting the node \n"
              "and creating a new node with the remaining memory after allocation\n")

        print(f"The node identified to split is {node_to_split.data}\n")

        #create a new node with the after split remaining memory
        new_node_mem = node_to_split.mem - sum_to_split
        new_node_data = str(node_to_split.data) + str("-1")

        #Create a new node to insert in the existing linked list
        newnode = Node(new_node_data, new_node_mem)
        newnode.next = node_to_split.next
        node_to_split.next = newnode

        #Change the mem value in the spliited node
        node_to_split.mem = sum_to_split

    # Function to
    #   1, Allocate the memory asked from the head of the linked list
    #   2, Once allocated remove the nodes from the linked list
    #   3, Change the linked list pointing to the next memory available node for allocation
    def allocate_mem(self, total_mem_need_to_allocate):
        curr = self.head
        sum = 0

        while curr:
            if sum <= total_mem_need_to_allocate and curr.mem + sum <= total_mem_need_to_allocate:
                sum += curr.mem
                curr = curr.next
            else:
                break
        self.head = curr

# Driver code
# Instantiate the object
ll = LL()

# Create the node with the memory allocated to each node
ll.add("M5",1500)
ll.add("M4",1000)
ll.add("M3",1500)
ll.add("M2",1500)
ll.add("M1",1000)

# Print the head of the linked list once the linked list with all the nodes created
ll.printhead()

# Print the entire linked list with the data and memory allocated associated with it
ll.print()

# Verify if the needed memory can be allocated or split the node with the needed memory accordingly
ll.mem_split(3000)

# Print the entire linked list
ll.print()

# After split verify if we are able to allocate the needed memory from the linked list nodes
ll.allocate_mem(3000)

# Print the new linked list
ll.print()
