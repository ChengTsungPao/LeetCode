/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    unordered_map<int, Node*> memo;
    
    Node* cloneGraph(Node* node) {
        if(node == nullptr){
            return nullptr;
        }
        
        int val = node -> val;
        if(memo.find(val) != memo.end()){
            return memo[val];
        }
        
        // copy current node
        Node* copyNode = new Node(val);
        memo[val] = copyNode;
        
        // copy neighbor node
        for(Node* nextNode: node -> neighbors){
            copyNode -> neighbors.push_back(cloneGraph(nextNode));
        }
        
        return copyNode;
    }
};