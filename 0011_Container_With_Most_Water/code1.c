int maxArea(int* height, int heightSize){

    // 方法: Two Pointer
    // 概念: height比較小的一側往前搜尋，才有機會找到較大的height使的面積變大

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