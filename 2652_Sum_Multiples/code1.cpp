class Solution {
public:
    int sumOfMultiples(int n) {
        int n3 = n / 3, n5 = n / 5, n7 = n / 7;
        int n35 = n / 15, n57 = n / 35, n37 = n / 21;
        int n357 = n / 105;
        return (formula(3, n3) + formula(5, n5) + formula(7, n7)) - (formula(15, n35) + formula(35, n57) + formula(21, n37)) + formula(105, n357);
    }
    
    int formula(int c, int n){
        return c * n * (n + 1) / 2;
    }
};