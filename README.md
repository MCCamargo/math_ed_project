In this project, we study math educational outcomes across the US, as measured by performance on SAT and ACT exams. 
We sought to use demographic data, from the US Census as well as from state departments of education, to predict math performance. Additionally, we sought to understand the effects of the COVID 19 pandemic. 
Our analysis focused on Texas, Arkansas, Illinois, and Massachusetts, which we took to be a roughly representative sample of states across the US. The time frame we were interested in is SY18-19 through SY22-23.
The repo is organized into 2 main folders, data and scripts.

The data files are organized by a common naming convention. Each contains a raw data file, obtained from a state department of education. The data folders also contain various supplemental data files generated throughout the project. Most significant are the files called, for example, IL20_Combined_Ed_Census.csv and IL20_Combined_Ed_Demographic.csv, which are the result of significant cleaning done by various scripts. 

The scripts: 
Address_Getter.ipynb is a script which merges census data at the census tract level to school SAT data. It uses Google Maps API to find location data for the schools, and then queries the census geolocation API to match these locations with census data.

The notebooks IL_Cleaner.ipynb and school_level_data_cleaning.ipynb clean this data to be useable for model prediction.
The notebook Illinois_model_training.ipynb is one of the two main notebooks in which model training happens. This notebook features many interesting plots, as well as Markdown explaining the goals at each stage. 
