int maxProfit(int* prices, int pricesSize){
    int ans = 0;
    for(int i = 0;i < pricesSize-1;i++){
        if(prices[i] < prices[i + 1])
            ans += prices[i + 1] - prices[i];    
    }
    return ans;
}