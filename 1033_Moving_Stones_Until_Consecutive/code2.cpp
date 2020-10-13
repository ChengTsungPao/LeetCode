class Solution {
public:
    vector<int> numMovesStones(int a, int b, int c) {
        vector<int> ans = {0, 0};
        vector<int> data = {a, b, c};
        sort(data.begin(), data.end()); 
        ans[1] = data[1] - data[0] - 1 + data[2] - data[1] - 1;
        if(data[1] - data[0] == 1 and data[2] - data[1] == 1)
            ans[0] = 0;
        else if(data[1] - data[0] > 2 and data[2] - data[1] > 2)
            ans[0] = 2;
        else
            ans[0] = 1;
        return ans;       
    }
};