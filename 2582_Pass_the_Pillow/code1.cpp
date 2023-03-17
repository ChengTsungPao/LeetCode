class Solution {
public:
    int passThePillow(int n, int time) {
        
        // 1 -> 2 -> 3 -> 4 -> 3 -> 2 -> 1
        
        int oneRound = 2 * n - 2;
        time %= oneRound;
        
        return (time <= n - 1) ? time + 1 : n - (time - (n - 1));
    }
};