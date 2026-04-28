class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary={}

        for string in strs:

            #were gonna make a asci array that shoes all the values from a-z using ord , that array will be the key in which we then append that value of string to that key in the dictionary 

            key=[0]*26

            for letter in string:
                '''
                a = 80, 80-80=0
                b = 81, 81-80=1
                c = 82, 82-80=2
                
                to map offset to 0, we are subtracting ord(a)
                '''
                number =ord(letter)-ord('a')

                key[number]+=1
            
            #cannot use list as a key in python, so we can cast that list as a tuple because its immutable aka not changeable
            if tuple(key) in dictionary:
                dictionary[tuple(key)].append(string)
            else:
                dictionary[tuple(key)]=[string]
        print(f'dictionary.values:    {dictionary.values()}')

        return list(dictionary.values())
