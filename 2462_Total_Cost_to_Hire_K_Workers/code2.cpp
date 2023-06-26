class Solution {
public:
    long long totalCost(vector<int>& costs, int k, int candidates) {
        int n = costs.size();
        
        priority_queue<int> pq_l, pq_r;
        
        int i = 0, j = n - 1;
        for(;i <= candidates; i++){
            if(pq_l.size() < candidates){
                pq_l.push((i <= j) ? -costs[i] : INT_MIN);
            } else {
                break;
            }
        }
        
        for(;j >= n - candidates; j--){
            if(pq_r.size() < candidates){
                pq_r.push((i <= j) ? -costs[j] : INT_MIN);
            } else {
                break;
            }
        }

        long long ans = 0;
        while(k > 0){
            int val_l = pq_l.top(), val_r = pq_r.top();
            if(val_l == INT_MIN && val_r == INT_MIN){
                break;
            }

            if(val_l >= val_r){
                ans -= val_l;
                pq_l.pop();
                pq_l.push((i <= j) ? -costs[i] : INT_MIN);
                i++;
            } else {
                ans -= val_r;
                pq_r.pop();
                pq_r.push((i <= j) ? -costs[j] : INT_MIN);
                j--;
            }
            k--;
        }
        
        return ans;
    }
};