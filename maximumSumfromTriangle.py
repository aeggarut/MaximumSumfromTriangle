# The purpose of this script is to calculate the maximum total sum that is calculated from optimal path.
# The optimal path must be formed from adjacent elements from the bottom row to the top row of triangle.

# The input of this software is sysmetrical triangle that has the same sizes of width and height.
# The output is the maximum total sum.



def main():
    exTriangle=[[3,0,0,0,0],[2,4,0,0,0],[14,19,16,0,0],[7,9,4,13,0],[5,4,1,8,1]]
    print('First, ensure that algorithm works with example triangle as question emphasize and result must be 44.')
    print('Result from example triangle is : '+str(calculateMaxPath(exTriangle)))
    print('')

    print('Then try with triangle from triangle1.txt')
    print('Result from example triangle 1 is : '+str(calculateMaxPath(fileToTriangle('triangle1.txt'))))
    print('')

    print('Then try with bigger triangle from triangle2.txt')
    print('Result from example triangle 2 is : '+str(calculateMaxPath(fileToTriangle('triangle2.txt'))))


def fileToTriangle(filename):
    triangle = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            numbers = [int(n) for n in line.replace('\n','').split(' ')]
            triangle.append(numbers)
    return triangle


def calculateMaxPath(triangle):
    
    # iterate each element in traingle from the lower row to upper row 
    # to identify its lower adjacent element that contains the maximum number.
    # then add the maximum number to it
    # after loop is done, the top left element contains the maximum total sum.
    
    for row in range((len(triangle)-2), -1, -1): 
        for col in range(row+1): 
  
            #Compare values between two lower adjacent elements and add the maximum number to it.
            if (triangle[row+1][col] > triangle[row+1][col+1]): 
                triangle[row][col] += triangle[row+1][col] 
            else: 
                triangle[row][col] += triangle[row+1][col+1] 
  
    # return the top left element that contains maximum sum.
    return triangle[0][0] 


if __name__ == "__main__":
    main()


