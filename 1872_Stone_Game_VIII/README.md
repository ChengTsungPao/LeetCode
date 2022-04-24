## Question: https://leetcode.com/problems/stone-game-viii/

code1.py:
* Time Limit Exceeded
> recur + memo (min-max): O(n^2)

code2.py:
* Runtime: 3950 ms, faster than 6.12% of Python3 online submissions for Stone Game VIII.
* Memory Usage: 357 MB, less than 6.12% of Python3 online submissions for Stone Game VIII.
> recur + memo (min-max + prefix sum): O(n)

code3.py:
* Time Limit Exceeded
> recur + memo (max): O(n^2)

code4.py:
* Runtime: 1888 ms, faster than 16.33% of Python3 online submissions for Stone Game VIII.
* Memory Usage: 209.3 MB, less than 10.20% of Python3 online submissions for Stone Game VIII.
> recur + memo (max + prefix sum): O(n)

code5.py:
* Time Limit Exceeded
> dp: O(n^2)

code6.py:
* Runtime: 1590 ms, faster than 33.33% of Python3 online submissions for Stone Game VIII.
* Memory Usage: 28.2 MB, less than 30.16% of Python3 online submissions for Stone Game VIII.
> dp + prefix sum: O(n)