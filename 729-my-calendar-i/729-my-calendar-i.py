class MyCalendar:
    
    '''
    [s e] [st end] 
    
    b <c or d<a 
    
    b >c and d>a
    
    
    '''

    def __init__(self):
        self.calendar=[]

    def book(self, start: int, end: int) -> bool:
        calendar=self.calendar
        if len(calendar)==0:
            calendar.append([start,end])
            return True
        
        for s,e in calendar:
            if e>start and end>s:
                return False
        
        calendar.append([start,end])
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)