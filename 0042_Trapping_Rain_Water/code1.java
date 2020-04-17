class Solution {
    public int trap(int[] height) {

        int maxpos = 0;
        int max = 0;
        for(int i=0;i<height.length;i++){
            if(height[i]>max){
                max = height[i];
                maxpos = i;
            }
        }
        
        int total_rain = 0;
        int start = 0;
        int sum = 0;        
        for(int i=1;i<=maxpos;i++){
            if(height[i]>=height[start]){
                total_rain += (i-start-1)*height[start] - sum;
                sum = 0;
                start = i;
            }else{
                sum += height[i];
            }         
        }

        start = height.length-1;
        sum = 0;        
        for(int i=height.length-2;i>=maxpos;i--){     
            if(height[i]>=height[start]){
                total_rain += (start-i-1)*height[start] - sum;
                sum = 0;
                start = i;
            }else{
                sum += height[i];
            }         
        }

        return total_rain;        
    }
}