class DynamicArray:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
    
    def append(self, x):
        if self.size == self.capacity:
            new_capacity = self.capacity * 2
            new_data = [None] * new_capacity
            for i in range(self.size):
                new_data[i] = self.data[i]
            self.data = new_data
            self.capacity = new_capacity
        self.data[self.size] = x
        self.size += 1
    
    def pop(self):
        if self.size == 0:
            raise IndexError("Cannot pop from empty array")
        value = self.data[self.size - 1]
        self.size -= 1
        self.data[self.size] = None
        return value
    
    def __str__(self):
        return str([self.data[i] for i in range(self.size)])


# Required test case
da = DynamicArray(2)
print(f"Initial: capacity={da.capacity}, size={da.size}, array={da}")

for i in range(12):  # 10+ appends
    da.append(i)
    print(f"After append {i}: capacity={da.capacity}, size={da.size}, array={da}")

print("\nPerforming 3 pops:")
for _ in range(3):
    popped = da.pop()
    print(f"After pop: capacity={da.capacity}, size={da.size}, array={da}, popped={popped}")



### Task 2

## Part A

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def delete_by_value(self, x):
        if not self.head:
            print(f"{x} not found in empty list")
            return False
        if self.head.data == x:
            self.head = self.head.next
            return True
        current = self.head
        while current.next:
            if current.next.data == x:
                current.next = current.next.next
                return True
            current = current.next
        print(f"{x} not found")
        return False
    
    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(f"List: {elements}")


# REQUIRED TEST CASE
sll = SinglyLinkedList()

print("\n1. Initial empty list:")
sll.traverse()

print("\n2. Insert 3 at beginning:")
sll.insert_at_beginning(3)
sll.traverse()

print("\n3. Insert 3 at end:")
sll.insert_at_end(3)
sll.traverse()

print("\n4. Delete one 3 by value:")
sll.delete_by_value(3)
sll.traverse()

##  Part B

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_after_target(self, target, x):
        current = self.head
        while current:
            if current.data == target:
                new_node = DoublyNode(x)
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                else:
                    self.tail = new_node
                current.next = new_node
                return True
            current = current.next
        print(f"Target {target} not found")
        return False
    
    def delete_at_position(self, pos):  # 0-based
        if pos < 0:
            print("Invalid position")
            return False
        current = self.head
        i = 0
        while current and i < pos:
            current = current.next
            i += 1
        if not current:
            print("Position out of range")
            return False
        
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next
        
        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev
        return True
    
    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(f"Doubly List: {elements}")

# REQUIRED TEST CASE
dll = DoublyLinkedList()

# Build initial list [10, 20, 30]
dll.head = DoublyNode(10)
dll.head.next = DoublyNode(20)
dll.head.next.prev = dll.head
dll.head.next.next = DoublyNode(30)
dll.head.next.next.prev = dll.head.next
dll.tail = dll.head.next.next

print("\n1. Initial list:")
dll.traverse()

print("\n2. Insert 25 after target 20:")
dll.insert_after_target(20, 25)
dll.traverse()

print("\n3. Delete at position 1 (0-based):")
dll.delete_at_position(1)
dll.traverse()

print("\n4. Delete at last position (2):")
dll.delete_at_position(2)
dll.traverse()


### Task 3

## Part A

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None  # SinglyLinkedList head
    
    def push(self, x):
        """O(1) - insert at head (LIFO top)"""
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        """O(1) - remove from head"""
        if self.head is None:
            raise IndexError("Stack is empty - underflow")
        top_value = self.head.data
        self.head = self.head.next
        return top_value
    
    def peek(self):
        """O(1) - view head without remove"""
        if self.head is None:
            raise IndexError("Stack is empty")
        return self.head.data
    
    def is_empty(self):
        return self.head is None
    
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def __str__(self):
        if self.is_empty():
            return "Stack: []"
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return "Stack: [" + ', '.join(elements) + "] (top to bottom)"
    

# Test implementation
s = Stack()

print("1. Initial:", s)

s.push(10)
print("2. push(10):", s)

s.push(20)
s.push(30)
print("3. push(20), push(30):", s)
print("Size:", s.size())
print("Peek:", s.peek())

print("4. pop():", s.pop(), "->", s)
print("5. pop():", s.pop(), "->", s)
print("Peek:", s.peek())


## Part B

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None  # Front
        self.tail = None  # Rear
    
    def enqueue(self, x):
        """O(1) - add to tail"""
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def dequeue(self):
        """O(1) - remove from head"""
        if not self.head:
            raise IndexError("Queue empty - underflow")
        value = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None  # Empty now
        return value
    
    def front(self):
        """O(1) - peek head"""
        if not self.head:
            raise IndexError("Queue empty")
        return self.head.data
    
    def is_empty(self):
        return self.head is None
    
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def __str__(self):
        if self.is_empty():
            return "Queue: [] (front to rear)"
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return "Queue: [" + ', '.join(elements) + "] (front to rear)"
    


# Required Case
q = Queue()
print("1. Initial:", q)

q.enqueue(10)
print("2. enqueue(10):", q)

q.enqueue(20)
q.enqueue(30)
print("3. enqueue(20,30):", q)
print("Size:", q.size())
print("Front:", q.front())

print("4. dequeue():", q.dequeue(), "->", q)
print("5. dequeue():", q.dequeue(), "->", q)
print("Front:", q.front() if not q.is_empty() else "Empty")


### Task 4

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        if not self.head:
            return None
        value = self.head.data
        self.head = self.head.next
        return value
    
    def peek(self):
        if not self.head:
            return None
        return self.head.data
    
    def is_empty(self):
        return self.head is None

def is_balanced(expr):
    stack = Stack()
    matching = {')': '(', '}': '{', ']': '['}
    
    for char in expr:
        if char in '({[':  
            stack.push(char)
        elif char in ')}]':  
            if stack.is_empty() or stack.pop() != matching[char]:
                return False
    
    return stack.is_empty()  


# Required Case
test_cases = ["([])", "([)]", "(((", ""]
for expr in test_cases:
    result = "Balanced" if is_balanced(expr) else "Not balanced"
    print(f'"{expr}" → {result}')