# Task 1
task1_data_collection.py is the python file which pulls the data from api and gathered it in trends.json file(100 stories are collected)

Using 3 different functions in the python file

> get_ids()

> get_story(item_id) - passing the ids taken from get_ids function

> categorize(title) - using the title here to categorise each story

# Task 2
task2_data_processing.py is the python file which reads the data from trends.json and cleaning up the data using pandas. After clean up it saves the data as trends_clean.csv 

# Task 3
task3_analysis.py is the python file which reads the csv file from the task 2 and performing some analysis and saving it again in one more csv file namely trends_analysed.csv

# Task 4
task4_visualization.py is the python file where it visualisizes the data collected in task 3. 3 different charts and a single dashboard which contains all the charts will be displayed under output folder.
