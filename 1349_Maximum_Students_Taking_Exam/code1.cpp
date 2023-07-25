class Solution {
public:
    int memo[8 + 1][256 + 1];
    int m, n;
    
    int maxStudents(vector<vector<char>>& seats) {
        m = seats.size();
        n = seats[0].size();
        
        vector<int> seat_mask(m, -1); // every row
        
        for(int i = 0; i < m; i++){
            int bitmask = 0;
            for(int j = 0; j < n; j++){
                if(seats[i][j] == '.') bitmask |= (1 << j);
            }
            seat_mask[i] = bitmask;
        }
        
        memset(memo, -1, sizeof(memo));
        return recur(m - 1, seat_mask[m - 1], seat_mask);
    }  
    
    int recur(int idx, int cur_state, vector<int>& seat_mask){
        if(idx < 0){
            return 0;
        }
        
        
        if(memo[idx][cur_state] != -1){
            return memo[idx][cur_state];
        }
        
        int nxt_state = (idx > 0) ? seat_mask[idx - 1] : 0;
        
        vector<vector<int>> states;
        subset(0, cur_state, nxt_state, 0, states);
        
        int ans = 0;
        for(auto v: states){
            int state = v[0], num_of_seat = v[1];            
            ans = max(ans, num_of_seat + recur(idx - 1, state, seat_mask));
        }
        
        return memo[idx][cur_state] = ans;        
    }

    void subset(int idx, int cur_state, int nxt_state, int num_of_seat, vector<vector<int>>& states){
        if(idx >= n){
            states.push_back({nxt_state, num_of_seat});
            return;
        }
        
        subset(idx + 1, cur_state, nxt_state, num_of_seat, states);
        if((cur_state & (1 << idx)) > 0){
            subset(idx + 2, cur_state, setZero(idx + 1, setZero(idx - 1, nxt_state)), num_of_seat + 1, states);
        }
    }
    
    int setZero(int i, int bitmask){
        if(i < 0 || i >= n || (bitmask & (1 << i)) == 0){
            return bitmask;
        }
        return bitmask - (1 << i);
    }
    
};