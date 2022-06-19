class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        
        # stack   => result與current的過去狀態
        # result  => 目前能夠確定的結果
        # current => 需相乘完才能與result合併 (Ex. "{{a, b}, c{d, e}}")
        
        stack, result, current = [], [], []
        
        for ch in expression:
            # 遇到字母直接相乘
            if ch.isalpha():
                current = [s + ch for s in current or [""]]
            # 儲存前一個{}內的狀態
            elif ch == "{":
                stack.append((result, current))
                result, current = [], []
            # 取出前一個{}內的狀態，與現在的狀態合併
            elif ch == "}":
                preResult, preCurrent = stack.pop()
                current = [p + s for p in preCurrent or [""] for s in result + current]
                result = preResult
            # 遇到下一個","代表current結果已確定
            elif ch == ",":
                result += current
                current = []
                
        return sorted(set(result + current))