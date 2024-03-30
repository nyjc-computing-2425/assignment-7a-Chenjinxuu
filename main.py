# Write a function to convert numbers to text numerals

def text_numeral(num):
    """
    Parameters
    ---------
    int
        an integer number
    Returns
    -------
    str
        the integer in the word form
    """
    count = 0
    new_num = num
    NUM_WORD = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninty"]
    if num <= 20:
        return NUM_WORD[num-1]
    elif new_num >= 20:
        while new_num >= 10:
            new_num -= 10
            count += 1
        if new_num > 0:
            ones_count = num - count*10
            return f"{NUM_WORD[17+count]} {NUM_WORD[ones_count-1]}"
        else:
            return NUM_WORD[17+count]