# Data Science Tutorial

## General

- If you have poor results when evaluating your model it's useful to try to
  gather more data or re-engineer your data to make it more valuable before you
  rework your model

- Continuous data & Categorical data (enumerative data)

## Four skills

- Domain Expertise
- Programming
- Storytelling
- Stats

# CrISPDM Cross-Industry standard process for data mining

1. Business Objective
2. Data Acquisition
3. Data analysis and prep
4. Model
5. Evaluation
6. Implementation

## ML

### Taxonomy of types

Unsupervised
    - data is not labeled
    - task is to group data together

Supervised
    - data is labeled
    - task is basically to learn those labels, e.g. prediction
    - Regression tasks deal with continuous examples and labels
    - Classicifation tasks deal with discrete examples and labels

# Practical

## Predicting customer churn

Goal: Identify which customers are likely to leave you in the near future so
that you can intervene.

## Useful pandas methods

- `DataFrame#corr` the cross correlation of the matrix
- `DataFrame#value_counts`
- `Series#nunique`
- `Series#sort_values`
