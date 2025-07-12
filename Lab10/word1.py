import os 

def TP(path):
    SubDs = 0
    files = 0

    List = os.listdir(path)

    for i in List:
        Ans = os.path.join(path, i)

        if os.path.isdir(Ans):
            SubDs += 1
            print(i)

        if os.path.isfile(Ans):
            files += 1
            print(i)

    print("Total SubDs: ", SubDs)
    print("Total Files: ", files)

TP('/Users/sreekarsbs/Desktop/Lab10/Lab10')
