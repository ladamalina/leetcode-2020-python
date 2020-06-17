import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

num_to_rom = {
    3: {1: "M"},
    2: {1: "C", 4: "CD", 5: "D", 9: "CM"},
    1: {1: "X", 4: "XL", 5: "L", 9: "XC"},
    0: {1: "I", 4: "IV", 5: "V", 9: "IX"}
}


class Solution:
    def intToRoman(self, num: int) -> str:
        out = ""
        num_s = str(num)
        for i in range(len(num_s)-1, -1, -1):
            idx = len(num_s)-1 - i
            ch_int = int(num_s[i])
            if 1 <= ch_int <= 3:
                ch_rom = num_to_rom.get(idx).get(1) * ch_int
            elif ch_int == 4:
                ch_rom = num_to_rom.get(idx).get(4)
            elif ch_int == 5:
                ch_rom = num_to_rom.get(idx).get(5)
            elif 6 <= ch_int <= 8:
                ch_rom = num_to_rom.get(idx).get(5) + num_to_rom.get(idx).get(1) * (ch_int - 5)
            elif ch_int == 9:
                ch_rom = num_to_rom.get(idx).get(9)
            else: # ch_int == 0
                ch_rom = ""
            out = f'{ch_rom}{out}'

        # logging.debug(f'num={num}, out={out}')
        return out

def main():
    assert Solution().intToRoman(0) == ""
    assert Solution().intToRoman(1) == "I"
    assert Solution().intToRoman(500) == "D"
    assert Solution().intToRoman(3) == "III"
    assert Solution().intToRoman(4) == "IV"
    assert Solution().intToRoman(9) == "IX"
    assert Solution().intToRoman(58) == "LVIII"
    assert Solution().intToRoman(1994) == "MCMXCIV"


if __name__ == '__main__':
    main()
