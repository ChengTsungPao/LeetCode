int longestSubarray(int* nums, int numsSize, int limit){
    int max = 0;
    int tmp[2];
    for(int i = 0;i < numsSize;i++){
        tmp[0] = nums[i];
        tmp[1] = nums[i];
        for(int j = i;j < numsSize;j++){
            if(nums[j] < tmp[0])
                tmp[0] = nums[j];
            if(nums[j] > tmp[1])
                tmp[1] = nums[j];
            if(tmp[1] - tmp[0] <= limit && j - i + 1 > max){
                max = j - i + 1;
            }else if(tmp[1] - tmp[0] > limit){
                break;
            }
        }
        if(max >= numsSize - i - 1)
            break;
    }        
    return max;
}