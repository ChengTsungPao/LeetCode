class Solution {
public:
    string removeStars(string s) {
        string stack;
        for(char ch: s) {
            if(ch == '*'){
                stack.pop_back();
            } else {
                stack.push_back(ch);
            }
        }
        return stack;
    }
};