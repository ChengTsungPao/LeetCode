class Solution {
public:
    int bestClosingTime(string customers) {
        int n = customers.size();
        
        int R_Y = 0, R_N = 0;
        for(auto c: customers){
            if(c == 'Y'){
                R_Y += 1;
            } else {
                R_N += 1;
            }
        }
        
        int L_Y = 0, L_N = 0;
        int ans = 0, penalty = L_N + R_Y;
        for(int hour = 0; hour < n; hour++){
            int c = customers[hour];
            if(c == 'Y'){
                L_Y += 1;
                R_Y -= 1;
            } else {
                L_N += 1;
                R_N -= 1;
            }
            if(L_N + R_Y < penalty){
                ans = hour + 1;
                penalty = L_N + R_Y;
            }
        }
        
        return ans;
    }
};