# Inlezen ledenlijst zoals aangeleverd

a = open('ledenlijst.txt')
ledenlijst = a.read().splitlines()
a.close()

with open('ledenlijst website.txt') as b:
    ledenlijst_website = b.read().splitlines()


for lid in ledenlijst:
    if lid not in ledenlijst_website:
        print lid + " bestaat niet op de website..."

for lid in ledenlijst_website:
    if lid not in ledenlijst:
        print lid + " heeft een account, maar zou die niet moeten hebben"

