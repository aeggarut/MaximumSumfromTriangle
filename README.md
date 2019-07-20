# Maximum Sum from Triangle
To calculate the maximum total sum that is calculated from triangle.

According to the above purpose, there are two ways to calculate, First choice is calculating through every possible paths that is taking time in case of big triangle (e.g. 100 rows up+). Second choice, which I adopted in this script, is calculating from bottom up.

The idea is instead of calculating from the top of triangle, script calculates in bottom up direction. It compare values between two lower adjacent elements and add the maximum number to upper element. Script iterate from left to right element and from lower row to upper row. After iteration is done, the top row will contain maximum total sum.

Below triangles describe How it works,

#Step 1: Obtain triangle
          3
         2 4
       14 19 16
      7  9  4  13
    5   4  1  8   1 


#Step 2: Calculate from bottom row
          3
         2 4
       14 19 16
 --> 12 13 12 21
  
  
#Repeat step2
          3
         2 4
   --> 26 32 37

   
#repeat step2
         3
   --> 34 41

 
#Last step: obtain maximum total sum
   -->   44
   
Done!
