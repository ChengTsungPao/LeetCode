class Solution {
public:
    long long findMaximumElegance(vector<vector<int>>& items, int k) {
        int n = items.size();
        sort(items.rbegin(), items.rend());

        unordered_set<int> cache;
        priority_queue<int, vector<int>, greater<int>> pq;

        long long cur_p = 0;
        for(int i = 0; i < k; i++){
            int p = items[i][0], t = items[i][1];
            cur_p += p;
            if(cache.find(t) != cache.end()){
                pq.push(p);
            }
            cache.insert(t);
        }

        long long number_of_types = cache.size();
        long long ans = cur_p + (long long)pow(number_of_types, 2);
        for(int i = k; i < n; i++){
            int p = items[i][0], t = items[i][1];
            if((cache.find(t) == cache.end()) && !pq.empty()){
                int min_p = pq.top(); pq.pop();
                cur_p = cur_p - min_p + p;
                cache.insert(t);
            }
            number_of_types = cache.size();
            ans = max(ans, cur_p + (long long)pow(number_of_types, 2));
        }

        return ans;
    }
};