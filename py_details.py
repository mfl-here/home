with open("details.txt","w") as f:
    n = int(input("Enter the number of lines: "))
    for i in range(n):
        line = input("Enter the line: ")
        f.write(line + "\n")
    f.flush()
    with open("details.txt","r") as fr:
        data = fr.read().split()
        c ={}
        k = 0
        nd = {}
        for  i in data:
            c[i] = data.count(i)
        print(c)
        keys = list(c.keys())
        v = sorted(list(c.values()),reverse = True)
        v = max(v)
        new_d = []
        for k in keys :
            if c[k] == v:
                print("Most occuring word is",k,"frequency",v)
        
           
            
