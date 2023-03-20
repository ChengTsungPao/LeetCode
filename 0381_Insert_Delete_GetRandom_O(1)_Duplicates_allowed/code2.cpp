class RandomizedCollection {
public:
    unordered_map<int, multiset<int>> valIndex;
    vector<int> vals;
    
    RandomizedCollection() {
        
    }
    
    bool insert(int val) {
        bool isExist = valIndex.find(val) != valIndex.end();
        int n = vals.size();
        valIndex[val].insert(n);
        vals.push_back(val);
        return !isExist;
    }
    
    bool remove(int val) {
        auto it1 = valIndex.find(val);
        bool isExist = it1 != valIndex.end();
        if(isExist){
            int n = vals.size();
            
            // remove val from valIndex
            auto it2 = it1 -> second.begin();
            int index = *it2;
            it1 -> second.erase(it2);
            if(it1 -> second.size() == 0) {
                valIndex.erase(it1);
            }
            
            // remove val from vals
            int lastVal = vals[n - 1];
            swap(vals[index], vals[n - 1]);
            vals.pop_back();
            
            // update lastVal index
            if(index != n - 1){
                auto it3 = valIndex.find(lastVal);
                it3 -> second.erase(n - 1);
                it3 -> second.insert(index);
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