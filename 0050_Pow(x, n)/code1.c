double myPow(double x, int n){
    unsigned long i;
    double pow(double x, int n){
        double ans = x;
        for(i=2;i<n;i=i*2)
            ans *= ans;
        if(n==0)
            return 1;
        else if(n==1)
            return x;
        else
            return ans*pow(x, n-(int)(i/2));       
    }
    if(x==0 || x==1)
        return x;
    else if(n >= 0)
        return pow(x, n);
    else
        return 1.0/pow(x, -n-1)/x;
}
