struct hash_tuple {
    template <class T1, class T2, class T3>
    size_t operator()(const tuple<T1, T2, T3>& x)
        const { return get<0>(x) ^ get<1>(x) ^ get<2>(x); }
};

class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        unordered_map<tuple<int, int, bool>, int, hash_tuple> memo;
        return recur(0, k, false, prices, memo);
    }
    
    int recur(int i, int k, bool isbuy, vector<int>& prices, unordered_map<tuple<int, int, bool>, int, hash_tuple>& memo){
        tuple<int, int, bool> key = make_tuple(i, k, isbuy);
        if(memo.count(key)){
            return memo[key];
        }
        
        if(i >= prices.size() || k == 0){
            return 0;
        }
        
        int ans = 0;
        if(isbuy){
             ans = max(recur(i + 1, k, true, prices, memo), recur(i + 1, k - 1, false, prices, memo) + prices[i]);
        } else {
             ans = max(recur(i + 1, k, false, prices, memo), recur(i + 1, k, true, prices, memo) - prices[i]);
        }
        
        memo[key] = ans;
        return ans;
    }
};