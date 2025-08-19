import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

student_file=r"D:\workspace\python\Data Manipulation\Student_Performance Data Analysis\student-scores.csv"

# Read movies.csv (contains 'id', 'first_name', 'last_name','email','gender',...scores of each subject)
student_df = pd.read_csv(student_file, usecols=["id", "first_name", "last_name","email",'gender','math_score','history_score','physics_score','chemistry_score','biology_score','english_score','geography_score'])

#total_score of all subject
student_df['total_score']=student_df[['math_score','history_score','physics_score','chemistry_score','biology_score','english_score','geography_score']].sum(axis=1)

#average marks of each student
student_df['average_score'] = student_df['total_score']/7

#print(student_df)

gender_analysis=student_df.groupby('gender').agg({
    'math_score': 'mean',
    'history_score': 'mean',
    'physics_score': 'mean',
    'chemistry_score': 'mean',
    'biology_score': 'mean',
    'english_score': 'mean',
    'geography_score': 'mean',
    'total_score': 'mean',
    'average_score': 'mean'
})

np_med = np.median(student_df[['math_score','history_score','physics_score','chemistry_score','biology_score','english_score','geography_score']],axis=0)

np_std = np.std(student_df[['math_score','history_score','physics_score','chemistry_score','biology_score','english_score','geography_score']],axis=0)

np_med_total_score = np.median(student_df['total_score'])

np_std_total_score = np.std(student_df['total_score'])

print("Median Scores per Subject",np_med)
print("Standard_deviation per Subject",np_std)

print("Median of total_score",np_med_total_score)
print("Standard_deviation of total_score",np_std_total_score)

# Set up the plot size
plt.figure(figsize=(12, 6))

subjects = ['math_score', 'history_score', 'physics_score', 'chemistry_score', 
            'biology_score', 'english_score', 'geography_score']

# Melt the dataframe to get the data in the correct format for seaborn
gender_subject_avg = student_df.melt(id_vars='gender', value_vars=subjects, 
                                     var_name='subject', value_name='score')

# Create a box plot to show the distribution of scores by gender for each subject
sns.pointplot(x='subject', y='score', hue='gender', data=gender_subject_avg)

# Add titles and labels
plt.title('Distribution of Scores by Gender for Each Subject')
plt.xlabel('Subject')
plt.ylabel('Score')
plt.xticks(rotation=45)  # Rotate x-axis labels for readability

# Show the plot
plt.show()
