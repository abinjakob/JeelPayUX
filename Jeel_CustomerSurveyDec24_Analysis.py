#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 10:59:07 2024

Analysis of JeelPay Customer Survey Dec24 Data
----------------------------------------------

The questionnaire had 10 questions with 9 quantitative and 1 qualitative questions.
This script plots relevant questions for analysis of the data. 

@author: Abin Jacob
         mail@abinjacob.com
"""

# libraries
import pandas as pd
import os.path as op
import matplotlib.pyplot as plt
import seaborn as sns

# file to load 
rootpath = '/Users/abinjacob/Documents/03. Bluematters/01. JeelPay'
filename = 'CustomerFeedbackData-Dec2024.csv'
filepath = op.join(rootpath,filename)
# load the data 
df = pd.read_csv(filepath)

# mapping questions
df['q1'] = pd.Categorical(df['q1'].map({1: 'Satisfied', 2: 'Neutral', 3: 'Dissatisfied'}), categories=["Satisfied", "Neutral", "Dissatisfied"], ordered=True)
df['q2'] = pd.Categorical(df['q2'].map({1: 'V.Easy', 2: 'Easy', 3: 'Avg', 4: 'Diff', 5: 'V.Diff'}), categories=["V.Easy", "Easy", "Avg", "Diff", "V.Diff"], ordered=True)
df['q4'] = pd.Categorical(df['q4'].map({1: 'Excellent', 2: 'Good', 3: 'Poor'}), categories=["Excellent", "Good", "Poor"], ordered=True)
df['q6a'] = pd.Categorical(df['q6a'].map({1: 'Yes', 2: 'No'}), categories=["Yes", "No"], ordered=True)
df['q7'] = pd.Categorical(df['q7'].map({1: 'Yes', 2: 'No'}), categories=["Yes", "No"], ordered=True)
df['q8'] = pd.Categorical(df['q8'].map({1: 'Definitely', 2: 'Maybe', 3: 'Never'}), categories=["Definitely", "Maybe", "Never"], ordered=True)
df['q9'] = pd.Categorical(df['q9'].map({1: '1', 2: '2', 3: '3', 4: '4', 5: '5'}), categories=["1", "2", "3", "4", "5"], ordered=True)


# color codes for bar plots (JeelPay theme)
c = ['#83C998', '#079D81', '#079D9D', '#3190A2', '#026173']

# plotting
plt.figure(figsize=(14, 10))

# plotting q1
counts = df['q1'].value_counts(sort= False)
plt.subplot(2,4,1)
plt.title('Product Satisfaction')
sns.barplot(x=counts.index, y=counts.values, palette=[c[0], c[2], c[4]])
plt.xticks(rotation=0)
plt.ylim(0,33)
plt.xlabel('')
plt.grid(True, linestyle='--', alpha=0.4)

# plotting q2
counts = df['q2'].value_counts(sort= False)
plt.subplot(2,4,2)
plt.title('Registration Process')
sns.barplot(x=counts.index, y=counts.values, palette=[c[0], c[1], c[2], c[3], c[4]])
plt.xticks(rotation=0)
plt.ylim(0,33)
plt.xlabel('')
plt.grid(True, linestyle='--', alpha=0.4)

# plotting q4
counts = df['q4'].value_counts(sort= False)
plt.subplot(2,4,3)
plt.title('Payment Experience')
sns.barplot(x=counts.index, y=counts.values, palette=[c[0], c[2], c[4]])
plt.xticks(rotation=0)
plt.ylim(0,33)
plt.xlabel('')
plt.grid(True, linestyle='--', alpha=0.4)

# plotting q6
counts = df['q6a'].value_counts(sort= False)
plt.subplot(2,4,4)
plt.title('Difficulty Using Services')
sns.barplot(x=counts.index, y=counts.values, palette=[c[0], c[2]])
plt.xticks(rotation=0)
plt.ylim(0,33)
plt.grid(True, linestyle='--', alpha=0.4)

# plotting q7
counts = df['q7'].value_counts(sort= False)
plt.subplot(2,4,5)
plt.title('Recommending JeelPay')
sns.barplot(x=counts.index, y=counts.values, palette=[c[0], c[2]])
plt.xticks(rotation=0)
plt.ylim(0,33)
plt.xlabel('')
plt.grid(True, linestyle='--', alpha=0.4)

# plotting q8
counts = df['q8'].value_counts(sort= False)
plt.subplot(2,4,6)
plt.title('Reusing JeelPay Service')
sns.barplot(x=counts.index, y=counts.values, palette=[c[0], c[2], c[4]])
plt.xticks(rotation=0)
plt.ylim(0,33)
plt.xlabel('')
plt.grid(True, linestyle='--', alpha=0.4)

# plotting q2
counts = df['q9'].value_counts(sort= False)
plt.subplot(2,4,7)
plt.title('Rate JeelPay')
sns.barplot(x=counts.index, y=counts.values, palette=[c[0], c[1], c[2], c[3], c[4]])
plt.xticks(rotation=0)
plt.ylim(0,33)
plt.xlabel('')
plt.grid(True, linestyle='--', alpha=0.4)

# save the plot as a PNG file
plt.savefig(op.join(rootpath,'CustomerFeedBackDec24.png'), dpi=300)


