class Solution {
    public int[] twoSum(int[] nums, int target) {
        int N=nums.length;
        int j=-1; 
        int[] val = new int[2];
        int[] ans = new int[2];
        int[] origin = Arrays.copyOf(nums,N);
        Arrays.sort(nums);
        for(int i=0;i<N;i++){
            j=Arrays.binarySearch(nums,i+1,N,target-nums[i]);
            if(j>0){
                val[0] = nums[i];
                val[1] = nums[j];
                break;
            }
        }
        for(j=0;j<N;j++){
            if(origin[j]==val[0] || origin[j]==val[1]){
                ans[0] = j;
                break;
            }
        }
        for(j=j+1;j<N;j++){
            if(origin[j]==val[0] || origin[j]==val[1]){
                ans[1] = j;
                break;
            }            
        }        
        return ans;          
    }
}