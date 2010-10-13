import re

numdict = {
    "00": "",
    "01": "one",
    "02": "two",
    "03": "three",
    "04": "four",
    "05": "five",
    "06": "six",
    "07": "seven",
    "08": "eight",
    "09": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen"
    }

tensdict = {"2":"twenty",
    "3":"thirty",
    "4":"forty",
    "5":"fifty",
    "6":"sixty",
    "7":"seventy",
    "8":"eighty",
    "9":"ninety"}

def saynum(number):
    st = str(number)
    units = st[-1:]
    if len(st) >= 2:
        tens = st[-2:-1]
    if len(st) >= 3:
        hundreds = st[-3:-2]
    if st == "1000":
        return "onethousand"
    if len(st)<=2:
        if numdict.has_key(st):
            return numdict[st]
        if numdict.has_key("0"+st):
            return numdict["0"+st]
        if units == "0":
            return tensdict[tens]
        else:
            return tensdict[tens] + "" + numdict["0"+units]
    if len(st) == 3:
        if st[1:] == "00":
            return numdict["0"+hundreds] + "hundred"
        return numdict["0"+hundreds] + "hundredand" + saynum(st[1:])

for i in range(1,1001):
    print saynum(i)

all = "".join([saynum(i) for i in range(1,1001)])

print len(all)
