while True:
    try:
        tag = input()
        valor = input()
        linha = input()
        nvLinha = ""
        ehDentro = False
        
        i = 0
        while i < len(linha):
            if linha[i] == "<":
                ehDentro = True
            elif linha[i] == ">":
                ehDentro = False
            
            if i < len(linha)-len(tag) and ehDentro and (linha[i:i+len(tag)]).upper() == tag.upper():
                nvLinha += valor
                i += len(tag)-1
                
            else:
                nvLinha += linha[i]
                
            i+=1
        print(nvLinha)
    except EOFError:
        break    
    
    