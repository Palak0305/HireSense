# HireSense

## AI-Powered Job Category Prediction System

HireSense is a Machine Learning project that predicts the most relevant technology job category from job skills and job descriptions.

The project combines Natural Language Processing (NLP) and Machine Learning to analyze job-related text and classify it into different technology job categories.

## Project Overview

Technology job postings contain a large amount of information about required skills, responsibilities, and technical requirements.

HireSense aims to automate job category identification using:

- Technical skills
- Job descriptions
- TF-IDF text representation
- Linear Support Vector Machine (SVM)

The final model predicts one of 13 technology job categories.

## Key Features

- Job category prediction from technical skills
- Job description-based classification
- Top 3 model category matches
- NLP-based text processing
- TF-IDF feature extraction
- Machine Learning classification
- Interactive Streamlit web application

## Dataset

The dataset contains:

- 9,380 job postings
- 3,870 unique job titles
- 13 technology job categories

The dataset includes information such as:

- Job title
- Company
- Job location
- Job level
- Job type
- Job summary
- Job skills
- Job category

## Machine Learning Approach

### 1. Data Preprocessing

Job skills were converted into text format so that they could be processed using NLP techniques.

Job skills and job descriptions were then combined to provide the model with both technical and contextual information.

### 2. Feature Extraction

TF-IDF (Term Frequency-Inverse Document Frequency) was used to convert text into numerical features.

The final TF-IDF representation used:

- Maximum 3,000 features
- Unigrams and bigrams

### 3. Model

A Linear Support Vector Machine (Linear SVM) was trained for multi-class classification.

Class balancing was used during training because the dataset contains significant differences in category sizes.

## Model Performance

The final model was evaluated on a held-out test set.

| Metric | Score |
|---|---:|
| Accuracy | 89.39% |
| Macro F1 | 0.558 |
| Weighted F1 | 0.894 |

Accuracy represents the overall percentage of correctly classified test examples.

Macro F1 is also reported because the dataset contains imbalanced job categories.

## Technology Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- TF-IDF
- Linear SVM
- Joblib
- Streamlit

## Project Structure

```text
HireSense/
│
├── HireSense.ipynb
├── app.py
├── hiresense_combined_svm.pkl
├── hiresense_combined_tfidf.pkl
└── README.md
