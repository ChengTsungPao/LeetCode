class RandomizedCollection {
public:
    unordered_map<int, vector<int>> valIndex;
    unordered_map<int, unordered_map<int, int>> valIndexToIndex;
    vector<int> vals;
    
    RandomizedCollection() {
        
    }
    
    bool insert(int val) {
        bool isExist = valIndex.find(val) != valIndex.end();
        int val_len = vals.size();
        int valIndex_len = valIndex[val].size();
        valIndex[val].push_back(val_len);
        valIndexToIndex[val][val_len] = valIndex_len;
        vals.push_back(val);
        return !isExist;
    }
    
    bool remove(int val) {
        auto it = valIndex.find(val);
        bool isExist = it != valIndex.end();
        if(isExist){
            // vals => remove val
            int i = it -> second.back(); // choose last elment remove
            int val_len = vals.size();
            int lastVal = vals[val_len - 1];
            swap(vals[i], vals[val_len - 1]);
            vals.pop_back();
            
            // valIndex & valIndexToIndex => edit lastVal
            int j = valIndexToIndex[lastVal][val_len - 1];
            valIndex[lastVal][j] = i;
            valIndexToIndex[lastVal][i] = j;
            valIndexToIndex[lastVal].erase(val_len - 1);
            
            // valIndex & valIndexToIndex => remove val
            it -> second.pop_back();
            valIndexToIndex[val].erase(i);
            if(it -> second.size() == 0){
                valIndex.erase(val);
                valIndexToIndex.erase(val);
            }
        }
        return isExist;   
    }
    
    int getRandom() {
        return vals[(int)(random() % vals.size())];
    }
};

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection* obj = new RandomizedCollection();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */