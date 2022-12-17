class Solution {
public:
    string maximumBinaryString(string binary) {      
        int n = binary.size();
        int firstZeroIndex = binary.find("0") == -1 ? n : binary.find("0");
        return binary.substr(0, firstZeroIndex) + helper(binary.substr(firstZeroIndex, n - firstZeroIndex));
    }
    
    string helper(string binary) {
        int n = binary.size();
        int countZero = count(binary.begin(), binary.end(), '0');
        return (binary == "") ? binary : string(countZero - 1, '1') + "0" + string(n - countZero, '1');
    }
    
};