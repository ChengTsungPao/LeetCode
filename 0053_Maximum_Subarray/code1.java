class Solution {
    public int maxSubArray(int[] nums) {
        int sum = 0, max = 0, min = 0;
        for (int i=0;i<nums.length;i++) {    
            if(sum > max) max = sum;
            sum += -nums[i];
            if(i==0 || sum - max < min) min = sum - max;
        }
        return -min;        
    }
}