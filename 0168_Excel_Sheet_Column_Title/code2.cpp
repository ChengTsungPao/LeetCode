class Solution {
public:
    string convertToTitle(int n) {
        
        string ans = "";
        
        while(n > 0){
            ans = ans.insert(0, string(1, 'A' + (n - 1) % 26));
            n = (n - 1) / 26;
        }
        
        return ans;
    }
};