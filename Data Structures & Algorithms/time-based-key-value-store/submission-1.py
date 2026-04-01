class TimeMap:

    def __init__(self):
      self.dict = collections.defaultdict(list)
    
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((value, timestamp))
        print(self.dict)

        
        

    def get(self, key: str, timestamp: int) -> str:
       #  using a key i can get the value form the dict 
        #  i need to check for the timestamp
        if self.dict[key]:
            # for i in range(len(self.dict[key])-1,-1,-1):
            #     if  self.dict[key][i][1] <=timestamp:
            #         return self.dict[key][i][0]
            # Implement binray search
            l=0
            r=len(self.dict[key])-1
            nums = self.dict[key]
            res = ""
            while l<=r:
                mid = (l+r)//2
                if nums[mid][1] <= timestamp:
                    res = nums[mid][0]
                    l=mid+1
                else:
                    r=mid-1
               



            return res
        else:
            return ""
        # check for the last value if the timestamp matches get the value
        # else chech if the last value of the array is less than the current value
        # send
        # if the list is empty return ""
        
