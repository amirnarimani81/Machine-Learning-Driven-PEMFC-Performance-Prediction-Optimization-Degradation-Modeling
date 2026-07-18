<h1 align="center">
Ensemble Machine Learning-Based PEM Fuel Cell Performance Prediction & MEA Optimization
</h1>

<h3 align="center">
Data-Centric Regression Framework for Predicting Maximum Power Density (MPD) in PEMFCs
</h3>

<p align="center">
  <img src="Plot/1.png" width="850">
</p>

## Overview

Designing high-performance **Membrane Electrode Assemblies (MEAs)** for 
**Proton Exchange Membrane Fuel Cells (PEMFCs)** traditionally relies on expensive and 
time-consuming experimental trial-and-error.

The objective is to replace traditional trial-and-error experimental approaches with
data-driven models capable of:

- Predicting fuel cell performance metrics such as maximum power density (MPD).
- Identifying critical catalyst and MEA design parameters.
- Understanding relationships between material properties and electrochemical performance.
- Supporting accelerated catalyst and MEA development.

Fuel cell development involves complex interactions between catalyst materials, synthesis
methods, electrode structures, and operating conditions. Machine learning provides a pathway
to extract hidden patterns from large experimental datasets and guide future material design.

---

#  Dataset Description

The dataset contains detailed information on **PEMFC catalysts and fuel cell performance**
collected from approximately **800 scientific articles** published between **2003 and 2020**
across multiple countries.

The dataset integrates information from catalyst synthesis, material characterization,
MEA fabrication, and electrochemical performance evaluation.

The final dataset contains:

- **799 experimental records**
- **66 initial features**
- Catalyst, synthesis, structural, MEA, and performance parameters


# Feature Categories

## Catalyst Composition
Material composition features include:
- Atomic percentages of Pt, Pd, Au, Ir, Ru, Ni, Co, and Fe.
- Metal loading values.
- Carbon support materials such as:
  - Carbon nanotubes (CNTs)
  - Graphene
  - Vulcan XC-72R


## Synthesis Parameters
Experimental synthesis conditions include:
- Reduction temperature and reaction time.
- Reducing agents:
  - NaBH₄
  - Ethylene glycol (EG)
  - Formic acid
- Annealing temperature and duration.
- Heating techniques:
  - Microwave-assisted synthesis.
  - Conventional heating.


## Structural Features
Material characterization information includes:
- Catalyst particle size.
- Nanostructure morphology:
  - Core-shell structures.
  - Nanowires.
  - Nanocages.
  - Alloy nanoparticles.
- BET surface area measurements.


## Electrochemical Performance Metrics
Target performance variables include:
- Electrochemical surface area (ECSA).
- Mass activity.
- Specific activity.
- Half-wave potential.
- Onset potential.
- Maximum power density (MPD):

  **~100 to more than 2000 mW/cm²**

- Voltage-current (V-I) polarization curves.


## MEA Fabrication Parameters
Fuel cell assembly parameters include:
- Ionomer-to-catalyst ratio.
- Membrane type and thickness.
- Hot pressing temperature and pressure.
- MEA fabrication conditions.


---

#  Machine Learning Objectives
The project aims to:

- Predict PEMFC maximum power density.
- Identify the most influential design parameters.
- Discover hidden relationships between material properties and performance.
- Develop a reproducible ML workflow for MEA optimization.


---

#  Data Science Workflow
## 1. Data Preprocessing

The data preparation pipeline included:

- Dataset cleaning and quality assessment.
- Missing value imputation.
- Encoding categorical variables.
- Feature normalization.
- Outlier detection and treatment.
- Feature correlation analysis.



## 2. Exploratory Data Analysis (EDA)

Performed analysis to understand relationships between catalyst properties and fuel cell performance:

- Catalyst composition distribution analysis.
- Performance comparison between catalyst families.
- Correlation analysis between synthesis parameters and MPD.
- Identification of important performance-driving features.


Examples of investigated relationships:

- Pt alloy composition vs catalytic activity.
- Carbon support type vs power density.
- Particle size vs electrochemical performance.
- Synthesis conditions vs catalyst efficiency.


## 3. Feature Engineering

Feature engineering approaches included:

- Removing irrelevant or redundant variables.
- Applying PCA for dimensionality reduction.
- Transforming highly skewed variables.
- Selecting important physical parameters.
- Creating optimized feature sets for regression modeling.


The goal was to improve prediction accuracy while maintaining scientific interpretability.


---

#  Machine Learning Model Development

Multiple regression algorithms were developed and compared.


## Baseline Models

| Model | Purpose |
|---|---|
| Linear Regression | Baseline performance |
| Decision Tree | Nonlinear relationship modeling |


## Ensemble Models

| Model | Purpose |
|---|---|
| Random Forest | Reduce variance and improve robustness |
| Gradient Boosting | Sequential error correction |
| XGBoost | High-performance nonlinear regression |
| CatBoost | Handle categorical material features |
| Voting Ensemble | Improve prediction stability |



## Stacking Regression

Multiple regression models are combined using a meta-model.
The stacking framework allows the final predictor to learn from the strengths of individual models.

Benefits:
- Improved generalization.
- Reduced prediction error.
- Better modeling of complex catalyst-performance relationships.


## Voting Regression
Predictions from multiple optimized models are combined through weighted averaging.

Advantages:
- Reduced model variance.
- More stable predictions.
- Improved reliability for experimental datasets.


---

#  Hyperparameter Optimization
The modeling workflow included:

- 5-fold cross-validation.
- Hyperparameter tuning.
- GridSearchCV optimization.
- Ensemble comparison.


Optimized parameters included:
- Learning rate.
- Tree depth.
- Number of estimators.
- Regularization parameters.

 <img src="Plot/2.png" width="850">
---

#  Model Performance

## Best Model: XGBoost Regression

Performance:

| Metric | Result |
|---|---|
| R² Score | **0.9852** |
| RMSE | **48.24 mW/cm²** |


The optimized XGBoost model successfully captured complex nonlinear relationships between:

- Catalyst design.
- MEA parameters.
- Operating conditions.
- Fuel cell performance.


---

# Potential Applications


## Performance Prediction

Predict:

- Maximum power density.
- Mass activity.
- Half-wave potential.

from catalyst composition and synthesis parameters.


## Material Optimization

Investigate:

- Alloy composition effects.
- Carbon support influence.
- Catalyst structure-performance relationships.


## Comparative Analysis

Compare:

- Core-shell catalysts vs alloy catalysts.
- Different synthesis techniques.
- Different catalyst families.


## Process Optimization

Identify optimal:

- Reduction temperatures.
- Reaction times.
- Annealing conditions.
- Catalyst compositions.



---

# Engineering Impact

This machine learning framework demonstrates how data science can accelerate PEMFC research by:

- Reducing experimental trial-and-error.
- Identifying critical catalyst design factors.
- Accelerating clean energy material discovery.
- Supporting future optimization algorithms:
  - Genetic Algorithms (GA)
  - Particle Swarm Optimization (PSO)


This project integrates:
**Electrochemical Engineering + Materials Science + Machine Learning + Data Analytics**
to accelerate next-generation hydrogen energy technologies.


---

#  Technology Stack

## Programming
- Python
- Pandas
- NumPy


## Machine Learning
- Scikit-learn
- XGBoost
- CatBoost
- LightGBM


## Data Analysis & Visualization
- Matplotlib
- Seaborn


## Optimization
- GridSearchCV
- Ensemble Learning


## Domain

- Proton Exchange Membrane Fuel Cells (PEMFC)
- Membrane Electrode Assembly (MEA)
- Catalyst Design
- Hydrogen Energy Systems