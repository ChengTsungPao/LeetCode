class Solution {
public:
    int minInsertions(string s) {
        
        vector<char> stack;
        int ans = 0;
        int count = 0;
        
        for(auto& ch: s){
            if(ch == '('){
                if(count == 1){
                    if(stack.size() > 0){
                        ans += 1;
                        stack.pop_back();
                    } else {
                        ans += 2;
                    }
                    count = 0;
                }
                stack.push_back(ch);
            } else if (count + 1 == 2){
                if(stack.size() > 0){
                    stack.pop_back();
                } else {
                    ans += 1;
                }
                count = 0;

            } else{
                count++;
            } 
        }   
        
        if(count > 0 && stack.size() == 0){
            ans += (count + count % 2) / 2 + count % 2;
        } else {
            ans += stack.size() * 2 - count;
        }
        
        return ans;
    }
    
};