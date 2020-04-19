int largestRectangleArea(int* heights, int heightsSize){
    int tmp;
    int ans = 0;
    int index[2];
    for(int i = 0;i < heightsSize;i++){
        index[0] = i;
        index[1] = i;
        for(int j = i + 1;j < heightsSize;j++){
            if(heights[i] > heights[j]){
                break;
            }else{
                index[1] = j;
            }
        }
        for(int j = i - 1;j > -1;j--){
            if(heights[i] > heights[j]){
                break;
            }else{
                index[0] = j;
            }
        } 
        tmp = heights[i]*(index[1]-index[0] + 1);
        if(tmp > ans){
            ans = tmp;
        }
    }
    return ans;
}
