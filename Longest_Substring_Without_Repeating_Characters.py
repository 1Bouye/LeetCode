class solution(object):
    def __init__(self):
      def lengthOfLongestSubstring(self,s):
             charSet = set()
             l = 0
             result = 0
             
             for r in range(len(s)):
                while s[r] in charSet:
                  charSet.remove(s[l])
                  l += 1
                charSet.add(s[r])
                result = max(result, r -l + 1)
            return result