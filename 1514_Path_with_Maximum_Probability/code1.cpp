class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start, int end) {
        
        unordered_map<int, vector<tuple<int, double>>> graph;
        for(int i = 0; i < edges.size(); i++){
            int node1 = edges[i][0], node2 = edges[i][1];
            double prob = succProb[i];
            graph[node1].push_back({node2, prob});
            graph[node2].push_back({node1, prob});
        }
        
        priority_queue<tuple<double, int>> pq;
        pq.push({1, start});
        unordered_set<int> cache;
        
        while(!pq.empty()){
            tuple<double, int> t = pq.top(); pq.pop();
            double prob = get<0>(t);
            int node = get<1>(t);

            if(node == end){
                return prob;
            }
            
            if(cache.find(node) != cache.end()){
                continue;
            }
            cache.insert(node);
            
            for(auto& t: graph[node]){
                int nextNode = get<0>(t);
                double nextProb = get<1>(t);
                if(cache.find(nextNode) == cache.end()){
                    pq.push({prob * nextProb, nextNode});
                }
            }
            
        }
        return 0;
    }
};