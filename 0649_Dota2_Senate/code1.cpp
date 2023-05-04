class Solution {
public:
    string predictPartyVictory(string senate) {
        int countR = 0, banR = 0;
        int countD = 0, banD = 0;
        
        do {
            countR = 0;
            countD = 0;
            
            for(int i = 0; i < senate.size(); i++){
                char opr = senate[i];
                if(opr == 'R'){
                    if(banR == 0){
                        countR++;
                        banD++;
                    } else {
                        banR--;
                        senate[i] = 'X';
                    }
                } else if (opr == 'D') {
                    if(banD == 0){
                        countD++;
                        banR++;
                    } else {
                        banD--;
                        senate[i] = 'X';
                    }
                }
            }
            
        } while(countR > 0 && countD > 0);
        
        return (countD == 0) ? "Radiant" : "Dire";
    }
};