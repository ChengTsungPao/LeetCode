class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> stack;
        
        for(int asteroid: asteroids){
            bool isExplode = false;
            while(!stack.empty() && stack.back() > 0 && asteroid < 0 && stack.back() <= -asteroid){
                if(!stack.empty() && stack.back() == -asteroid){
                    isExplode = true;
                    stack.pop_back();
                    break;
                } 
                stack.pop_back();
            }
            
            if(!stack.empty() && stack.back() > 0 && asteroid < 0 && stack.back() > -asteroid){
                isExplode = true;
            }
            
            if(!isExplode){
                stack.push_back(asteroid);
            }
        }
        
        return stack;
    }
};