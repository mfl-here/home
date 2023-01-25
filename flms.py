#flms
name_1 = input("Enter the name: ")
name_2 = input("Enter the name: ")

name_1 = name_1.lower()
name_2 = name_2.lower()

name_1 = name_1.replace(" ","")
name_2 = name_2.replace(" ","")


for i in name_1:
    for j in name_2:
        if i == j:
            name_1= name_1.replace(i,"")
            name_2 = name_2.replace(j,"")
            break
        else:
            pass
        
namef = name_1+name_2

len_ = len(namef)
#print(len_)

if len_ > 0:
    main = ["F","L","A","M","E","S"]
    while len(main) > 1:
        cut = len_%len(main)
        midx = cut-1
        if  midx >= 0:
            left = main[:midx]
            right = main[midx+1:]
            main =right+left
        else:
            main = main[:len(main)-1]
            

    print (main[0])

else:
    print("Nope")
    
