class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev= self.head
        

    def get(self, key: int) -> int:
        if key in self.dic:
            n = self.dic[key]
            self.remove(n)
            self.insert(n)
            return n.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.remove(self.dic[key])
            
        n=Node(key, value)
        self.insert(n)
        self.dic[key]=n
        if len(self.dic)>self.capacity:
            n = self.head.next
            self.remove(n)
            del self.dic[n.key]
            
    def remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        
    def insert(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
        
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)