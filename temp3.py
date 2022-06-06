MAX = 256
 
# This function returns true if contents
# of arr1[] and arr2[] are same,
# otherwise false.
def compare(arr1, arr2):
     
    global MAX
 
    for i in range(MAX):
        if (arr1[i] != arr2[i]):
            return False
             
    return True
 
# This function search for all permutations
# of pat[] in txt[]
def search(pat, txt):
     
    M = len(pat)
    N = len(txt)
 
    # countP[]: Store count of all characters
    #           of pattern
    # countTW[]: Store count of current window
    #            of text
    countP = [0 for i in range(MAX)]
    countTW = [0 for i in range(MAX)]
 
    for i in range(M):
        countP[ord(pat[i])] += 1
        countTW[ord(txt[i])] += 1
 
    # Traverse through remaining
    # characters of pattern
    for i in range(M, N):
         
        # Compare counts of current window
        # of text with counts of pattern[]
        if (compare(countP, countTW)):
            return True
             
        # Add current character
        # to current window
        countTW[ord(txt[i])] += 1
 
        # Remove the first character
        # of previous window
        countTW[ord(txt[i - M])] -= 1
 
    # Check for the last window in text
    if(compare(countP, countTW)):
        return True
        return False
 
# Driver code
txt = "hxtcczht"
pat = "htc"
 
if (search(pat, txt)):
    print("Yes")
else:
    print("No")
 
# This code is contributed by avanitrachhadiya2155