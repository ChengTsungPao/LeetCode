class Solution {
public:
    string convertToTitle(int n) {
        
        string ans = "";
        string table[26] = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"};
        
        while(n > 0){
            ans = ans.insert(0, table[(n - 1) % 26]);
            n = (n - 1) / 26;
        }
        
        return ans;
    }
};