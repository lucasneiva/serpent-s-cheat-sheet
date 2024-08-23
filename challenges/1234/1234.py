while True:
    try:
        sentenca = input()
        stringDancante = ""
        
        ehMaiuscula = True
        for i in range(0, len(sentenca)):
            if sentenca[i] != " ":
                if ehMaiuscula:
                    stringDancante += sentenca[i].upper()
                    ehMaiuscula = False
                else:
                    stringDancante += sentenca[i].lower()
                    ehMaiuscula = True
            else:
                stringDancante += " "
                    
                
        print(stringDancante)
            
    except EOFError:
        break
    