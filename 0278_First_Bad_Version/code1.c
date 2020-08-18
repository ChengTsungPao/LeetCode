// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

int firstBadVersion(int n) {
    long left = 1;
    long right = n;
    while(left < right){
        if(isBadVersion((left + right)/2)){
            right = (left + right) / 2;
        }else{
            left = (left + right) / 2 + 1;
        }
    }
    return right;    
}