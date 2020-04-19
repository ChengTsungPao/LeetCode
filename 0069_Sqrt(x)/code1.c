int mySqrt(int x){
    unsigned long mid;
    int left = 0 + (x == 1);
    int right = x;
    while(right - left > 1){
        mid = (left + right) / 2;
        if(mid * mid > x)
            right = mid;
        else
            left = mid;
    }
    if(left < right)
        return left;
    else
        return right;
}