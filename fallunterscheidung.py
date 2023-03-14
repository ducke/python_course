
punktzahl = input('Bitte gebe deine Punktzahl ein: ')
try:
    punktzahl = int(punktzahl)
except Exception:
    exit(0)

# r1 = range(91, 100)
# r2 = range(76, 90)
# r3 = range(61, 75)
# r4 = range(46, 60)
# r5 = range(31, 45)
# r6 = range(0,30)

# if punktzahl in range(91, 100):
#     print("Note 1")
# elif punktzahl in range(76, 90):
#     print("Note 2")
# elif punktzahl in range(61, 75):
#     print("Note 3")
# elif punktzahl in range(46, 60):
#     print("Note 4")
# elif punktzahl in range(31, 45):
#     print("Note 5")
# elif punktzahl in range(0,30):
#     print("Note 6")
# else:
#     print("Keine Note!")

# if 91<=punktzahl<=100


if  punktzahl >= 91 and punktzahl <= 100:
    print("Note 1")
elif punktzahl >= 76 and punktzahl <= 90:
    print("Note 2")
elif punktzahl >= 61 and punktzahl <= 75:
    print("Note 3")
elif punktzahl >= 46 and punktzahl <= 60:
    print("Note 4")
elif punktzahl >= 31 and punktzahl <= 45:
    print("Note 5")
elif punktzahl >= 0 and punktzahl <= 30:
    print("Note 6")
else:
    print("Keine Note!")
#print(punktzahl)

