class Solution {
public:
    long long repairCars(vector<int>& ranks, int cars) {
        priority_queue<tuple<long long, int, int>, vector<tuple<long long, int, int>>, greater<tuple<long long, int, int>>> pq;
        for(int i = 0; i < ranks.size(); i++){
            pq.push({ranks[i], 1, i});
        }
        
        long long maxTime = 0;
        for(int j = 0; j < cars; j++){
            tuple<long long, int, int> t = pq.top(); pq.pop();
            int times = get<1>(t), i = get<2>(t);
            maxTime = get<0>(t);
            pq.push({(long long)ranks[i] * pow(times + 1, 2), times + 1, i});
        }
        
        return maxTime;
    }
};