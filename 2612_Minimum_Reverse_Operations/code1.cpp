class Solution {
public:
    vector<int> minReverseOperations(int n, int p, vector<int>& banned, int k) {
        /*           
            |        |
        [0, 0, 0, 0, 1, 0, 0, 0], k = 4
         x  x                 x
         
        
        1's pos = 4
        
        set([4, 1, 3, 5, 7, 9])
        
        (1, 4) => 2.5 * 2 = (4 + x) => x = 1 -3
        (2, 5) => 3.5 * 2 = (4 + x) => x = 3 -1
        (3, 6) => 4.5 * 2 = (4 + x) => x = 5 +1
        (4, 7)                      => x = 7 +3
        */
        
        vector<int> ans(n, -1);
        
        queue<tuple<int, int>> q;
        q.push({p, 0});
        vector<bool> visited(n, false);
        visited[p] = true;
        
        for(int pos: banned){
            visited[pos] = true;
        }
        
        while(!q.empty()){
            tuple<int, int> t = q.front(); q.pop();
            int pos = get<0>(t), step = get<1>(t);
            
            ans[pos] = step;
            
            for(int i = 0; i < k; i++){
                int start = pos + i - k + 1, end = pos + i;
                int nextPos = start + end - pos;

                if(start < 0 || end >= n || visited[nextPos]) continue;
                
                q.push({nextPos, step + 1});
                visited[nextPos] = true;
            }
        }
        
        return ans;
    }
};