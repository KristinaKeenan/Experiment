

def multiply(x,y):
    for header in range(11):
        if header == 0:
            print("X", "\t|",end="\t")
        else:
            print(header,end="\t")
    print("")

    for spacer in range(12):
        print("-------",end="\t")
                  
    answer = x * y
    return answer
    for i in range(1,11):
        print("")
        for j in range(1,11):
            if j == 0:
                print(row,"\t|",end="\t")
            else:
                print(i*j, end="\t|")
    print("\n\n")
            
            
            
            
        
        
        
    
        
    
        


multiply()
