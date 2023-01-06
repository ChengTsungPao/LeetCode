class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        
        vector<int> neg_costs;
        for(int cost: costs){
            neg_costs.push_back(-cost);
        }
        
        priority_queue<int> pq(std::less<int>(), neg_costs);
        
        int ans = 0;
        while(!pq.empty()){            
            coins += pq.top();
            if(coins < 0) break;
            pq.pop();
            ans += 1;
        }
        
        return ans;     
    }
    
};