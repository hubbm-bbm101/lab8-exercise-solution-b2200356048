import sys

dict = {}
with open(sys.argv[1], "r", encoding="utf-8") as f:
    for line in f:
        if line.endswith("\n"):
            line = line[:-1]
        student, informations = line.split(":")
        dict[student] = informations
for i in sys.argv[2].split(","):
    try:
         print("Name: {} , University: {}".format(i ,dict[i]))
    except:
         print("No records of {} was found!".format(i))
