def block(x): 
      
    v = [] 
      
    # Converting the decimal number 
    # into its binary equivalent. 
    print ("Blocks for %d : " %x, end="") 
    while (x > 0): 
        v.append(int(x % 2)) 
        x = int(x / 2) 
  
    # Displaying the output when 
    # the bit is '1' in binary 
    # equivalent of number. 
    for i in range(0, len(v)): 
        if (v[i] == 1): 
            print (i, end = "") 
            if (i != len(v) - 1): 
                print (", ", end = "") 
    print ("\n")
block(5)