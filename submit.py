# Python program to form a Spiral Matrix
# from the given Array

R = 3;
C = 3;


# Function to form the spiral matrix
def formSpiralMatrix(arr, mat):
    top = 0;
    bottom = R - 1;
    left = 0;
    right = C - 1;

    index = 0;

    while (True):

        if (left > right):
            break;

        # prtop row
        for i in range(left, right + 1):
            mat[top][i] = arr[index];
            index += 1;
        top += 1;

        if (top > bottom):
            break;

        # prright column
        for i in range(top, bottom + 1):
            mat[i][right] = arr[index];
            index += 1;
        right -= 1;

        if (left > right):
            break;

        # prbottom row
        for i in range(right, left - 1, -1):
            mat[bottom][i] = arr[index];
            index += 1;
        bottom -= 1;

        if (top > bottom):
            break;

        # prleft column
        for i in range(bottom, top - 1, -1):
            mat[i][left] = arr[index];
            index += 1;
        left += 1;


# Function to prthe spiral matrix
def printSpiralMatrix(mat):
    for i in range(R):
        for j in range(C):
            print(mat[i][j], end=" ");
        print();


# Driver code
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];

    mat = [[0 for i in range(C)] for j in range(R)];
    formSpiralMatrix(arr, mat);
    printSpiralMatrix(mat);

# This code contributed by PrinciRaj1992