int trailingZeroes(int n){
    int ans = 0;
    unsigned long N = 5;       
    while(N <= n){
        ans += n/N;
        N *= 5;     
    }
    return ans;
}