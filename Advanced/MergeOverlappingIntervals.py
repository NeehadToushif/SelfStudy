'''
Problem Description
Given a collection of intervals, merge all overlapping intervals.

Problem Constraints
1 <= Total number of intervals <= 100000.'''
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    #use this if intervals is list of list or list of tuples
    def merge(self, intervals):
        l,r = list(intervals[0])
        ans =[]
        n = len(intervals)
        for i in range(1,n):
            start,end = intervals[i]
            if start <= r:
                r = max(end,r)
            else:
                ans.append([l, r])
                l = start
                r = end
        ans.append([l, r])
        return ans


    # if intervals is list of Interval objects
    def merge1(self, intervals):
        intervals = sorted(intervals,key=lambda interval: interval.start)
        l, r = intervals[0].start,intervals[0].end
        ans = []
        n = len(intervals)
        for i in range(1, n):
            start, end = intervals[i].start,intervals[i].end
            if start <= r:
                r = max(end, r)
            else:
                ans.append(Interval(l,r))
                l = start
                r = end
        ans.append(Interval(l,r))
        return ans



A = [[1,6],[8,10],[15,18]]
A = [[1,3],[2,6],[8,10],[15,18]]
# A = [[1,3],[2,6],[4,10],[15,18]]
print(Solution().merge(A))
A = [ Interval(1, 10), Interval(2, 9), Interval(3, 8), Interval(4, 7), Interval(5, 6), Interval(6, 6) ]
out =Solution().merge1(A)
print([[o.start,o.end] for o in out ])