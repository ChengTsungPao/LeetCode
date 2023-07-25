class Solution {
public:
    int longestValidSubstring(string word, vector<string>& forbidden) {
        int n = word.size();
        
        unordered_set<string> forbidden_set(forbidden.begin(), forbidden.end());
        unordered_map<int, vector<int>> pair;
        multiset<int> orderEnd;
        orderEnd.insert(n);
        
        for(int i = 0; i < n; i++){
            string cur_s = "";
            for(int j = i; j < min(i + 10, n); j++){
                cur_s += word[j];
                if(forbidden_set.find(cur_s) != forbidden_set.end()){
                    pair[i].push_back(j);
                    orderEnd.insert(j);
                }
            }
        }
        
        int ans = 0;
        for(int i = 0; i < n; i++){
            for(int j: pair[i - 1]){
                orderEnd.erase(orderEnd.find(j));
            }
            int minEnd = *orderEnd.begin();
            ans = max(ans, minEnd - i);
        }
        
        return ans;
    }
};