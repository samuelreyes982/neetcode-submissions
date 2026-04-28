class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        approach is sliding window with a hashmap 
        that matches every letter of s1 with a sliding 
        window of s2, if s2 substring contains the same number 
        and values of chars of s1 then it is a permutation and 
        can be considered true
        '''

        #lets create both mappings to alphabet for s1 and s2

        s1_map={}
        s2_map={}

        #lets fill these mappings with keys first and set values to 0

        for i in range(26):
            index= i+ord('a')
            s2_map[index]=0
            s1_map[index]=0
        #
        #we have exactly 26 matches now
        #print(f's1_map:    {s1_map.items()}')

        #fill mappings with values for s1
        for i in range(len(s1)):
            s1_map[ord(s1[i])]+=1

        #print(f's1_map:    {s1_map.items()}')
        
        #now lets do our sliding window, first we must calculate how many
        # matches we already have after setting s1
        matches=0
        for i in range(26):
            letter= ord('a')+i
            if s1_map[letter]==s2_map[letter]:
                matches= matches+1
        print(f'matches: {matches}')



        #sliding window time


        left=0
        queue=[]
        matches_added=0
        for i in range(len(s2)):
            char=ord(s2[i])
            #IF MATCHES ==26 THEN BREAK LOOP AND RETURN TRUE
            if matches==26:
                return True
            
            #IF ITS NOT AN MATCH, AND IS s1[char]=0 THEN ADDING IT WONT MATTER, RESTART SUBSTRING
            if s1_map[char]==0:
                #clear queue
                for char in queue:
                    s2_map[ord(char)]-=1
                matches-=matches_added
                matches_added=0
                queue=[]
                print(f'not in substring 1 skip [reset]    s2[i]:{s2[i]}')
                left=i


            #IF IT IS A MATCH ALREADY, THEN ADDING IT AGAIN WOULD CANCEL IT OUT
            #is_match= bool(s1_map[ord(s2[i])]==s2_map[ord(s2[i])])
            elif s1_map[char]==s2_map[char]:
                
                
                print(f'in substring 1 but now overshooting, start from new    s2[i]:{s2[i]}')
                if s2[left]==s2[i]:
                    #
                    print(f'duplicate and left shifting over 1 keeping matches same')
                    left+=1
                else:
                    #clear queue
                    for char in queue:
                        s2_map[ord(char)]-=1
                    matches-=matches_added
                    matches_added=0
                    queue=[]
                    print(f'overshoot and now [reset]    s2[i]:{s2[i]}')
                    left=i

                       

                
            

            #IS A MATCH SO LETS ADD IT TO MATCHES AND KEEP GOING
            elif s1_map[char]==s2_map[char]+1:
                #add to queue
                queue.append(s2[i])
                print(f'in substring 1 and now matches lets keep searching this substring  s2[i]:{s2[i]}      matches:{matches}')
                
                s2_map[char]+=1
                matches_added+=1
                matches+=1

            #IF ITS NOT A MATCH AND IS NOT s1[char]!=0 THEN ADDING IT MIGHT HELP keep going
            elif s2_map[char]+1 < s1_map[char]:
                queue.append(s2[i])
                s2_map[char]+=1
                print(f"in substring but now at correct value yet lets keep going but no match added  queue: {queue}  matches {matches}") 
            

        return matches==26

