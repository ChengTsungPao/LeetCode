class Solution {
public:
    int minOperations(vector<int>& nums, int target) {
        int n = nums.size();
        vector<int> count(32, 0);
        for(int num: nums){
            int i = (int)log2(num);
            count[i]++;
        }
        
        int ans = 0;
        int m = (int)log2(target);
        for(int i = 0; i <= m; i++){
            // add from small num
            if(count[i] > 0 && ((target >> i) & 1) == 1){
                count[i]--;
                target -= (1 << i);
            // div from big num
            } else if (((target >> i) & 1) == 1) {
                bool isFind = false;
                for(int opr = 0; i + opr < 32; opr++){
                    if(count[i + opr] > 0){
                        count[i + opr]--;
                        for(int j = opr - 1; j >= 0; j--){
                            count[i + j]++;
                        }
                        target -= 1 << i;
                        ans += opr;
                        isFind = true;
                        break;
                    }
                }
                if(!isFind){
                    return -1;
                }
            }
            
            if(count[i] >= 2){
                int nextC = count[i] / 2;
                count[i] %= 2;
                count[i + 1] += nextC;
            }
        }
        
        return ans;
    }
};