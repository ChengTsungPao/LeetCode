class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        
        unordered_set<string> deadends_set(deadends.begin(), deadends.end());
        if(deadends_set.count("0000")){
            return -1;
        }
        
        unordered_set<string> cache = {"0000"};
        queue<tuple<string, int>> que;
        que.push(make_tuple("0000", 0));

        while(que.size() > 0){
            tuple<string, int> curNode = que.front(); que.pop();
            
            string curLock = get<0>(curNode);
            int curStep = get<1>(curNode);
            
            if(curLock == target){
                return curStep;
            }
            
            for(int i = 0; i < 4; i++){
                string addDigit = (curLock[i] != '9') ? to_string(curLock[i] + 1 - '0'): "0";
                string minusDigit = (curLock[i] != '0') ? to_string(curLock[i] - 1 - '0'): "9";
                
                string nextLock;
                nextLock = curLock.substr(0, i) + addDigit + curLock.substr(i + 1);
                if(!deadends_set.count(nextLock) && !cache.count(nextLock)){
                    que.push(make_tuple(nextLock, curStep + 1));
                    cache.insert(nextLock);
                    
                }
                
                nextLock = curLock.substr(0, i) + minusDigit + curLock.substr(i + 1);
                if(!deadends_set.count(nextLock) && !cache.count(nextLock)){
                    que.push(make_tuple(nextLock, curStep + 1));
                    cache.insert(nextLock);
                }                
                
            }
        }
        
        return -1;
    }
};