#       BVNUM2AVNUM V0.2 BY REECHEEYEAH
#         PLEASE DOWNLOAD FROM GITHUB
#READY PART START
print("BVNum2AVNum v0.2 By ReeCheeYeah")
print("请依次输入去bv后的第二、三、五、七、九、十位，如bv17x411w7KC就输入\n7\nx\n1\nw\nK\nC")
print("第一位已自动调整为1(若不是请在github提交issues)")
finum = 494893003072
senum = input("输入第二位：")
thinum = input("输入第三位：")
print("第四位已自动调整为4(若不是请在github提交issues)")
fonum = 3969955533258496
fifnum = input("输入第五位：")
print("第六位已自动调整为1(若不是请在github提交issues)")
sinum = 96559563615384064
sevnum = input("输入第七位：")
print("第八位已自动调整为7(若不是请在github提交issues)")
einum = 88319366702080
ninum = input("输入第九位：")
thnum = input("输入第十位：")
# READY PART END
# CALCULATE SIGNATURE START
print("转换bv1",senum,thinum,'4',fifnum,'1',sevnum,'7',ninum,thnum,"?")
choose = input("Y或N(区分大小写)")
if choose == "Y":
    if senum == "1":
        senum = 13
    elif senum == "2":
        senum = 12
    elif senum == "3":
        senum = 46
    elif senum == "4":
        senum = 31
    elif senum == "5":
        senum = 43
    elif senum == "6":
        senum = 18
    elif senum == "7":
        senum = 40
    elif senum == "8":
        senum = 28
    elif senum == "9":
        senum = 5
    elif senum == "A":
        senum = 54
    elif senum == "B":
        senum = 20
    elif senum == "C":
        senum = 15
    elif senum == "D":
        senum = 8
    elif senum == "E":
        senum = 39
    elif senum == "F":
        senum = 57
    elif senum == "G":
        senum = 45
    elif senum == "H":
        senum = 36
    elif senum == "J":
        senum = 38
    elif senum == "K":
        senum = 51
    elif senum == "L":
        senum = 42
    elif senum == "M":
        senum = 49
    elif senum == "N":
        senum = 52
    elif senum == "P":
        senum = 53
    elif senum == "Q":
        senum = 7
    elif senum == "R":
        senum = 4
    elif senum == "S":
        senum = 9
    elif senum == "T":
        senum = 50
    elif senum == "U":
        senum = 10
    elif senum == "V":
        senum = 44
    elif senum == "W":
        senum = 34
    elif senum == "X":
        senum = 6
    elif senum == "Y":
        senum = 25
    elif senum == "Z":
        senum = 1
    elif senum == "a":
        senum = 26
    elif senum == "b":
        senum = 29
    elif senum == "c":
        senum = 56
    elif senum == "d":
        senum = 3
    elif senum == "e":
        senum = 24
    elif senum == "f":
        senum = 0
    elif senum == "g":
        senum = 47
    elif senum == "h":
        senum = 27
    elif senum == "i":
        senum = 22
    elif senum == "j":
        senum = 41
    elif senum == "k":
        senum = 16
    elif senum == "m":
        senum = 11
    elif senum == "n":
        senum = 37
    elif senum == "o":
        senum = 2
    elif senum == "p":
        senum = 35
    elif senum == "q":
        senum = 21
    elif senum == "r":
        senum = 17
    elif senum == "s":
        senum = 33
    elif senum == "t":
        senum = 30
    elif senum == "u":
        senum = 48
    elif senum == "v":
        senum = 23
    elif senum == "w":
        senum = 55
    elif senum == "x":
        senum = 32
    elif senum == "y":
        senum = 14
    elif senum == "z":
        senum = 19
    else:
        print("第二位错误！")
    if thinum == "1":
        thinum = 13
    elif thinum == "2":
        thinum = 12
    elif thinum == "3":
        thinum = 46
    elif thinum == "4":
        thinum = 31
    elif thinum == "5":
        thinum = 43
    elif thinum == "6":
        thinum = 18
    elif thinum == "7":
        thinum = 40
    elif thinum == "8":
        thinum = 28
    elif thinum == "9":
        thinum = 5
    elif thinum == "A":
        thinum = 54
    elif thinum == "B":
        thinum = 20
    elif thinum == "C":
        thinum = 15
    elif thinum == "D":
        thinum = 8
    elif thinum == "E":
        thinum = 39
    elif thinum == "F":
        thinum = 57
    elif thinum == "G":
        thinum = 45
    elif thinum == "H":
        thinum = 36
    elif thinum == "J":
        thinum = 38
    elif thinum == "K":
        thinum = 51
    elif thinum == "L":
        thinum = 42
    elif thinum == "M":
        thinum = 49
    elif thinum == "N":
        thinum = 52
    elif thinum == "P":
        thinum = 53
    elif thinum == "Q":
        thinum = 7
    elif thinum == "R":
        thinum = 4
    elif thinum == "S":
        thinum = 9
    elif thinum == "T":
        thinum = 50
    elif thinum == "U":
        thinum = 10
    elif thinum == "V":
        thinum = 44
    elif thinum == "W":
        thinum = 34
    elif thinum == "X":
        thinum = 6
    elif thinum == "Y":
        thinum = 25
    elif thinum == "Z":
        thinum = 1
    elif thinum == "a":
        thinum = 26
    elif thinum == "b":
        thinum = 29
    elif thinum == "c":
        thinum = 56
    elif thinum == "d":
        thinum = 3
    elif thinum == "e":
        thinum = 24
    elif thinum == "f":
        thinum = 0
    elif thinum == "g":
        thinum = 47
    elif thinum == "h":
        thinum = 27
    elif thinum == "i":
        thinum = 22
    elif thinum == "j":
        thinum = 41
    elif thinum == "k":
        thinum = 16
    elif thinum == "m":
        thinum = 11
    elif thinum == "n":
        thinum = 37
    elif thinum == "o":
        thinum = 2
    elif thinum == "p":
        thinum = 35
    elif thinum == "q":
        thinum = 21
    elif thinum == "r":
        thinum = 17
    elif thinum == "s":
        thinum = 33
    elif thinum == "t":
        thinum = 30
    elif thinum == "u":
        thinum = 48
    elif thinum == "v":
        thinum = 23
    elif thinum == "w":
        thinum = 55
    elif thinum == "x":
        thinum = 32
    elif thinum == "y":
        thinum = 14
    elif thinum == "z":
        thinum = 19
    else:
        print("第三位错误！")
    if fifnum == "1":
        fifnum = 13
    elif fifnum == "2":
        fifnum = 12
    elif fifnum == "3":
        fifnum = 46
    elif fifnum == "4":
        fifnum = 31
    elif fifnum == "5":
        fifnum = 43
    elif fifnum == "6":
        fifnum = 18
    elif fifnum == "7":
        fifnum = 40
    elif fifnum == "8":
        fifnum = 28
    elif fifnum == "9":
        fifnum = 5
    elif fifnum == "A":
        fifnum = 54
    elif fifnum == "B":
        fifnum = 20
    elif fifnum == "C":
        fifnum = 15
    elif fifnum == "D":
        fifnum = 8
    elif fifnum == "E":
        fifnum = 39
    elif fifnum == "F":
        fifnum = 57
    elif fifnum == "G":
        fifnum = 45
    elif fifnum == "H":
        fifnum = 36
    elif fifnum == "J":
        fifnum = 38
    elif fifnum == "K":
        fifnum = 51
    elif fifnum == "L":
        fifnum = 42
    elif fifnum == "M":
        fifnum = 49
    elif fifnum == "N":
        fifnum = 52
    elif fifnum == "P":
        fifnum = 53
    elif fifnum == "Q":
        fifnum = 7
    elif fifnum == "R":
        fifnum = 4
    elif fifnum == "S":
        fifnum = 9
    elif fifnum == "T":
        fifnum = 50
    elif fifnum == "U":
        fifnum = 10
    elif fifnum == "V":
        fifnum = 44
    elif fifnum == "W":
        fifnum = 34
    elif fifnum == "X":
        fifnum = 6
    elif fifnum == "Y":
        fifnum = 25
    elif fifnum == "Z":
        fifnum = 1
    elif fifnum == "a":
        fifnum = 26
    elif fifnum == "b":
        fifnum = 29
    elif fifnum == "c":
        fifnum = 56
    elif fifnum == "d":
        fifnum = 3
    elif fifnum == "e":
        fifnum = 24
    elif fifnum == "f":
        fifnum = 0
    elif fifnum == "g":
        fifnum = 47
    elif fifnum == "h":
        fifnum = 27
    elif fifnum == "i":
        fifnum = 22
    elif fifnum == "j":
        fifnum = 41
    elif fifnum == "k":
        fifnum = 16
    elif fifnum == "m":
        fifnum = 11
    elif fifnum == "n":
        fifnum = 37
    elif fifnum == "o":
        fifnum = 2
    elif fifnum == "p":
        fifnum = 35
    elif fifnum == "q":
        fifnum = 21
    elif fifnum == "r":
        fifnum = 17
    elif fifnum == "s":
        fifnum = 33
    elif fifnum == "t":
        fifnum = 30
    elif fifnum == "u":
        fifnum = 48
    elif fifnum == "v":
        fifnum = 23
    elif fifnum == "w":
        fifnum = 55
    elif fifnum == "x":
        fifnum = 32
    elif fifnum == "y":
        fifnum = 14
    elif fifnum == "z":
        fifnum = 19
    else:
        print("第五位错误！")
    if sevnum == "1":
        sevnum = 13
    elif sevnum == "2":
        sevnum = 12
    elif sevnum == "3":
        sevnum = 46
    elif sevnum == "4":
        sevnum = 31
    elif sevnum == "5":
        sevnum = 43
    elif sevnum == "6":
        sevnum = 18
    elif sevnum == "7":
        sevnum = 40
    elif sevnum == "8":
        sevnum = 28
    elif sevnum == "9":
        sevnum = 5
    elif sevnum == "A":
        sevnum = 54
    elif sevnum == "B":
        sevnum = 20
    elif sevnum == "C":
        sevnum = 15
    elif sevnum == "D":
        sevnum = 8
    elif sevnum == "E":
        sevnum = 39
    elif sevnum == "F":
        sevnum = 57
    elif sevnum == "G":
        sevnum = 45
    elif sevnum == "H":
        sevnum = 36
    elif sevnum == "J":
        sevnum = 38
    elif sevnum == "K":
        sevnum = 51
    elif sevnum == "L":
        sevnum = 42
    elif sevnum == "M":
        sevnum = 49
    elif sevnum == "N":
        sevnum = 52
    elif sevnum == "P":
        sevnum = 53
    elif sevnum == "Q":
        sevnum = 7
    elif sevnum == "R":
        sevnum = 4
    elif sevnum == "S":
        sevnum = 9
    elif sevnum == "T":
        sevnum = 50
    elif sevnum == "U":
        sevnum = 10
    elif sevnum == "V":
        sevnum = 44
    elif sevnum == "W":
        sevnum = 34
    elif sevnum == "X":
        sevnum = 6
    elif sevnum == "Y":
        sevnum = 25
    elif sevnum == "Z":
        sevnum = 1
    elif sevnum == "a":
        sevnum = 26
    elif sevnum == "b":
        sevnum = 29
    elif sevnum == "c":
        sevnum = 56
    elif sevnum == "d":
        sevnum = 3
    elif sevnum == "e":
        sevnum = 24
    elif sevnum == "f":
        sevnum = 0
    elif sevnum == "g":
        sevnum = 47
    elif sevnum == "h":
        sevnum = 27
    elif sevnum == "i":
        sevnum = 22
    elif sevnum == "j":
        sevnum = 41
    elif sevnum == "k":
        sevnum = 16
    elif sevnum == "m":
        sevnum = 11
    elif sevnum == "n":
        sevnum = 37
    elif sevnum == "o":
        sevnum = 2
    elif sevnum == "p":
        sevnum = 35
    elif sevnum == "q":
        sevnum = 21
    elif sevnum == "r":
        sevnum = 17
    elif sevnum == "s":
        sevnum = 33
    elif sevnum == "t":
        sevnum = 30
    elif sevnum == "u":
        sevnum = 48
    elif sevnum == "v":
        sevnum = 23
    elif sevnum == "w":
        sevnum = 55
    elif sevnum == "x":
        sevnum = 32
    elif sevnum == "y":
        sevnum = 14
    elif sevnum == "z":
        sevnum = 19
    else:
        print("第七位错误！")
    if ninum == "1":
        ninum = 13
    elif ninum == "2":
        ninum = 12
    elif ninum == "3":
        ninum = 46
    elif ninum == "4":
        ninum = 31
    elif ninum == "5":
        ninum = 43
    elif ninum == "6":
        ninum = 18
    elif ninum == "7":
        ninum = 40
    elif ninum == "8":
        ninum = 28
    elif ninum == "9":
        ninum = 5
    elif ninum == "A":
        ninum = 54
    elif ninum == "B":
        ninum = 20
    elif ninum == "C":
        ninum = 15
    elif ninum == "D":
        ninum = 8
    elif ninum == "E":
        ninum = 39
    elif ninum == "F":
        ninum = 57
    elif ninum == "G":
        ninum = 45
    elif ninum == "H":
        ninum = 36
    elif ninum == "J":
        ninum = 38
    elif ninum == "K":
        ninum = 51
    elif ninum == "L":
        ninum = 42
    elif ninum == "M":
        ninum = 49
    elif ninum == "N":
        ninum = 52
    elif ninum == "P":
        ninum = 53
    elif ninum == "Q":
        ninum = 7
    elif ninum == "R":
        ninum = 4
    elif ninum == "S":
        ninum = 9
    elif ninum == "T":
        ninum = 50
    elif ninum == "U":
        ninum = 10
    elif ninum == "V":
        ninum = 44
    elif ninum == "W":
        ninum = 34
    elif ninum == "X":
        ninum = 6
    elif ninum == "Y":
        ninum = 25
    elif ninum == "Z":
        ninum = 1
    elif ninum == "a":
        ninum = 26
    elif ninum == "b":
        ninum = 29
    elif ninum == "c":
        ninum = 56
    elif ninum == "d":
        ninum = 3
    elif ninum == "e":
        ninum = 24
    elif ninum == "f":
        ninum = 0
    elif ninum == "g":
        ninum = 47
    elif ninum == "h":
        ninum = 27
    elif ninum == "i":
        ninum = 22
    elif ninum == "j":
        ninum = 41
    elif ninum == "k":
        ninum = 16
    elif ninum == "m":
        ninum = 11
    elif ninum == "n":
        ninum = 37
    elif ninum == "o":
        ninum = 2
    elif ninum == "p":
        ninum = 35
    elif ninum == "q":
        ninum = 21
    elif ninum == "r":
        ninum = 17
    elif ninum == "s":
        ninum = 33
    elif ninum == "t":
        ninum = 30
    elif ninum == "u":
        ninum = 48
    elif ninum == "v":
        ninum = 23
    elif ninum == "w":
        ninum = 55
    elif ninum == "x":
        ninum = 32
    elif ninum == "y":
        ninum = 14
    elif ninum == "z":
        ninum = 19
    else:
        print("第九位错误！")
    if thnum == "1":
        thnum = 13
    elif thnum == "2":
        thnum = 12
    elif thnum == "3":
        thnum = 46
    elif thnum == "4":
        thnum = 31
    elif thnum == "5":
        thnum = 43
    elif thnum == "6":
        thnum = 18
    elif thnum == "7":
        thnum = 40
    elif thnum == "8":
        thnum = 28
    elif thnum == "9":
        thnum = 5
    elif thnum == "A":
        thnum = 54
    elif thnum == "B":
        thnum = 20
    elif thnum == "C":
        thnum = 15
    elif thnum == "D":
        thnum = 8
    elif thnum == "E":
        thnum = 39
    elif thnum == "F":
        thnum = 57
    elif thnum == "G":
        thnum = 45
    elif thnum == "H":
        thnum = 36
    elif thnum == "J":
        thnum = 38
    elif thnum == "K":
        thnum = 51
    elif thnum == "L":
        thnum = 42
    elif thnum == "M":
        thnum = 49
    elif thnum == "N":
        thnum = 52
    elif thnum == "P":
        thnum = 53
    elif thnum == "Q":
        thnum = 7
    elif thnum == "R":
        thnum = 4
    elif thnum == "S":
        thnum = 9
    elif thnum == "T":
        thnum = 50
    elif thnum == "U":
        thnum = 10
    elif thnum == "V":
        thnum = 44
    elif thnum == "W":
        thnum = 34
    elif thnum == "X":
        thnum = 6
    elif thnum == "Y":
        thnum = 25
    elif thnum == "Z":
        thnum = 1
    elif thnum == "a":
        thnum = 26
    elif thnum == "b":
        thnum = 29
    elif thnum == "c":
        thnum = 56
    elif thnum == "d":
        thnum = 3
    elif thnum == "e":
        thnum = 24
    elif thnum == "f":
        thnum = 0
    elif thnum == "g":
        thnum = 47
    elif thnum == "h":
        thnum = 27
    elif thnum == "i":
        thnum = 22
    elif thnum == "j":
        thnum = 41
    elif thnum == "k":
        thnum = 16
    elif thnum == "m":
        thnum = 11
    elif thnum == "n":
        thnum = 37
    elif thnum == "o":
        thnum = 2
    elif thnum == "p":
        thnum = 35
    elif thnum == "q":
        thnum = 21
    elif thnum == "r":
        thnum = 17
    elif thnum == "s":
        thnum = 33
    elif thnum == "t":
        thnum = 30
    elif thnum == "u":
        thnum = 48
    elif thnum == "v":
        thnum = 23
    elif thnum == "w":
        thnum = 55
    elif thnum == "x":
        thnum = 32
    elif thnum == "y":
        thnum = 14
    elif thnum == "z":
        thnum = 19
    else:
        print("第十位错误！")
    # CALCULATE SIGNATURE END
    # CALCULATE XOR READY PART START
    senum = senum * 3364
    thinum = thinum * 11316496
    fifnum = fifnum * 656356768
    sevnum = sevnum * 195112
    ninum = ninum * 58
    he = finum + senum + thinum + fonum + fifnum + sinum + sevnum + einum + ninum + thnum
    he = he - 100618342136696320
    # CALCULATE XOR READY PART END
    # CALCULATE XOR START 
    he = int(he)^177451812
    # CALCULATE XOR END
    print("转换成功！结果为av",he)
    input("按回车退出")
elif choose == 'N':
    exit()
else:
    print("你输的都啥啊你")
#ALL DONE!
#BVNUM2AVNUM V0.2.1 COMPLETED AT 2020.03.31 20:01:48
#BY REECHEEYEAH
#THANKS FOR YOUR USING!