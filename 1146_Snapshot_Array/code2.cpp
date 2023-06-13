class SnapshotArray {
public:
    int cur_snap_id = 0;
    vector<vector<tuple<int, int>>> arr;
    
    SnapshotArray(int length) {
        for(int index = 0; index < length; index++){
            vector<tuple<int, int>> vec;
            vec.push_back({cur_snap_id, 0});
            arr.push_back(vec);
        }
    }
    
    void set(int index, int val) {
        tuple<int, int> t = arr[index].back();
        int last_snap_id = std::get<0>(t);
        if(last_snap_id == cur_snap_id){
            arr[index].pop_back();
        }
        arr[index].push_back({cur_snap_id, val});
    }
    
    int snap() {
        cur_snap_id += 1;
        return cur_snap_id - 1;
    }
    
    int get(int index, int snap_id) {
        tuple<int, int> t = {snap_id + 1, -1};
        int i = lower_bound(arr[index].begin(), arr[index].end(), t) - arr[index].begin() - 1;
        return std::get<1>(arr[index][i]);
    }
};

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray* obj = new SnapshotArray(length);
 * obj->set(index,val);
 * int param_2 = obj->snap();
 * int param_3 = obj->get(index,snap_id);
 */