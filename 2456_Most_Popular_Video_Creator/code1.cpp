class Solution {
public:
    vector<vector<string>> mostPopularCreator(vector<string>& creators, vector<string>& ids, vector<int>& views) {
        unordered_map<string, int> creatorView;
        unordered_map<string, vector<tuple<int, string>>> creatorIds;
        
        int maxView = 0;
        for(int i = 0; i < creators.size(); i++){
            string creator = creators[i], id = ids[i];
            int view = views[i];
            creatorView[creator] += view;
            creatorIds[creator].push_back(make_tuple(view, id));
            maxView = max(maxView, creatorView[creator]);
        }
        
        vector<vector<string>> ans;
        for(auto& [creator, view]: creatorView){
            if(view == maxView){
                tuple<int, string> element = *min_element(creatorIds[creator].begin(), creatorIds[creator].end(),
                    [] (tuple<int, string>& t1, tuple<int, string>& t2) { 
                        if(get<0>(t1) > get<0>(t2)) return true;
                        else if(get<0>(t1) == get<0>(t2) && get<1>(t1) < get<1>(t2)) return true;
                        return false;
                });
                string id = get<1>(element);
                ans.push_back({creator, id});
            }
        }
        return ans;
    }
};
