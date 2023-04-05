class Solution {
public:
    int partitionString(string s) {
        
        int n = s.size();
        
        int ans = 1;
        int bitmask = 0;
        for(char ch : s){
            if(bitmask & (1 << (ch - 'a'))){
                ans += 1;
                bitmask = 0;
            }
            bitmask |= 1 << (ch - 'a');
        }
        
        return ans;
    }
};