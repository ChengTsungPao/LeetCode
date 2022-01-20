class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        
        def add(i, j, record):
            i_ = bisect.bisect_left(record, i)
            j_ = bisect.bisect_right(record, j)
            
            if i_ % 2 == 0 and j_ % 2 == 0:
                record[i_:j_] = [i, j]
            elif i_ % 2 == 0 and j_ % 2 == 1:
                record[i_:j_] = [i]
            elif i_ % 2 == 1 and j_ % 2 == 0:
                record[i_:j_] = [j]
            else:
                record[i_:j_] = []
            
        record = []
        for word in words:
            for i in range(len(s)):
                i, j = i, i + len(word)
                if word == s[i : j]:
                    add(i, j, record)
        if len(record) == 0:
            return s
        if record[-1] < len(s):
            record.append(len(s))
        
        ans = s[:record[0]]
        for index in range(len(record) - 1):
            i, j = record[index], record[index + 1]
            if index % 2 == 0:
                ans += "<b>{}</b>".format(s[i : j])
            else:
                ans += s[i : j]
            
        return ans