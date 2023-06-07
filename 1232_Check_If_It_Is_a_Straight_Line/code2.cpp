class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        int n = coordinates.size();
        int x1 = coordinates[0][0], y1 = coordinates[0][1];
        int x2 = coordinates[1][0], y2 = coordinates[1][1];
        
        tuple<int, int> t = norm(x2 - x1, y2 - y1);
        int dx1 = get<0>(t);
        int dy1 = get<1>(t);
        
        for(int i = 2; i < n; i++){
            x2 = coordinates[i][0]; 
            y2 = coordinates[i][1];
            t = norm(x2 - x1, y2 - y1);
            int dx2 = get<0>(t);
            int dy2 = get<1>(t);
            if(dx2 == 0 && dy2 == 0){
                continue;
            }
            
            if(dx1 != dx2 || dy1 != dy2){
                return false;
            }
        }
        
        return true;
    }
    
    tuple<int, int> norm(int dx, int dy){
        if(dx < 0) {
            dx = -dx;
            dy = -dy;
        }
        if(dx == 0 && dy == 0){
            return {0, 0};
        } else if (dx == 0) {
            return {0, 1};
        } else if (dy == 0) {
            return {1, 0};
        }
        int g = gcd(dx, abs(dy));
        dx /= g;
        dy /= g;
        return {dx, dy};
    }
    
    int gcd(int a, int b){
        if(a < b){
            swap(a, b);
        }
        if(a % b == 0){
            return b;
        }
        return gcd(a % b, b);
    }
    
};