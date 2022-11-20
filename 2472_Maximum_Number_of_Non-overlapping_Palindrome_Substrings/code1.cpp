class Solution {
public:
    int maxPalindromes(string s, int k) {
        unordered_map<int, int> memo;
        return recur(0, s, k, memo);
    }
    
    int recur(int i, string s, int k, unordered_map<int, int>& memo){
        if(i + k > s.size()){
            return 0;
        }
        
        if(memo.count(i)){
            return memo[i];
        }
        
        int ans = recur(i + 1, s, k, memo);
        if(i + k <= s.size() && isPalindrome(s.substr(i, k))){
            ans = max(ans, recur(i + k, s, k, memo) + 1);
        }
        if(i + k + 1 <= s.size() && isPalindrome(s.substr(i, k + 1))){
            ans = max(ans, recur(i + k + 1, s, k, memo) + 1);
        }
        
        memo[i] = ans;
        return memo[i];
    }
    
    bool isPalindrome(string str){
        string reverse_str = str;
        reverse(reverse_str.begin(), reverse_str.end());
        return str == reverse_str;
    }
    
};