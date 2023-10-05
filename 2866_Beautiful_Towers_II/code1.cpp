class Solution {
public:
    long long maximumSumOfHeights(vector<int>& maxHeights) {        
        int n = maxHeights.size();
        long long s = 0;
        
        vector<pair<long long, long long>> stack;
        
        vector<long long> suffix(n, -1);
        suffix[n - 1] = maxHeights[n - 1];
        s = maxHeights[n - 1];
        stack.push_back({maxHeights[n - 1], 1});
        for(int i = n - 2; i >= 0; i--){
            int h = maxHeights[i];
            if(h >= stack.back().first){
                
                if(stack.back().first == h){
                    stack.back().second++;
                } else {
                    stack.push_back({h, 1});
                }
                s += h;
            } else {
                long long k = 0, m = 0;
                while(!stack.empty() && stack.back().first >= h){
                    k += stack.back().second;
                    m += (stack.back().first - h) * stack.back().second;
                    stack.pop_back();
                }
                stack.push_back({h, k + 1});
                s = s + h - m;
            }
            
            suffix[i] = s;
        }
        stack.clear();
        
        vector<long long> prefix(n, -1);
        prefix[0] = maxHeights[0];
        s = maxHeights[0];
        stack.push_back({maxHeights[0], 1});
        for(int i = 1; i < n; i++){
            int h = maxHeights[i];
            if(h >= stack.back().first){
                
                if(stack.back().first == h){
                    stack.back().second++;
                } else {
                    stack.push_back({h, 1});
                }
                s += h;
            } else {
                long long k = 0, m = 0;
                while(!stack.empty() && stack.back().first >= h){
                    k += stack.back().second;
                    m += (stack.back().first - h) * stack.back().second;
                    stack.pop_back();
                }
                stack.push_back({h, k + 1});
                s = s + h - m;
            }
            
            prefix[i] = s;
        }
        
        long long ans = 0;
        for(int i = 0; i < n; i++){
            ans = max(ans, prefix[i] + suffix[i] - maxHeights[i]);
        }
        
        return ans;
    }
};