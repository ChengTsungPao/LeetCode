class Solution {
public:
    int magicalString(int n) {
        
        if(n <= 3){
            return 1;
        } 
        
        vector<int> magic = {1, 2, 2};
   
        int ans = 1;
        int d;
        int i = 2;
        int j = 2;
        
        while(magic.size() < n){
            d = magic[j] == 2 ? 1 : 2;
            
            if(magic[i] == 1){
                magic.push_back(d);
                ans += (d == 1) ? 1 : 0;
                i += 1;
                j += 1;
            } else {
                magic.push_back(d);
                magic.push_back(d);
                ans += (d == 1) ? 2 : 0;
                i += 1;
                j += 2;
            }
            
        }
        
        ans -= (magic.size() > n && magic[n] == 1) ? 1 : 0;
        
        return ans;
    }
};