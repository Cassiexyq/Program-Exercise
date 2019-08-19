# -*- coding: utf-8 -*-

# @Author: xyq

class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        if not pattern and s: return False # pattern为空 s不为空
        elif not pattern and not s : return True
        elif not s and pattern:
            if len(pattern) > 1 and pattern[1] == '*':
                return self.match(s,pattern[2:])
            else: return False
        else:
            # if len(pattern) > 1 and pattern[1] == '*':
            #     if s[0] == pattern[0] or pattern[0] == '.' :
            #         return self.match(s, pattern[2:]) or self.match(s[1:],pattern[2:]) or self.match(s[1:],pattern)
            #     else:
            #         return self.match(s,pattern[2:])
            # else:
            #     if s[0] == pattern[0] or pattern[0] == '.':
            #         return self.match(s[1:], pattern[1:])
            #     else:
            #         return False
            return self.checkmatch(s, 0, pattern, 0)

    def checkmatch(self,s, sidx, pattern, pidx):
        if sidx == len(s) and pidx == len(pattern): return True
        if sidx != len(s) and pidx == len(pattern): return False
        if sidx == len(s) and pidx != len(pattern):
            if pidx+1 < len(pattern) and pattern[pidx+1] == '*':  # 不能拿len(pattern）去做比较，而是根据pidx+1 看会不会越界
                return self.checkmatch(s, sidx, pattern, pidx+2)
            else: return False
        if pidx +1 < len(pattern) and pattern[pidx+1] == '*':
            if (pattern[pidx] == s[sidx] and sidx != len(s)) or (pattern[pidx] == '.' and sidx != len(s)):
                return self.checkmatch(s, sidx, pattern, pidx+2) or self.checkmatch(s,sidx+1, pattern, pidx+2) \
                       or self.checkmatch(s, sidx+1, pattern, pidx)
            else:
                return self.checkmatch(s, sidx, pattern, pidx+2)
        else:
            if(pattern[pidx] == s[sidx] and sidx != len(s)) or (pattern[pidx] == '.' and sidx != len(s)):
                return self.checkmatch(s, sidx+1, pattern, pidx+1)

        return False

s = Solution()
print(s.match('a','a.'))