In this project, we study math educational outcomes across the US, as measured by performance on SAT and ACT exams. 
We sought to use demographic data, from the US Census as well as from state departments of education, to predict math performance. Additionally, we sought to understand the effects of the COVID 19 pandemic. 
Our analysis focused on Texas, Arkansas, Illinois, and Massachusetts, which we took to be a roughly representative sample of states across the US. The time frame we were interested in is SY18-19 through SY22-23.
The repo is organized into 2 main folders, data and scripts.

The data files are organized by a common naming convention. Each contains a raw data file, obtained from a state department of education. The data folders also contain various supplemental data files generated throughout the project. Most significant are the files called, for example, IL20_Combined_Ed_Census.csv and IL20_Combined_Ed_Demographic.csv, which are the result of significant cleaning done by various scripts. 

The scripts: 
Address_Getter.ipynb is a script which merges census data at the census tract level to school SAT/ACT data. It uses Google Maps API to find location data for the schools, and then queries the census geolocation API to match these locations with census data.

The notebooks IL_Cleaner.ipynb and school_level_data_cleaning_AR_and_MA.ipynb clean this data to be useable for model prediction, for the states of Massachusetts, Arkansas and Illinois.

The notebook model_training_on_school_level_data_AR_and_MA.ipynb focuses on the problem of predicting, for each state (MA and AR) and year, the outcomes of SAT/ACT Math tests, using as features demographic data at the school level which was cleaned previously using school_level_data_cleaning_AR_and_MA.ipynb. In this notebook, we train linear regression and XGBoost models, and use them to understand which features in our data are most predictive.

The notebook inter_year_comparison_visualization_AR_and_MA.ipynb focuses on visualizing score changes in ACT/SAT Math tests in the period 2019 - 2023, for schools located in Arkansas and Massachusetts.

The notebook inter_year_comparison_models_AR_and_MA.ipynb is where we attempt to train models that predict score changes in ACT/SAT math tests in the period 2019 - 2023 for AR and MA schools. We find that neither linear nor non-linear models we train are able to adequately predict these score changes with the features that are available to us in these states (in particular, they have a performance comparable or worse than that of the baseline model which always guesses the average target value for the training set). 

The notebook Illinois_model_training.ipynb is one of the other main notebooks in which model training happens, both for predicting SAT/ACT performance in a single year as well as performance changes over time, for the state of Illinois. This notebook features many interesting plots, as well as Markdown explaining the goals at each stage. 

