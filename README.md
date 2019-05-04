# EO-Data-Search-Prototype
This is a level 1 abstraction EO query processing prototype script where the user can provide the source, type and and location of data he/she wants to find.
For eg: A query "Find the images of Mount Everest from Sentinel 2" will give the output:
"You want: images;
You want images from: Sentinel 2;
You want images of: Mount Everest;"

These extracted objects can then be used as queries for searching from a wide range of EO data. 
For eg, this output dara can be converted into a query as: SELECT images from database, WHERE satellite = "Sentinel 2" and location = "Mount Everest"

This is an unsupervised and untrained prototype(since no dataset is available) and therefore works only for specific cases (mainly for demonstration purposes). 
Database: Although the script can detect the objects using NLP, it will only show successful output for the following:
satellites: Sentinel 2, TanSat, Theos, Gaofen 1, BelKA
locations: Mount Everest, Amazon, Kanchenjunga, Africa  (random locations have been taken) 
datatypes: images, photos, signals, pictures, images, records 

# Note: 
1. If you want to add any data, just insert the desired data name in the respective lists given in the source code. 
2. Date and Time has not been considered as it's just a rough model.
3. Might not give correct output if spelling mistakes are there. Also, error will be thrown if datatype in the query doesn't match with the datatypes present in the database.

# Further plan (for SOCIS):
Once the training set has been provided, a suitable ML algorithm will be implemented and trained with the data provided. Each EO data will also be labelled suitably so that the extracted information(using NLP) from the query(input by the user) can further be queried within the database to show the most accurate results. Labelling of EO is important mainly for the 2nd and 3rd abstraction level. 


# Requirements: 
nltk 
python version 3 or above
