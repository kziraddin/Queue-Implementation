# --------------------- QUEUE IMPLEMENTATION ---------------------

# --------------------- using DYNAMIC ARRAYS ---------------------

class dynamicArrayQueue:
    def __init__(self):
        self.queue = []


    def isEmpty(self):
        if len(self.queue) == 0:
            return None


    def enqueue(self, val):
        self.queue.append(val)


    def dequeue(self):
        if self.isEmpty():
            return None
        return self.queue.pop(0)
    

    def peek(self):
        if self.isEmpty():
            return None
        return self.queue[0]
    
    
# --------------------- using DEQUE() ---------------------

from collections import deque

class doubleEndedQueue:
    def __init__(self):
        self.queue = deque()


    def isEmpty(self):
        return not self.queue
    
    # ADD TO END
    def enqueue(self, val):
        self.queue.append(val)

    # REMOVE HEAD
    def dequeue(self):
        if self.isEmpty():
            return None
        return self.queue.popleft()
    
    # GIVEs 1st VALUE in the list
    def peek(self):
        if self.isEmpty():
            return None
        return self.queue[0]
    

    def size(self):
        return len(self.queue)
    

# --------------------- using SINGLY LINKED LIST ---------------------
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class linkedListQueue:
    
    def __init__(self):
        self.head = None
        self.tail = None
    

    def isEmpty(self):
        return not self.head # will need this func() once we come to pop()
    

    # ADD TO END
    def enqueue(self,val):
        newNode = Node(val)

        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode


    # REMOVE 1ST VALUE IN THE QUEUE
    def dequeue(self):
        if self.isEmpty():
            return None
        
        removed = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None

        return removed.val
    
    # RETURN 1ST VALUE IN THE QUEUE
    def peek(self):
        if self.isEmpty():
            print("\nQUEUE is Empty.")
            return None
        else:
            print(f"The PEEK value in QUEUE is: {self.head.val}.")
            return self.head.val
    

    def display(self):
        values = []

        curr = self.head
        while curr:
            values.append(curr.val)
            curr = curr.next
        print("QUEUE: ", values)



# --------------------- MAIN PROGRAM ---------------------

if __name__ == "__main__":

    queue = linkedListQueue()

    while True:
        print("\nPress q to QUIT.")
        print("\nPress 1 to ADD value to the queue.")
        print("\nPress 2 to POP value from the queue.")
        print("\nPress 3 to print PEEK value from queue.")
        #print("\nCHOOSE AN OPTION.")

        choice = input("\n>>> CHOOSE AN OPTION <<<  >>  ")
        print("\n")

        # ADD
        if choice == "1":
            val = int(input("\nEnter value to add. >>  "))
            queue.enqueue(val)
            print("\n")
            queue.display()

        # REMOVE
        elif choice == "2":
            queue.dequeue()
            print("\n")
            queue.display()

        # PEEK
        elif choice == "3":
            queue.display()
            print("\n")
            queue.peek()

        elif choice.lower() == "q":
            print("\nExiting...")
            break
    
        else:
            print("\n")
            print("Invalid choice. Try again.")