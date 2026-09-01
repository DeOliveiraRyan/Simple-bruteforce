from string import digits
from random import randint
 
senha = str(randint(00000,99999)).zfill(5)

tentativa = ""

achou = False

for i in digits:
    for j in digits:
        for k in digits:
            for l in digits:
                for m in digits:
                    print(i,j,k,l,m)

                    tentativa = i+j+k+l+m

                    if tentativa == senha:  
                        achou = True
                    if achou:
                        break
                if achou:
                    break
            if achou: 
                break
        if achou:
            break
    if achou:
        break

print("A senha é", senha)

main()
