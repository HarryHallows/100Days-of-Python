yourName = input("Enter your name\n")
yourCrushName = input("Now enter your crush's name\n")

finalNames = (yourName + yourCrushName).lower()

trueLove = "true love"

t = (trueLove + finalNames).count("t")
r = (trueLove + finalNames).count("r")
u = (trueLove + finalNames).count("u")
e = (trueLove + finalNames).count("e")

l = (trueLove + finalNames).count("l")
o = (trueLove + finalNames).count("o")
v = (trueLove + finalNames).count("v")
e = (trueLove + finalNames).count("e")

loveScore = t + r + u + e + l + o + v + e 


if loveScore >= 90 :
    print(f"Your score is {loveScore}%, and were born to be together!")
elif loveScore < 90 and loveScore > 50:
    print(f"Your score is {loveScore}%, which you both go together okay")
elif loveScore < 50 and loveScore > 20:
    print(f"Your love score is {loveScore}%, you can try your chances...")
else:
    print(f"Your love percentage is {loveScore}%, you're both doomed to be. Save yourself the time and find someone better!")
