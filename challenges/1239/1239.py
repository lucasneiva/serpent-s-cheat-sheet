while True:
    try:
        texto = input("")
        html = ""
        isIOpen = False
        isBOpen = False
        for i in range(0, len(texto)):
                if(texto[i] == "_"):
                    if(isIOpen):
                        html += "</i>"
                        isIOpen = False
                    else:
                        html += "<i>"
                        isIOpen = True
                        
                elif (texto[i] == "*"):
                    if(isBOpen):
                        html += "</b>"
                        isBOpen = False
                    else:
                        html += "<b>"
                        isBOpen = True
                
                else:
                    html += texto[i]
            
    
        print(html)
    
    except EOFError:
        break


        