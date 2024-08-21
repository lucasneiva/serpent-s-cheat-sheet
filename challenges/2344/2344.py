N = int(input())

for _ in range(0, N):
    str1, str2 = input().split()
    
    for i in range(0, max(len(str1), len(str2))):
        if(i < len(str1)):
            print(str1[i], end="")
        if(i < len(str2)):
            print(str2[i], end="")

    print("")

        