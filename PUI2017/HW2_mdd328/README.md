PUI2017 HW 2
Matt Dwyer

The first assignment in Homework 2 involved using an API key to access MTA bus time data through a url. The code was a python script that accessed the URL and downloaded the JSON format data and mapped it to a python dictionary. The rest of the code parsed through the bus data to pull out data on a given bus line, returning the number of vehicles and each vehicle's location. I worked with Prince, Charlie, Sarah, and Jack to figure out the beginning URL that accessed the MTA website. 

The second assignment was similar to the first, except instead of the script returning the bus information to the terminal, it wrote the data into a csv file. The data pulled from the MTA website was still bus line specific, but instead returned the location, current stop name, and current stop status of each bus on the line. Aside from occasionally asking for pointers, I worked on this section alone. 

The third assignment was in a jupyter notebook, and involved pulling a csv file from the CUSP data facility using an environmental variable to access the facility's location. The dataframe downloaded was then reduced and plotted. I worked on this section alone. 

The extra credit assignment was similar to the third assignment except the csv file I used had a date and time column, which made plotting the data more difficult. I worked with Kent and Matt to figure out how to plot the data set, with Kent showing me how to convert the date time column into a legible format. 