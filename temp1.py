def solve(D, N, X, Y): 
  
    # Stores the time at which  
    # points reach the origin 
    T = []  
          
    # Calculate time for each point 
    for i in range(N): 
  
        x = D[i][0]  
        y = D[i][1] 
  
        speed = D[i][2] 
  
        time = ((x * x - X * X) +
                (y * y - Y * Y)) / (speed * speed)  
                  
  
        T.append(time) 
          
    # Sort the times 
    T.sort() 
      
    i = 0
    total = 0
          
  
    # Counting total collisions 
    while i<len(T)-1: 
          
        # Count of elements arriving at 
        # a given point at the same time 
        count = 1
  
        while i<len(T)-1 and T[i] == T[i + 1]: 
            count += 1
            i+= 1
          
        total+= (count*(count-1))/2
        i+= 1
  
    return total 
  
# Driver Code 
  
N = 2
# Given set of points with speed 
# D = [[5, 12, 1], [16, 63, 5], \
#     [-10, 24, 1], [7, 24, 1], \
#     [-24, 7, 2]]
#

D = [[-1, 0, 1], [1, 0, 1]]
X = 0
Y = 0
  
# Function Call 
print(solve(D, N, X, Y)) 