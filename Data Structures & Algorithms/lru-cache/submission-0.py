class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
    

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        # design: map, key = key, val = Node object with key and value
        self.cache = {} # map, initially empty
        
        # left = LRU, right = MRU
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    # remove the node and update adjacent nodes
    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    # insert a node at the start, updating right and adjacent
    def insert(self, node):
        node.next = self.right
        node.prev = self.right.prev
        self.right.prev.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    # if new, put in at most recent and add to map
    # if not new, remove from wherever and put at most recent and update map
    # if exceed the capacity, remove the left 
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache.keys()) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
    



