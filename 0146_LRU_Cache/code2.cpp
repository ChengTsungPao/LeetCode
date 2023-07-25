class Node {
public:
    int val, key;
    Node *prev, *next;

    Node() {
        key = 0;
        val = 0;
        next = NULL;
        prev = NULL;
    }

    Node(int key, int val) {
        this -> key = key;
        this -> val = val;
        this -> next = NULL;
        this -> prev = NULL;
    }
};

class DoubleLinkedList {
public:
    int capacity;
    unordered_map<int, Node*> cache;
    Node *dummyHead, *dummyTail;
    
    DoubleLinkedList(int capacity) {
        this -> capacity = capacity;
        dummyHead = new Node();
        dummyTail = new Node();
        dummyHead -> next = dummyTail;
        dummyTail -> prev = dummyHead;
    }
    
    int get(int key){
        int val = -1;
        if(cache.find(key) != cache.end()){
            val = cache[key] -> val;
            move_to_tail(key);
        }
        return val;
    }
    
    void move_to_tail(int key){
        // find
        Node *node = cache[key];
        Node *prev = node -> prev, *next = node -> next;
        prev -> next = next;
        next -> prev = prev;
        
        // move
        Node *temp = dummyTail -> prev;
        dummyTail -> prev = node;
        node -> next = dummyTail;
        
        node -> prev = temp;
        temp -> next = node;
    }
    
    void add(int key, int val){
        if(cache.find(key) != cache.end()){
            cache[key] -> val = val;
            move_to_tail(key);
            return;
        }
        
        Node *node = new Node(key, val);
        cache[key] = node;
        
        // add
        Node *temp = dummyTail -> prev;
        dummyTail -> prev = node;
        node -> next = dummyTail;
        
        node -> prev = temp;
        temp -> next = node;    
        
        if(cache.size() > capacity){
            Node *delNode = dummyHead -> next;
            dummyHead -> next = delNode -> next;
            dummyHead -> next -> prev = dummyHead;
            cache.erase(delNode -> key);
            delNode -> next = NULL;
            delNode -> prev = NULL;
        }
    }
    
};

class LRUCache {
public:
    DoubleLinkedList *doubleLinkedList;
    
    LRUCache(int capacity) {
        doubleLinkedList = new DoubleLinkedList(capacity);
    }
    
    int get(int key) {
        return doubleLinkedList -> get(key);
    }
    
    void put(int key, int value) {
        doubleLinkedList -> add(key, value);
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */