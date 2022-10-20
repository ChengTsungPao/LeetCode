class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        int ans = 0;
        int counti = 0;
        int countj = 0;
        for(int i = 0; i < bank.size(); i++){
            countj = count(bank[i]);
            if(countj > 0){
                ans += counti * countj;
                counti = countj;
            }
        }
        return ans;
    }
    
    int count(string str){
        int c = 0;
        for(auto ch: str){
            c += (ch == '1') ? 1 : 0;
        }
        return c;
    }
};