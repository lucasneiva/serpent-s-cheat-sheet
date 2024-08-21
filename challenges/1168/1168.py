mapNumLeds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
#             0  1  2  3  4  5  6  7  8

N = int(input())

for _ in range(0, N):
    leds = input()
    numLeds = 0
    for i in range(0, len(leds)):
        numLeds += mapNumLeds[int(leds[i])]
    
    print(numLeds, "leds")