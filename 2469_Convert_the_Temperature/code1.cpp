class Solution {
public:
    vector<double> convertTemperature(double celsius) {
        return {round((celsius + 273.15) * pow(10, 5)) / pow(10, 5), round((celsius * 1.80 + 32.00) * pow(10, 5)) / pow(10, 5)};
    }
};