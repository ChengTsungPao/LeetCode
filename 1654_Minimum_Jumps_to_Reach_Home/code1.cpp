class Solution {
public:
    int minimumJumps(vector<int>& forbidden, int a, int b, int x) {        
        unordered_set<int> forbidden_set(forbidden.begin(), forbidden.end());
        
        int maxBan = *max_element(forbidden.begin(), forbidden.end());
        int boundary = max(maxBan, x) + ((a > b) ? b : a + b);
        vector<vector<int>> isVisited(boundary + 1, vector<int>(2, -1));
        
        queue<tuple<int, int, bool>> q;
        q.push({0, 0, false});
        isVisited[0][false] = true;
        
        while(!q.empty()){
            tuple<int, int, bool> t = q.front(); q.pop();
            int pos = get<0>(t), step = get<1>(t);
            bool preBack = get<2>(t);
            
            if(pos == x){
                return step;
            }
            
            if(pos + a <= boundary && isVisited[pos + a][false] < 0 && forbidden_set.find(pos + a) == forbidden_set.end()){
                q.push({pos + a, step + 1, false});
                isVisited[pos + a][false] = true;
            }
            if(!preBack && pos - b >= 0 && isVisited[pos - b][true] < 0 && forbidden_set.find(pos - b) == forbidden_set.end()){
                q.push({pos - b, step + 1, true});
                isVisited[pos - b][true] = true;
            }
        }
        
        return -1;
    }
};