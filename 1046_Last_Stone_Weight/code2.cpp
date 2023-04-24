class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        
        priority_queue<int> pq(stones.begin(), stones.end());
        
        int max1, max2;
        while(pq.size() > 1){
            max1 = pq.top(); pq.pop();
            max2 = pq.top(); pq.pop();
            if(pq.empty() || max1 != max2) pq.push(max1 - max2);
        }
        
        return pq.top();
    }
};