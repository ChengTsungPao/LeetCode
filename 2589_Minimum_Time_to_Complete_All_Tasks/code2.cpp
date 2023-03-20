class Solution {
public:
    int findMinimumTime(vector<vector<int>>& tasks) {
        int ans = 0;
        for(int t = 0; t <= 2000; t++){
            if(check(t, tasks)){
                ans++;
                for(int i = 0; i < tasks.size(); i++){
                    int start = tasks[i][0], end = tasks[i][1], duration = tasks[i][2];
                    if(start <= t && t <= end && duration > 0){
                        tasks[i][2]--;
                    }
                }
            }
        }
        return ans;
    }
    
    bool check(int t, vector<vector<int>>& tasks){
        for(int i = 0; i < tasks.size(); i++){
            int start = tasks[i][0], end = tasks[i][1], duration = tasks[i][2];
            if(end - t + 1 == duration and duration > 0){
                return true;
            }
        }
        return false;
    }
    
};