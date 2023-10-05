class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        int n = s.size();
        int zero = 0, one = 0;
        for(auto ch: s){
            zero += (ch == '0');
        }
        one = n - zero;
        
        if(one == 1){
            return string(n - 1, '0') + "1";
        }
        
        return string(one - 1, '1') + string(zero, '0') + "1";
    }
};