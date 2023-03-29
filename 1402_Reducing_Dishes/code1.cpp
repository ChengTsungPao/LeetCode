class Solution {
public:
    int maxSatisfaction(vector<int>& satisfaction) {
        
        // split postive & negative number
        vector<int> pos, neg;
        for(int num: satisfaction){
            if(num > 0){
                pos.push_back(num);
            } else {
                neg.push_back(-num);
            }
        }
        
        // sort postive & negative vector
        sort(pos.begin(), pos.end());
        sort(neg.begin(), neg.end());
        
        // get all postive answer
        int ans = 0, sum = 0;
        for(int i = 0; i < pos.size(); i++){
            int num = pos[i];
            sum += num;
            ans += (i + 1) * num;
        }
        
        // prefix sum
        for(int num: neg){
            num = -num;
            int cur_ans = ans + sum + num;
            if(cur_ans >= ans){
                ans = cur_ans;
            } else {
                break;
            }
            sum += num;
        }
        
        return ans;
    }
};