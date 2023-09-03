class Solution {
public:
    long long minimumPossibleSum(int n, int target) {
        long long sum = 0;
        int num = 1;
        while(n > 0){
            if(num <= target / 2 || num >= target){
                sum += num;
                n--;
            }
            num++;
        }
        return sum;
    }
};