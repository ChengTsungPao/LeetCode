class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        
        int n = pushed.size();
        
        int idx = 0;
        vector<int> stack;
        for(int num: pushed){
            stack.push_back(num);
            
            while(!stack.empty() && stack.back() == popped[idx]){
                stack.pop_back();
                idx += 1;
            }
                
        }

        return idx == n;
    }
};