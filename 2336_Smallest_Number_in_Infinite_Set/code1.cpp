class SmallestInfiniteSet {
public:
    priority_queue<int, vector<int>, greater<int>> pq;
    unordered_set<int> cache;
    
    SmallestInfiniteSet() {
        pq.push(1);
    }
    
    int popSmallest() {
        int minVal = pq.top(); pq.pop();
        cache.insert(minVal);
        if(pq.empty()) pq.push(minVal + 1);
        return minVal;
    }
    
    void addBack(int num) {
        if(cache.find(num) != cache.end()){
            pq.push(num);
            cache.erase(num);
        }
    }
};

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet* obj = new SmallestInfiniteSet();
 * int param_1 = obj->popSmallest();
 * obj->addBack(num);
 */