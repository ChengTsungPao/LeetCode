class Solution {
public:
    int minSpeedOnTime(vector<int>& dist, double hour) {
        int n = dist.size();

        int ans = -1;
        int left = 1, right = pow(10, 7);
        while(left <= right){
            int mid = left + (right - left) / 2;
            if(getMinTime(dist, mid) <= hour){
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        
        return ans;
    }
    
    double getMinTime(vector<int>& dist, int speed){
        int n = dist.size();
        double time = 0;
        for(int i = 0; i < n - 1; i++){
            int d = dist[i];
            time += (d / speed) + (d % speed > 0);
        }
        time += (double)dist[n - 1] / speed;;
        return time;
    }
};