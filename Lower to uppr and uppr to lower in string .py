string = "wWw.HackerRank.Com"

for i in range(0, len(string)):
    if string[i].isupper():

        # temp = string[i].lower()
        string = string[i].replace(string[i], string[i].lower())

    else:
        string = string[i].replace(string[i], string[i].upper())
print(string)