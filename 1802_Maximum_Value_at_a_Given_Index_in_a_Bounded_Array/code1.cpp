class Solution {
public:
    int maxValue(int n, int index, int maxSum) {
        // [1, 1, ... , k-2, k-1, k, k-1, k-2, ... , 1, 1]
        
        int ans = 0;
        int left = 1, right = maxSum;
        while(left <= right){
            int mid = left + (right - left) / 2;
            if(getSum(mid, n, index) <= maxSum){
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return ans;        
    }
    
    long long getSum(int maxNum, int n, int index){
        long long sum = 0;
        
        long long mid = maxNum;
        long long left = max(maxNum - index, 1);
        long long right = max(maxNum - (n - index - 1), 1);
        
        sum += (left + mid) * (mid - left + 1) / 2;
        sum += (n - index) - (mid - left + 1);
        
        sum += (right + mid) * (mid - right + 1) / 2;
        sum += (index + 1) - (mid - right + 1);
        
        sum -= mid;
        
        return sum;
    }
    
};