class Solution {
public:
    int findValidSplit(vector<int>& nums) {
        
        vector<int> primesTable = getPrimesTable(1005);
        
        unordered_map<int, int> leftFactorMap, rightFactorMap;
        for(auto& num: nums){
            getFactor(num, rightFactorMap, primesTable, 1);
        }
        
        for(int i = 0; i < nums.size() - 1; i++){
            bool isValid = true;
            int num = nums[i];
            getFactor(num, leftFactorMap, primesTable, 1);
            getFactor(num, rightFactorMap, primesTable, -1);
            for(auto it = leftFactorMap.begin(); it != leftFactorMap.end(); it++){
                int factor = it -> first;
                if(rightFactorMap.find(factor) != rightFactorMap.end()){
                    isValid = false;
                    break;
                }
            }
            if(isValid){
                return i;
            }
            
        }
        
        return -1;
    }
    
    void getFactor(int num, unordered_map<int, int>& factorMap, vector<int>& primesTable, int add) {
        int index = 0;
        while(num > 1 && index < primesTable.size()){
            int factor = primesTable[index];
            if(num % factor == 0) {
                factorMap[factor] += add;
                num /= factor;
                if(factorMap[factor] == 0){
                    factorMap.erase(factor);
                }
            } else {
                index++;
            }
        }
        if(num > 1){
            factorMap[num] += add;
            if(factorMap[num] == 0){
                factorMap.erase(num);
            }
        }
    }
    
    vector<int> getPrimesTable(int n) {
        vector<bool> primes(n, true);
        for(int i = 2; i < n; i++){
            if(primes[i]){
                for(int j = i * i; j < n; j += i){
                    primes[j] = false;
                }
            }
        }
        
        vector<int> primesTable;
        for(int i = 2; i < n; i++){
            if(primes[i]){
                primesTable.push_back(i);
            }
        }
        
        return primesTable;
    }
};