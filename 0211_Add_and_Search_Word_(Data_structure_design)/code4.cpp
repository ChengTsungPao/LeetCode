struct Node{
    char ch;
    unordered_map<char, Node*> children;
    bool isWord;
    
    Node(char ch){
        ch = ch;
        isWord = false;
    }
};

class WordDictionary {
public:
    Node* root;
    
    WordDictionary() {
        this -> root = new Node('#');
    }
    
    void addWord(string word) {
        Node* node = this -> root;
        for(char ch: word){
            if(node -> children.count(ch) == 0){
                node -> children[ch] = new Node(ch);
            }
            node = node -> children[ch];
        }
        node -> isWord = true;
    }
    
    bool search(string word) {
        return _search(0, this -> root, word);
    }
    
    bool _search(int idx, Node* node, string& word){
        if(idx >= word.size()){
            return node -> isWord;
        }
        char ch = word[idx];
        if(ch == '.'){
            for(auto it = node -> children.begin(); it != node -> children.end(); it++){
                char curCh = it -> first;
                if(_search(idx + 1, node -> children[curCh], word)){
                    return true;
                }
            }
        }
        return (node -> children.count(ch)) ? _search(idx + 1, node -> children[ch], word) : false;
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */