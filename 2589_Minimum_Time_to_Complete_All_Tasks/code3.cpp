class Solution {
public:
    int findMinimumTime(vector<vector<int>>& tasks) {
        sort(tasks.begin(), tasks.end(), [](vector<int>& a,vector<int>& b){
            return a[1] < b[1];
        });
        
        int ans = 0;
        vector<bool> state(2000 + 1, false);
        
        for(int i = 0; i < tasks.size(); i++){
            int start = tasks[i][0], end = tasks[i][1], duration = tasks[i][2];
            
            for(int t = start; t <= end; t++){
                duration -= state[t];
            }
            
            ans += max(duration, 0);
            
            int t = end;
            while(duration > 0){
                if(!state[t]){
                    state[t] = true;
                    duration--;
                }
                t--;
            }
            
        }
        
        return ans;
    }
};