
kennwort = input("Kennwort eingeben: ")
# count = 0
# while len(kennwort) < 10:
#     print("Zu kurz")
#     count += 1
#     if count == 10:
#         print("zu viele versuche")
#         break
#     kennwort = input("Kennwort eingeben: ")

def kennwort_check(anzahl_versuche,kennwort):
    count = 0
    while len(kennwort) < anzahl_versuche:
        print("Zu kurz")
        count += 1
        if count == 10:
            print("zu viele versuche")
            break
        kennwort = input("Kennwort eingeben: ")

kennwort = input("Kennwort eingeben: ")
kennwort_check(2,kennwort)