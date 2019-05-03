# EO-Data-Search-Prototype
This is a level 1 abstraction EO query processing script where the user can provide the source, type and and location of data he/she wants to find.
For eg: A query "Find the images of Mount Everest from Sentinel 2" will give the output:
"You want: images
You want images from: Sentinel 2
You want images of: Mount Everest"

This is an unsupervised and untrained prototype and therefore works only for specific cases. 
Database: Although the script can detect the objects using NLP, it will only show successful output for the following:
satellites: Sentinel 2, TanSat, Theos, Gaofen 1, BelKA
locations: Mount Everest, Amazon, Kanchenjunga, Africa  (random locations have been taken) 
datatypes: images, photos, signals, pictures, images, records 

Note: 1. If you want to add any data, just insert the desired data name in the respective lists given in the source code. 
2. Date and Time has not been considered as it's just a rough model.
3. Might not give correct output if spelling mistakes are there. 

Requirements: 
nltk 
python version 3 or above
