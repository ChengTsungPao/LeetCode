class Solution {
public:
    int MOD = pow(10, 9) + 7;
    
    int countRoutes(vector<int>& locations, int start, int finish, int fuel) {
        int n = locations.size();
        vector<vector<int>> memo(n, vector<int>(fuel + 1, -1));
        return recur(start, fuel, locations, finish, memo);
    }
    
    int recur(int loc, int fuel, vector<int>& locations, int finish, vector<vector<int>>& memo){
        int n = locations.size();
        
        if(fuel < 0){
            return 0;
        } 
        
        if(memo[loc][fuel] != -1){
            return memo[loc][fuel];
        }
        
        int ans = (loc == finish), fs = locations[loc];
        for(int next_loc = 0; next_loc < n; next_loc++){
            if(loc != next_loc){
                int fe = locations[next_loc];
                ans += recur(next_loc, fuel - abs(fe - fs), locations, finish, memo);
                ans %= MOD;
            }
        }
        
        memo[loc][fuel] = ans;
        return ans;
    }
};