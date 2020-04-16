double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size){
    int index[2] = {0, 0};
    int length = (nums1Size + nums2Size)/2 + (nums1Size + nums2Size)%2;
    int ans = 0;
    
    while(length > 0){    
        if(index[0]==nums1Size){
            index[1] += length;
            ans = nums2[index[1]-1];
            break;
        }
        if(index[1]==nums2Size){
            index[0] += length;
            ans = nums1[index[0]-1];
            break;
        }
        if(nums1[index[0]] < nums2[index[1]]){
            index[0] += 1;
            ans = nums1[index[0]-1];            
        }else{
            index[1] += 1;
            ans = nums2[index[1]-1];            
        }        
        length--;
    }
    if((nums1Size + nums2Size)%2==1){
        return ans;
    }else{
        if(index[0]==nums1Size){
            return (ans + nums2[index[1]])/2.;
        }else if(index[1]==nums2Size){
            return (ans + nums1[index[0]])/2.;
        }else if(nums1[index[0]] < nums2[index[1]]){
            return (ans + nums1[index[0]])/2.;
        }else{
            return (ans + nums2[index[1]])/2.;
        }
    }
}
