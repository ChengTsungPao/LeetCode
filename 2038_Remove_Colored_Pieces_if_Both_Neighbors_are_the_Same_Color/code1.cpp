class Solution {
public:
    bool winnerOfGame(string colors) {
        int n = colors.size();
        int A = 0, B = 0;
        for(int i = 1; i < n - 1; i++){
            A += colors[i] == 'A' && colors[i + 1] == 'A' && colors[i - 1] == 'A';
            B += colors[i] == 'B' && colors[i + 1] == 'B' && colors[i - 1] == 'B';
        }
        return A > B;
    }
};