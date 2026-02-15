# By Tinaelis Mumbi
# Linked List - Singly linked list with dynamic size
# O(n) for append/access/search, O(1) for insert/delete with node reference

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    # Add a node at the end
    def append(self, data):
        new_node = Node(data)
        
        # If list is empty
        if not self.head:
            self.head = new_node
            return
        
        # Traverse to the last node
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node
    
    # Add a node at the beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # Delete first occurrence of a value
    def delete(self, key):
        # Empty list
        if not self.head:
            return
        
        # If head node itself holds the key
        if self.head.data == key:
            self.head = self.head.next
            return
        
        # Search for the key
        current = self.head
        while current.next:
            if current.next.data == key:
                current.next = current.next.next
                return
            current = current.next
    
    # Print the list
    def display(self):
        if not self.head:
            print("List is empty")
            return
        
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print(" → ".join(elements))
    
    # Get length of list
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


# ────────────────────────────────────────────────
# Example usage
# ────────────────────────────────────────────────

if __name__ == "__main__":
    ll = LinkedList()
    
    # Adding elements
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.prepend(5)
    ll.append(40)
    
    print("Original list:")
    ll.display()           # 5 → 10 → 20 → 30 → 40
    
    print("\nLength:", ll.length())  # 5
    
    print("\nAfter deleting 20:")
    ll.delete(20)
    ll.display()           # 5 → 10 → 30 → 40
    
    print("\nAfter deleting 5 (head):")
    ll.delete(5)
    ll.display()           # 10 → 30 → 40
    
    print("\nAfter deleting non-existing value (99):")
    ll.delete(99)          # no change
    ll.display()
