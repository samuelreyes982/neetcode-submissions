class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets=len(position)
        result=[0]*len(position)

        dic={}
        for i in range(len(position)):
            dic[position[i]]=speed[i]

        stack=[]
        
        
        position_sorted=sorted(position)
        print(f'positions: {position_sorted}')
        for index, positions in enumerate(position_sorted):
            time_to_target_in_hours = (target-positions)/dic[positions]
            while stack and stack[-1][1]<=time_to_target_in_hours:
                stack.pop()
                fleets-=1
            
            stack.append([index,time_to_target_in_hours])
        
        return fleets

        ttt=[5,6]

        