class TopVotedCandidate {
public:
    vector<int> times;
    vector<int> wins;
        
    TopVotedCandidate(vector<int>& persons, vector<int>& times) {
        this -> times = times;
        
        int candidate = -1;
        unordered_map<int, int> vote;
        
        for(auto& person: persons){
            vote[person]++;
            if(vote[person] >= vote[candidate]){
                candidate = person;
            }
            wins.push_back(candidate);
        }
    }
    
    int q(int t) {
        int index = upper_bound(times.begin(), times.end(), t) - times.begin() - 1;
        return wins[index];
    }
};

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * TopVotedCandidate* obj = new TopVotedCandidate(persons, times);
 * int param_1 = obj->q(t);
 */