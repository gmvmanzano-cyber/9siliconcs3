![alt text](image.png)

Byear = int(input("Enter your birth year: "))
if Byear < 1900:
    print("Invalid Year, it should not be earlier than 1900")
else:
    zsign = (Byear-1900)%12
    if zsign == 0:
        print("Your Chinese Zodiac Sign is: Rat (鼠 / Shǔ)")
    elif zsign == 1:
        print("Your Chinese Zodiac Sign is: Ox (牛 / Niú)")
    elif zsign == 2:
        print("Your Chinese Zodiac Sign is: Tiger (虎 / Hǔ)")
    elif zsign == 3:
        print("Your Chinese Zodiac Sign is: Rabbit (兔 / Tù)")
    elif zsign == 4:
        print("Your Chinese Zodiac Sign is: Dragon (龙 / Lóng)")
    elif zsign == 5:
        print("Your Chinese Zodiac Sign is: Snake (蛇 / Shé)")
    elif zsign == 6:
        print("Your Chinese Zodiac Sign is: Horse (马 / Mǎ)")
    elif zsign == 7:
        print("Your Chinese Zodiac Sign is: Goat (羊 / Yáng)")
    elif zsign == 8:
        print("Your Chinese Zodiac Sign is: Monkey (猴 / Hóu)")
    elif zsign == 9:
        print("Your Chinese Zodiac Sign is: Rooster (鸡 / Jī)")
    elif zsign == 10:
        print("Your Chinese Zodiac Sign is: Dog (狗 / Gǒu)")
    elif zsign == 11:
        print("Your Chinese Zodiac Sign is: Pig (猪 / Zhū)")