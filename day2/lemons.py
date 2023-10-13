i=int(input())
print( ("enough") if i==21 else (i-21,"extra") if i>21 else (21-i,"less") else ("enter valid input") if(is_integer("i")!=True))                
