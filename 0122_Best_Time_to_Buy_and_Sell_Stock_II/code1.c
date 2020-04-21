int maxProfit(int* prices, int pricesSize){
    if(pricesSize<2) 
        return 0;
    int ans = 0;
    int buy = -1;   
    for(int i = 0;i < pricesSize-1;i++){
        if(prices[i] < prices[i + 1]){
            if(buy == -1)
                buy = i;
        }else{
            if(buy != -1){
                ans += prices[i] - prices[buy];
                buy = -1;
            }
        }
    }
    if(buy != -1)
        ans += prices[pricesSize-1] - prices[buy];
    return ans;
}