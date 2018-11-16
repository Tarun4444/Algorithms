# Definition for an interval.
class Interval:
    def __init__(self, s, e):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        #print(intervals[0].start,intervals[0].end)
        n=len(intervals)
        
        if new_interval.end > intervals[0].start and new_interval.start < intervals[0].start:
            intervals[0].start=new_interval.start
        elif new_interval.end > intervals[n-1].end and intervals[n-1].end > new_interval.start:
            intervals[n-1].end=new_interval.end
        elif new_interval.end < intervals[0].start :
            intervals.insert(0,new_interval)
        elif new_interval.end > intervals[n-1].end :
            intervals.insert(n,new_interval)
   

        for i in range(0,(len(intervals)-1)):
            if intervals[i].end < new_interval.start and intervals[i+1].start > new_interval.end:
                intervals.insert(i+1,new_interval)
                break
            elif intervals[i].end > new_interval.start and intervals[i+1].start > new_interval.end:
                intervals[i].end=new_interval.end
                break
            elif intervals[i].end < new_interval.start and intervals[i+1].start < new_interval.end:
                intervals[i].end
                break
            elif intervals[i].end > new_interval.start and intervals[i+1].start < new_interval.end:
                temp=intervals[i+1]
                del intervals[i+1]
                intervals[i].end=temp.end
                break
            
        return intervals

intervals=[]
j,k=2,4
for i in range(5):
    intervals.insert(i,Interval(j,k))
    j+=5
    k+=5
for i in range(len(intervals)):
    print(intervals[i].start,intervals[i].end)
print()
intervals =(Solution().insert(intervals,Interval(3,20) ) )
for i in range(len(intervals)):
    print(intervals[i].start,intervals[i].end)
