#Begin 2020.03.31 12:03:06
print("AVNum2BVNum v0.1 by ReeCheeYeah")
print("输入要转换的av号(去掉av)")
av = input("Press here:")
print("这个？",av)
choose = input("Y or N(区分大小写)")
if choose == 'Y':
    av = int(av)^177451812
    print(av)
    av = av + 100618342136696320
    print(av)
    n = 0
    while n <= 9:
        av = (av/58**n)%58
        print(av)
        n = n + 1
    else:
        print("ebd")
elif choose == 'N':
    exit()
else:
    print("你输的啥啊你")