import time

class obj:
    """unsorted list objects, obtain from back-end database"""
    def __init__(self,id,begin,last):
        self.id = id
        self.begin = begin
        self.last = last

class Sorting:
    """
    TimeVec: n*n vector for storing the distance from server
    TimeDiff: pre-regulated time between different actions
    sequence: the arranged time provided to the user
    UnsortedList: the waiting list to be sorted
    [
        id:
        begin:
        last:
        location:
    ]
    """
    def __init__(self,TimeVec,TimeDiff,UnSortedList):
        self.TimeVec = TimeVec #attain from database
        self.TimeDiff = TimeDiff #attain from database
        self.UnSortedList = UnSortedList
        self.sequence = []
        # self.currentTime = time.time()
        self.currentTime = 0

    def GetTravellingTime(self, begin_id,end_id):
        return TimeVec[begin_id][end_id]

    def GreedyRoute(self):
        ''' rrange the marked schedule'''
        cnt1 = 0
        for i in self.UnSortedList:
            if i.begin != -1:
                i.last += self.TimeDiff#the lasting Time has been prolonged for "Timediff" sec
                self.sequence.append(i)
                self.UnSortedList.remove(i)#remove the user-defined ones
                # print("self.sequence=",self.sequence[:])                
                cnt1+=1
        #consider the problem for "no sorted list"

        '''arrange the unmarked schedule'''
        # 1. search for min-time-range
        TimeInterval = [] #record the time intervals between two different positioned works
        ScheduleInsertion = [] #record the inserted schedule between diff intervals
        newTime = [] #[time interval,beginid]
        newTime.append(self.sequence[0].begin-self.currentTime-self.TimeDiff)
        newTime.append(-1);
        TimeInterval.append(newTime)
        ScheduleInsertion.append([])     
        # TimeInterval.append(sequence[0].begin-self.currentTime)
        for i in range(0,len(self.sequence)-1):
            print("i",i)
            newSchedule = []
            ScheduleInsertion.append(newSchedule)
            newTime = []
            newTime.append(self.sequence[i+1].begin-(self.sequence[i].begin+self.sequence[i].last))
            newTime.append(i)
        newSchedule = []
        ScheduleInsertion.append(newSchedule)
        print("schedule insertion", ScheduleInsertion)
        TimeInterval.sort(cmp = None,key = lambda x:x[0],reverse=False)
        print(TimeInterval)
        #2. insert objects according to a greedy schedule
        SortedSequence = self.UnSortedList
        begin_id = 0 # from current place
        for i in SortedSequence:
            i.last += self.GetTravellingTime(begin_id,i.id)
            print i.last
        # SortedSequence = sorted(self.sequence,key = lambda x :x.last,reverse=False)
        cnt = 0
        valid = True
        while len(SortedSequence):
            """
            for insertion into every single piece
            try
            """
            if cnt== len(SortedSequence):
                print("No appropriate solution.")
                valid = False
                break
            cur = SortedSequence[0]
            print(TimeInterval)
            print(cnt)
            if TimeInterval[cnt][0] - cur.last < self.TimeDiff:
                cnt+=1
                continue
            ScheduleInsertion[TimeInterval[cnt][1]+1].append(cur)
            TimeInterval[cnt][0] -= (cur.last + self.TimeDiff)
            """between schedule insertion, the scheule marked 0 means from current status to the 1st scheme, and so on and so on.."""
            SortedSequence.remove(SortedSequence[0])
            begin_id = cur.id
            for i in SortedSequence:
                i.last += self.GetTravellingTime(begin_id,i.id)
            cnt = 0
            SortedSequence = self.UnSortedList
        if valid:
            print(ScheduleInsertion)


# TimeVec = [[0,3,2,6],[3,0,4,2],[2,4,0,5],[6,2,5,0]]
# TimeDiff = 0.05
# A = obj(0,1,0.5)
# B = obj(1,-1,3)
# C = obj(2,1.5,3)
# D = obj(3,-1,2)

# UnSortedList = []
# UnSortedList.append(A)
# UnSortedList.append(B)
# UnSortedList.append(C)
# UnSortedList.append(D)

# res = Sorting(TimeVec,TimeDiff,UnSortedList)
# res.GreedyRoute()



        
        
            





        


            

            



        

            

            