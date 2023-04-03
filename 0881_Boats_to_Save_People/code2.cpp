class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        
        int n = people.size();
        sort(people.begin(), people.end());
        
        int ans = 0;
        int i = 0, j = n - 1;
        while(i <= j){
            if(i != j && people[i] + people[j] <= limit){
                i += 1;
                j -= 1;
            } else {
                j -= 1;
            }
            ans += 1;
        }
        
        return ans;
    }
};