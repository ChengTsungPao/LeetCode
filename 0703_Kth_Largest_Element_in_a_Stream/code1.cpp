class KthLargest {
public:
    int k;
    multiset<int> container;
    
    KthLargest(int k, vector<int>& nums) {
        this -> k = k;
        for(int num: nums){
            add(num);
        }
    }
    
    int add(int val) {
        container.insert(val);
        if(container.size() > k){
            container.erase(container.begin());
        }
        return *container.begin();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */