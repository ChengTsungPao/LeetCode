int maxArea(int* height, int heightSize){
    int ans = 0;
    int i = 0;
    int j = heightSize - 1;
    while(i < j){
        if(height[i] < height[j]){
            if(height[i] * (j - i) > ans)
                ans = height[i] * (j - i);
            i += 1;
        }else{
            if(height[j] * (j - i) > ans)
                ans = height[j] * (j - i);
            j -= 1;
        }
    }
    return ans;
}