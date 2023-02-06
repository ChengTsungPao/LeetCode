class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        def get_path_and_content(path):
            strs = path.split(" ")
            f_dir = strs[0]
            for filename in strs[1:]:
                f_name = filename.split("(")[0]
                f_content = filename.split("(")[-1][:-1]
                yield f_dir + "/" + f_name, f_content
                
        status = collections.defaultdict(list)
        for path in paths:
            for f_path, f_content in get_path_and_content(path):
                status[f_content].append(f_path)
                
        return [v for k, v in status.items() if len(v) >= 2]