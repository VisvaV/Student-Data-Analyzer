# data_processing.py

import pandas as pd
import numpy as np

def process_data(filepath, fig):
    # Read data
    data = pd.read_csv(filepath)

    # Perform calculations
    data['Total Marks'] = data['Cont Asses 1'] + data['Cont Asses 2'] + data['Tutorial Marks']
    data['Attendance Percentage'] = (data['Student Attendance'] / 30) * 100
    data['Remarks'] = np.where(data['Total Marks'] >= 40, 'Pass', 'Fail')

    # Group data by subject and calculate total marks for each subject
    subject_marks = data.groupby('Subject')['Total Marks'].sum()

    # Generate pie chart for marks distribution across subjects
    ax1 = fig.add_subplot(121)
    subject_marks.plot(kind='pie', autopct='%1.1f%%', ax=ax1, colors=['skyblue', 'lightgreen', 'lightcoral', 'lightsalmon'])
    ax1.set_title('Marks Distribution by Subject')
    ax1.set_ylabel('')  # Remove y-label

    # Generate histogram for total marks distribution
    ax2 = fig.add_subplot(122)
    bins = np.arange(0, 101, 10)  # Define bins for histogram
    ax2.hist(data['Total Marks'], bins=bins, color='lightblue', edgecolor='black')
    ax2.set_title('Total Marks Distribution')
    ax2.set_xlabel('Total Marks')
    ax2.set_ylabel('Frequency')

    # Add annotations to the histogram bars
    for i, bin in enumerate(bins[:-1]):
        bin_center = (bin + bins[i+1]) / 2  # Calculate the center of the bin
        bin_count = ((data['Total Marks'] >= bin) & (data['Total Marks'] < bins[i+1])).sum()  # Count the number of students in the bin
        ax2.text(bin_center, bin_count, f'{bin_count}\n{bin}-{bins[i+1]}', ha='center', va='bottom')

    # Add grid to histogram
    ax2.grid(True, linestyle='--', alpha=0.7)

def display_student_stats(filepath, roll_no):
    # Read data
    data = pd.read_csv(filepath)

    # Filter data for the given student roll number
    student_data = data[data['Roll No'] == roll_no]
    student_stats = student_data.describe()
    student_stats = student_stats.drop('std')
    # Return student statistics as DataFrame
    return student_stats

def display_teacher_stats(filepath, teacher_name):
    # Read data
    data = pd.read_csv(filepath)

    # Filter data for the given teacher's name
    teacher_data = data[data["Teacher's Name"].str.lower() == teacher_name.lower()]

    if not teacher_data.empty:
        # Calculate total marks for teacher's data
        return teacher_data.describe()
        #total_marks = teacher_data["Total Marks"].sum()

        # Return total marks for teacher
        #return f"Total marks for {teacher_name}: {total_marks}"
    #else:
     #   return f"No data found for teacher {teacher_name}"
