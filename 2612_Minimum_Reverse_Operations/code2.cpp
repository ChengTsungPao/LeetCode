class Solution {
public:
    vector<int> minReverseOperations(int n, int p, vector<int>& banned, int k) {
        
        vector<int> ans(n, -1);
        ans[p] = 0;
        
        set<int> s[2];
        unordered_set<int> bans(banned.begin(), banned.end());
        for(int pos = 0; pos < n; pos++){
            if(bans.find(pos) == bans.end()){
                s[pos % 2].insert(pos);
            }
        }
        
        queue<tuple<int, int>> q;
        s[p % 2].erase(p);
        q.push({p, 0});     

        while(!q.empty()){
            tuple<int, int> t = q.front(); q.pop();
            int pos = get<0>(t), step = get<1>(t);
            
            bool isOdd = (k % 2) ? pos % 2 : 1 - pos % 2;
            
            // get range of nextPos
            int startL = max(pos - k + 1, 0); 
            int endL = startL + k - 1;
            int left = startL + endL - pos;
            
            int endR = min(pos + k - 1, n - 1);
            int startR = endR - k + 1;
            int right = startR + endR - pos;
            
            auto itStart = s[isOdd].lower_bound(left);
            auto itEnd = s[isOdd].upper_bound(right);
            
            for(auto it = itStart; it != itEnd; it++){
                int nextPos = *it;
                ans[nextPos] = step + 1;
                q.push({nextPos, step + 1});
            }
            
            s[isOdd].erase(itStart, itEnd);
        }
        
        return ans;
    }
};