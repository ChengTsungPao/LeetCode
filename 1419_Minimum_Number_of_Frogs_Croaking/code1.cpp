class Solution {
public:
    int minNumberOfFrogs(string croakOfFrogs) {
        
        // meeting room
        
        unordered_map<char, char> table = {{'k', 'a'}, {'a', 'o'}, {'o', 'r'}, {'r', 'c'}, {'c', '#'}};
        unordered_map<char, int> countEnd;
        
        int ans = 0, count = 0;
        for(char ch: croakOfFrogs){            
            char preCh = table[ch];

            if(preCh == '#'){
                countEnd[ch] += 1;
                count += 1;
            } else if (countEnd[preCh] > 0) {
                countEnd[preCh] -= 1;
                if(ch == 'k'){
                    count -= 1;
                } else {
                    countEnd[ch] += 1;
                }
            } else {
                return -1;
            }

            ans = (ans < count) ? count : ans;
        }
        
        return (count == 0) ? ans : -1;
    }
};