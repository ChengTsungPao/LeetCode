class Solution {
public:
    int findMinimumTime(vector<vector<int>>& tasks) {
        /*              
        [[2,3,1],[4,5,1],[1,5,2]]
          3       5       4
          
          1, 2, 3, 4, 5
             0  0
                ^
                   1  1
                      ^
          2           2
                   ^
          
          timeToTask = {3: {0: 1s}, 4: {2: 2s}, 5: (1, 1s)}  {startTime: {task: duration}}
          taskToTime = {0: 3, 1: 5, 2: 4} {task: startTime}
          loop tasks
          
        */
        
        unordered_map<int, unordered_map<int, int>> timeToTask;
        unordered_map<int, int> taskToTime;

        
        for(int i = 0; i < tasks.size(); i++){
            int start = tasks[i][0], end = tasks[i][1], duration = tasks[i][2];
            int lastStartTime = end - duration + 1;
            timeToTask[lastStartTime][i] = duration;
            taskToTime[i] = lastStartTime;
        }
        
        int ans = 0;
        for(int t = 1; t <= 2000; t++){
            
            // someone task need to turn now or not 
            bool needTrunOn = false;
            for(int i = 0; i < tasks.size(); i++){
                if(taskToTime[i] == t){
                    needTrunOn = true;
                    break;
                }
            }
            if(!needTrunOn){
                continue;
            }
            
            // turn on
            ans += 1;
            
            // find which task can turn on now
            for(int i = 0; i < tasks.size(); i++){
                int start = tasks[i][0];
                
                if(t >= start){
                    int lastStartTime = taskToTime[i];
                    
                    if(timeToTask[lastStartTime][i] > 0){
                        int duration = timeToTask[lastStartTime][i];
                        if(duration > 1) {
                            timeToTask[lastStartTime + 1][i] = duration - 1;
                            taskToTime[i]++;
                        } else {
                            taskToTime[i] = 0;
                        }
                        
                        timeToTask[lastStartTime][i] = 0;
                    }
                }                
            }            
            
        }
        
        return ans;
    }
};