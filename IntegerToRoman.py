class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {1:'I', 5:'V',  10:'X', 50:'L' , 100:'C', 500 :'D', 1000:'M'}
        
        
        
        ans = ""
        keys = list(roman_dict.keys())[::-1]
        for i in range(0, len(keys), 2):
            q = num // keys[i]
            r = num % keys[i]
            
            if q == 4:
                ans += roman_dict[keys[i]] + roman_dict[keys[i-1]] 
            elif q == 9:
                ans += roman_dict[keys[i]] + roman_dict[keys[i-2]]
            elif 1 <= q < 4:
                ans += roman_dict[keys[i]] * q 
            elif 5 <= q < 9:
                ans += roman_dict[keys[i-1]] + roman_dict[keys[i]] * (q-5) * int(q>5)
            
            num = r
            
        return ans
        
