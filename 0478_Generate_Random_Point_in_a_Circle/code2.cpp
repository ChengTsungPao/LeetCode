class Solution {
public:
    double R, X, Y;
    
    Solution(double radius, double x_center, double y_center) {
        R = radius;
        X = x_center;
        Y = y_center;
    }
    
    vector<double> randPoint() {
        double r = R * sqrt(rand() / (RAND_MAX + 1.0));
        double theta = 2 * M_PI * rand() / (RAND_MAX + 1.0);
        return {r * cos(theta) + X, r * sin(theta) + Y};
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(radius, x_center, y_center);
 * vector<double> param_1 = obj->randPoint();
 */