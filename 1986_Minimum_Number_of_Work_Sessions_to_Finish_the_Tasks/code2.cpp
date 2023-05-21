class Solution {
public:
    int ans = INT_MAX;
    
    int minSessions(vector<int>& tasks, int sessionTime) {
        vector<int> buckets;
        recur(0, buckets, tasks, sessionTime);
        return ans;
    }
    
    void recur(int idx, vector<int>& buckets, vector<int>& tasks, int sessionTime){
        
        // pruning
        if(buckets.size() >= ans){
            return;
        }
        
        // stop condition
        if(idx >= tasks.size()){
            ans = buckets.size();
            return;
        }
        
        int time = tasks[idx];
        
        // choose one bucket in buckets
        for(int i = 0; i < buckets.size(); i++){
            if(time + buckets[i] <= sessionTime){
                buckets[i] += time;
                recur(idx + 1, buckets, tasks, sessionTime);
                buckets[i] -= time;
            }
        }
        
        // add one bucket in buckets
        buckets.push_back(time);
        recur(idx + 1, buckets, tasks, sessionTime);
        buckets.pop_back();
    }
};