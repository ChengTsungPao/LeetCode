class Solution {
public:
    int minStoneSum(vector<int>& piles, int k) {
        
        int pile = 0;
        priority_queue<int> pq(piles.begin(), piles.end());
        
        for(int i = 0; i < k; i++){
            pile = pq.top(); pq.pop();
            pq.push(pile / 2 + pile % 2);
        }
        
        int sum = 0;
        while (!pq.empty()) {
            sum = sum + pq.top();
            pq.pop();
        }
        
        return sum;
    }
};