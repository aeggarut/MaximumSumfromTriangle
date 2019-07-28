# Maximum Sum from Triangle
To calculate the maximum total sum of triangle.

According to the above purpose, there are two ways to calculate, First choice is calculating through every possible paths that is taking time in case of big triangle (e.g. 100 rows up+). 

Second choice is calculating from bottom up. Instead of calculating from the top of triangle, script calculates in bottom up direction. It compare values between two lower adjacent elements and add the maximum number to upper element. Script iterate from left to right element and from lower row to upper row. After iteration is done, the top row will contain maximum total sum.

This script adopt both methods to calculate maximum total sum. In case that user want to see optimal path, first method is chosen. On the other hand, second method is chosen if user want to obtain only maximum total sum value of triangle.

> **Run: Python maximumSumfromTriangle.py <br />** 

<br />Script will show maximum sum values from three triangle, first value from example triangle and remaining values from triangle1.txt and triangle2.txt, respectively.
