# Heart Disease Classification

## Project Description
The project focuses on Heart Disease data gathered from [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/dataset/45/heart+disease), from the year 1988. The data was collected from two clinics - Cleveland and VA Long Beach.

The goal of the project using the data on heart disease is to diagnose patients based on a multitude of factors. Diagnosis is classified on whether there is an absence or presence of heart disease. We also want to find out if specific factors, or features, affect the prediction score or accuracy as a comparison. 

In order to achieve this outcome, we used the following tools & platforms:
-	Python libraries (pandas, Matplotlib)
-	Machine Learning (ML) libraries (scikit-learn, Seaborn, TensorFlow)
-	PySpark
-	Tableau

## Data Extraction and Cleaning
All data used for the project was extracted from and saved into the **`Resources/`** folder. 

Using the text files `unclean_cleveland.txt` and `unclean_long_beach_va.txt`, we were able to clean data to a data frame and stack data vertically. 

Cleaned data was saved as **`full_dataset.csv`** in the folder and used in Tableau to create visualize analyses.  

Each individual cleaned dataset `cleveland.txt` and `va.txt` were extracted and stacked vertically. The new data frame was cleaned by removing unwanted columns that were either irrelevant or contained too many missing values. 

This cleaned data was saved as **`heartdisease.csv`** in the folder and used when computing and analyzing the ML models.

## Heart Disease Analysis
Using Tableau (link: https://public.tableau.com/app/profile/anna.lewis2284/viz/Project4HeartDisease_17222974244730/Story1?publish=yes), we created dynamic visualizations to further analyze heart disease.

We delved into three different visualisatons: 
- Sex vs. Age

  
![image](https://github.com/user-attachments/assets/e24a62fc-ee7d-4a67-878a-ba257802f5ec)

- Smokers vs. Diabetics

  
![image](https://github.com/user-attachments/assets/11acb635-5a2e-4c6d-b2c4-e419d9399736)

- Chest Pain vs. Overall Diagnosis

  
![image](https://github.com/user-attachments/assets/bec676a4-46f0-404e-8811-bd3ad77129b7)

## Heart Disease Classification 
- Reiterate and explain what was being classified
- Describe the models that were used
- Add reports/scores

## Conclusion
The model that provided the best accuracy in diagnosing Heart Disease is the Neural Networking Optimized model using features Cholesterol and Resting Blood Pressure. Using those two features can determine the presence and absence of heart disease the best based on the overall scores.

The model that did the best using the full dataset features would be the Support Vector Machine model, where the data is balanced and the based on the precision and recall. 

Based on the model results, linear classification models do best in diagnosing heart disease.

