class Solution:
    def intToRoman(self, num: int) -> str:
        str = ''
        
        while num > 0:
            if num >= 1000:
                str += 'M'
                num -= 1000
            elif num >= 500:
                if num >= 900:
                    str += 'CM'
                    num -= 900
                else:
                    str += 'D'
                    num -= 500
            elif num >= 100:
                if num >= 400:
                    str += 'CD'
                    num -= 400
                else:
                    str += 'C'
                    num -= 100
            elif num >= 50:
                if num >= 90:
                    str += 'XC'
                    num -= 90
                else:
                    str += 'L'
                    num -= 50
            elif num >= 10:
                if num >= 40:
                    str += 'XL'
                    num -= 40
                else:
                    str += 'X'
                    num -= 10
            elif num >= 5:
                if num >= 9:
                    str += 'IX'
                    num -= 9
                else:
                    str += 'V'
                    num -= 5
            else:
                if num >= 4:
                    str += 'IV'
                    num -= 4
                else:
                    str += 'I'
                    num -= 1
        return str