int singleNonDuplicate(int* nums, int numsSize){
    for(int i = 0;i < numsSize;i += 2){
        if(i + 1 == numsSize || nums[i] != nums[i + 1])
            return nums[i];
    }
    return 0;
}