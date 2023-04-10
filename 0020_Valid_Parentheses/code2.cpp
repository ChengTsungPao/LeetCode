class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;
        for(char ch: s){
            if(!stack.empty() && isPair(stack.back(), ch)){
                stack.pop_back();
            } else {
                stack.push_back(ch);
            }
        }
        return stack.empty();
    }
    
    bool isPair(char ch1, char ch2) {
        return (ch1 == '(' && ch2 == ')') || (ch1 == '[' && ch2 == ']') || (ch1 == '{' && ch2 == '}');
    }
    
};