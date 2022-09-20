class Solution {
public:
    string validIPAddress(string queryIP) {
        if(isIPv4(queryIP)){
            return "IPv4";
        } else if(isIPv6(queryIP)){
            return "IPv6";
        } else {
            return "Neither";
        }
    }
    
    bool isIPv4(string str){
        int c = count(str.begin(), str.end(), '.');
        if(c != 3){
            return false;
        }
        
        int num;
        vector<string> numbers = split(str, ".");
        for(unsigned int i = 0; i < numbers.size(); i++){
            if(!(isdigitStr(numbers[i]) && (numbers[i].size() == 1 || numbers[i][0] != '0'))){
                return false;
            }
            if(numbers[i].size() > 3){
                return false;
            }
            num = stoi(numbers[i]);
            if(!(num >= 0 && num <= 255)){
                return false;
            }            
        }  
        return true;
    }
    
    bool isIPv6(string str){
        int c = count(str.begin(), str.end(), ':');
        if(c != 7){
            return false;
        }
        
        int num;
        vector<string> numbers = split(str, ":");
        for(unsigned int i = 0; i < numbers.size(); i++){
            if(!(isHexStr(numbers[i]) && numbers[i].size() <= 4)){
                return false;
            }           
        }  
        return true;
    }
    
    bool isdigitStr(string str){
        for(unsigned int i = 0; i < str.size(); i++){
            if(!(str[i] >= '0' && str[i] <= '9')){
                return false;
            }
        }
        return str.size() > 0;
    }
    
    bool isHexStr(string str){
        for(unsigned int i = 0; i < str.size(); i++){
            if(!((str[i] >= 'A' && str[i] <= 'F') || (str[i] >= 'a' && str[i] <= 'f') || (str[i] >= '0' && str[i] <= '9'))){
                return false;
            }
        }
        return str.size() > 0;
    }
    
    vector<string> split(string str, string key){
        unsigned int idx;
        vector<string> result;
        while(str.find(key) != -1){
            idx = str.find(key);
            result.push_back(str.substr(0, idx));
            str = str.substr(idx + 1);
        }
        result.push_back(str.substr(0, str.size()));
        return result; 
    }
    
};