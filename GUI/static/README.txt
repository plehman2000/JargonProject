PROJECT 1 PART 3
Part a: In the data iterations, the read() function is called for templates and candidates on lines 37 and 48 respectively. 
The read() function itself is on lines 126-157. The data was stored in a class called Data that kept track of the raw data, 
the processed data, and the gesture name. Functions called getEGestures (lines 160-172) and getRandomNum (lines 174-176) 
were used to get the random instances to use for templates and candidates.

Part b: In the data iterations, the preprocess() function is called for the templates and candidates on lines 52 and 57
respectively. The preprocess() function and it's helper functions (getDistance, calculateLength, resampling, centroid, 
rotateBy, rotateToXero, ScaleToSquare, and translateToOrigin) take place on lines 179-296. The recognize() function to 
connect the templates to the candidate is called on line 58. The actual recognize function and its helper methods 
(pathDistance, distanceAtAngle, distanceAtBestAngle) take place on lines 299-368). 

Part c: The process of looping through the data takes place on lines 31-77. Templates and candidates are selected, and 
run through the recognizer.

Part d: The data is kept track of throughout part c, and is dispalyed through the writeCSV() fuction on lines 80-95. This 
function is called on line 67, and the total accuracy is added to the file afterwards on lines 75-77. 
