def print_rangoli(size):
    string=''
    weight=size*4-3
    for i in range(1,size+1):
        for j in range(i):
            string+=chr(96+size-j)
            if len(string)<weight:
                string+='-'
            
            
        for k in range(i-1,0,-1):
            string+=chr(97+size-k)
            if len(string)<weight:
                string+='-'
        print(string.center(weight,'-'))
        string=""
    for i in range(size-1,0,-1):
        for j in range(i):
            string+=chr(96+size-j)
            if len(string)<weight:
                string+='-'
            
            
        for k in range(i-1,0,-1):
            string+=chr(97+size-k)
            if len(string)<weight:
                string+='-'
        print(string.center(weight,'-'))
        string=""



        
            

print_rangoli(int(input()))