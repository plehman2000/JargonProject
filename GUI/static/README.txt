The following four components are composed of:
a)Store the Points: Line 154 has the list tbat stores the gesture points. Line 156 has the function (storePoint) that store said points. This function is called within the draw function as a reaction to moving the mouse.

b)Store some Templates: Lines 22-29 compose the Template class. Lines 32-97 contains the instantiation of the given templates. Lines 101 and 102 preprocesses the template data (uses function preprocess).

c)Implement $1 Algorithm: Lines 161-345 (including functions getDistance, calculateLength, resampling, centroid, rotateBy, rotateToZero, ScaleToSquare, translateToOrigin, recognize, pathDistance, distanceAtAngle and distanceAtBestAngle) implements the 1$ algorithm.   

d)Output the Result: Function recognize returns the string result, and lines 128-131 in the mouseUp function displays the result to the screen.