class MKAverage {
public:
    int m, k;
    long long sum;
    multiset<int> lower, middle, upper;
    queue<int> container;
    
    MKAverage(int m, int k) {
        this -> m = m;
        this -> k = k;
        this -> sum = 0;
    }
    
    void addElement(int num) {
        this -> container.push(num);
        
        if(this -> container.size() > this -> m){
            int val = container.front();
            this -> container.pop();
            
            // remove val
            if(this -> lower.find(val) != this -> lower.end()){
                this -> lower.erase(this -> lower.find(val));
            } else if (this -> middle.find(val) != this -> middle.end()){
                this -> middle.erase(this -> middle.find(val));
                this -> sum -= val;
            } else {
                this -> upper.erase(this -> upper.find(val));
            }
        }

        // add num
        this -> lower.insert(num);
        
        int prev_max_val, next_min_val;

        prev_max_val = (this -> lower.size() > 0) ? *(this -> lower.rbegin()) : 0;
        next_min_val = (this -> middle.size() > 0) ? *(this -> middle.begin()) : pow(10, 5) + 1;            
            
        if (this -> lower.size() > this -> k){
            
            this -> lower.erase(this -> lower.find(prev_max_val));
            this -> middle.insert(prev_max_val);
            
            this -> sum += prev_max_val;
            
        } else if (prev_max_val > next_min_val){
            
            this -> lower.erase(this -> lower.find(prev_max_val));
            this -> lower.insert(next_min_val);
            
            this -> middle.erase(this -> middle.find(next_min_val));
            this -> middle.insert(prev_max_val);
            
            this -> sum += prev_max_val - next_min_val;
        }

        prev_max_val = (this -> middle.size() > 0) ? *(this -> middle.rbegin()) : 0;
        next_min_val = (this -> upper.size() > 0) ? *(this -> upper.begin()) : pow(10, 5) + 1;         
            
        if(this -> middle.size() > this -> m - 2 * this -> k){
            
            this -> middle.erase(this -> middle.find(prev_max_val));
            this -> upper.insert(prev_max_val);
            
            this -> sum -= prev_max_val;
            
        } else if (prev_max_val > next_min_val){
            
            this -> middle.erase(this -> middle.find(prev_max_val));
            this -> middle.insert(next_min_val);
            
            this -> upper.erase(this -> upper.find(next_min_val));
            this -> upper.insert(prev_max_val);
            
            this -> sum += next_min_val - prev_max_val;
        }
    
    }
    
    int calculateMKAverage() {
        return (this -> container.size() >= this -> m) ? (this -> sum / (this -> m - 2 * this -> k)) : -1;
    }
};

/**
 * Your MKAverage object will be instantiated and called as such:
 * MKAverage* obj = new MKAverage(m, k);
 * obj->addElement(num);
 * int param_2 = obj->calculateMKAverage();
 */