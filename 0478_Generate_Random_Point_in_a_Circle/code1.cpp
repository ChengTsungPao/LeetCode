class Solution {
public:
    double R, X, Y;
    
    Solution(double radius, double x_center, double y_center) {
        R = radius;
        X = x_center;
        Y = y_center;
    }
    
    vector<double> randPoint() {
        double x = 2 * R * rand() / (RAND_MAX + 1.0) - R;
        double y = 2 * R * rand() / (RAND_MAX + 1.0) - R;
        while(x * x + y * y > R * R){
            x = 2 * R * rand() / (RAND_MAX + 1.0) - R;
            y = 2 * R * rand() / (RAND_MAX + 1.0) - R;
        }
        return {x + X, y + Y};
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(radius, x_center, y_center);
 * vector<double> param_1 = obj->randPoint();
 */