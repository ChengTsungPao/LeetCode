class Solution {
public:
    string predictPartyVictory(string senate) {
        int n = senate.size();
        queue<int> rQue, dQue;
        
        for(int i = 0; i < n; i++){
            char opr = senate[i];
            if(opr == 'R'){
                rQue.push(i);
            } else {
                dQue.push(i);
            }
        }
        
        while(!rQue.empty() && !dQue.empty()){
            int rIdx = rQue.front(); rQue.pop();
            int dIdx = dQue.front(); dQue.pop();
            
            if(rIdx < dIdx){
                rQue.push(rIdx + n);
            } else {
                dQue.push(dIdx + n);
            }
            
        }
        
        return (!rQue.empty()) ? "Radiant" : "Dire";
    }
};