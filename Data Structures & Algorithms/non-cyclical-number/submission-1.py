class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        def recurse(int):
            number=int
            summ=0
            while number>=10:
                print(f'number : {number}')
                x= number%10
                number=(number//10)
                summ+= x*x
            print('exit while')
            summ+=number*number
            print(f'number after loop {number}')
            if summ==1:
                return True
            
            elif summ in seen:
                return False
            else:
                seen.add(summ)
                return recurse(summ)
        return recurse(n)
        