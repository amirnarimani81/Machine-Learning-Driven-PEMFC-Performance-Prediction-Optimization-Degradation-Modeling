<div align="center">

<h1>
Machine Learning-Driven PEMFC Performance Prediction, Optimization & Degradation Modeling
</h1>

<h3>
Electrochemical Engineering | MEA Characterization | Performance Prediction | Fuel Cell Durability Analysis
</h3>

<p>
A collection of three interconnected projects focused on understanding, optimizing, and predicting 
Proton Exchange Membrane Fuel Cell (PEMFC) behavior using experimental data analysis, statistical modeling, 
and machine learning approaches.
</p>

</div>

<hr>


<h2 align="center">🎥 Project Overview</h2>

<p align="center">
<img src="Plot/pemfc_project_overview.gif" width="850">
</p>

<p align="center">
  <img src="Plot/4.png" width="850" alt="PEMFC Performance Prediction Results">
</p>

<hr>


# Overview

Proton Exchange Membrane Fuel Cells (PEMFCs) are promising technologies for clean hydrogen energy conversion.
However, improving PEMFC performance and durability requires a deep understanding of the complex interaction between:

- Membrane Electrode Assembly (MEA) properties
- Catalyst characteristics
- Operating conditions
- Electrochemical losses
- Long-term degradation mechanisms


This repository presents my work on three major projects for PEMFC development:


**1. Understanding MEA behavior through experimental electrochemical data analysis**

**2. Predicting and optimizing fuel cell performance using Machine learning-driven models**

**3. Modeling degradation behavior and estimating fuel cell lifetime using Deep leaning, time series (ARIMAM, SARIMA, GRU,,+ RNN, LSTM)**


The projects represent different stages of PEMFC engineering development, from laboratory characterization 
to predictive modeling.


<hr>


# Project 1  
# PEMFC MEA Activation Data Analysis & Electrochemical Performance Intelligence


## Objective

The objective of this project was to analyze experimental PEMFC data and understand how operating conditions 
and MEA activation strategies influence fuel cell performance.


## Experimental Analysis

The study focused on Nafion 112 membrane-based PEM fuel cells and investigated the effects of:

- Hydrogen and oxygen pressure
- Relative humidity
- Nafion content
- Membrane compression
- MEA activation protocols
<h2>Analysis & Visualization Framework</h2>

<p>
This project includes a reusable Python framework for analyzing <strong>PEM fuel cell (PEMFC)</strong> electrochemical datasets. The framework automates data loading, preprocessing, filtering, and scientific visualization to evaluate fuel cell performance under different operating conditions and MEA activation strategies. Built using a <strong>modular function-based architecture</strong>, specialized analysis functions reuse a common plotting engine to generate consistent, publication-quality scientific figures.
</p>

<h3>Capabilities</h3>

<ul>
  <li><strong>Experimental Data Processing</strong> – Import and preprocess PEMFC experimental datasets.</li>
  <li><strong>Operating Condition Filtering</strong> – Analyze data by voltage, pressure, relative humidity (RH), membrane compression, Nafion content, and activation set.</li>
  <li><strong>Polarization Analysis</strong> – Generate current density–voltage (I–V) and power density (I–P) curves.</li>
  <li><strong>Electrochemical Impedance Spectroscopy (EIS)</strong> – Produce comparative Nyquist plots for impedance analysis.</li>
  <li><strong>Performance Comparison</strong> – Compare multiple operating conditions and activation protocols.</li>
  <li><strong>Reusable Visualization Engine</strong> – Modular plotting functions provide consistent formatting, legends, markers, and publication-quality figures.</li>
  <li><strong>Workflow Automation</strong> – Developed Python-based functional analysis tools to automate electrochemical data processing, reducing manual analysis and accelerating MEA performance evaluation.</li>
</ul>

<h3>Function Architecture</h3>

<ul>
  <li><code>load_data()</code> → Load and preprocess experimental datasets.</li>
  <li><code>format_number()</code> → Format numerical labels for figures.</li>
  <li><code>plot_func()</code> → Shared visualization engine for all plots.</li>
  <li><code>impedance_plot1()</code> → Generate Nyquist plots grouped by voltage.</li>
  <li><code>impedance_plot2()</code> → Compare impedance curves under different RH, pressure, or voltage conditions.</li>
  <li><code>polarization_plot1()</code> → Plot polarization and power density curves.</li>
  <li><code>polarization_plot2()</code> → Compare polarization performance across multiple experimental sets.</li>
</ul>

<h3>Techniques</h3>

<p>
<strong>Python</strong>,
<strong>NumPy</strong>,
<strong>Matplotlib</strong>,
<strong>Scientific Data Visualization</strong>,
<strong>Boolean Indexing</strong>,
<strong>CSV Data Processing</strong>,
<strong>Electrochemical Impedance Spectroscopy (EIS)</strong>,
<strong>Polarization Curve Analysis</strong>, and
<strong>Modular Function Design</strong>.
</p>

<h3>Example</h3>

<pre><code class="language-python">
data = load_data("data/impedance.csv")
impedance_plot2(data, V=0.7, P=25)
</code></pre>

<p>
Loads the experimental dataset, filters measurements by voltage and pressure,
and automatically generates a comparative Nyquist (EIS) plot.
</p>

<p align="center">
  <img src="Plot/6.png" width="850">
</p>

<p align="center">
  <img src="Plot/7.png" width="850" >
</p>


# Project 2  
# Ensemble Machine Learning-Based PEM Fuel Cell Performance Prediction & MEA Optimization

<p align="center">
  <img src="Plot/1.png" width="850" >
</p>


## Objective

The goal of this project was to develop predictive models for estimating PEMFC performance based on 
material properties, catalyst characteristics, and MEA fabrication parameters.


## Dataset

The dataset contained:

- 799 experimental records
- 66 input features
- Data collected from approximately 800 scientific publications


The dataset included:

### Catalyst Properties

- Pt loading
- Alloy composition
- Carbon support
- Particle characteristics


### Synthesis Conditions

- Reduction temperature
- Reaction time
- Annealing conditions


### MEA Parameters

- Membrane properties
- Ionomer ratio
- Fabrication conditions


## Modeling Approach

Developed regression models including:

- Linear Regression
- Random Forest
- Gradient Boosting
- XGBoost
- CatBoost
- Ensemble regression models


## Results

Best-performing model:

**XGBoost Regression**

| Metric | Result |
|---|---|
| R² Score | 0.9852 |
| RMSE | 48.24 mW/cm² |


## Contribution

The model identified important factors controlling PEMFC performance and demonstrated how data-driven 
approaches can reduce experimental trial-and-error during MEA development.

<p align="center">
  <img src="Plot/2.png" width="850" >
</p>

<hr>


# Project 3  
# Deep Learning Models for PEMFC Degradation Prediction & Remaining Useful Life (RUL) Estimation

<p align="center">
  <img src="Plot/5.png" width="850" >
</p>

## Objective

The objective of this project was to analyze PEMFC aging behavior and predict future degradation trends 
for durability assessment and maintenance planning.


## Dataset

Used the IEEE PHM 2014 Fuel Cell Data Challenge dataset containing:

- Five-cell PEMFC stack measurements
- Cell voltages
- Stack voltage
- Temperature
- Pressure
- Flow rates
- Humidity


## Data Processing

Performed:

- Time-series preprocessing
- Noise reduction
- Feature preparation
- Sequence generation
- Data normalization


## Modeling Approach

Developed and compared:

- Recurrent Neural Network (RNN)
- Long Short-Term Memory (LSTM)
- Gated Recurrent Unit (GRU)


## Results

| Model | MAE | RMSE |
|---|---|---|
| GRU | 0.015 | - |
| LSTM | 0.025 | 1.26×10⁻³ |
| RNN | 0.045 | - |


## Contribution

This project demonstrated the capability of deep learning models to capture nonlinear PEMFC degradation 
patterns and support durability analysis.


<hr>


# Overall Engineering Workflow



These projects cover the complete PEMFC development cycle:

| Area | Focus |
|---|---|
| Electrochemical Analysis | Understanding MEA behavior |
| Performance Modeling | Predicting fuel cell output |
| Durability Modeling | Predicting degradation and lifetime |


<hr>


# Technical Skills Demonstrated

## Electrochemical Engineering

- PEM Fuel Cells
- Membrane Electrode Assembly (MEA)
- Electrochemical Impedance Spectroscopy (EIS)
- Polarization curve analysis
- Fuel cell degradation mechanisms


## Data Analysis & Modeling

- Python
- Pandas
- NumPy
- Statistical analysis
- Data visualization


## Machine Learning

- Regression modeling
- Ensemble learning
- Feature analysis
- Model evaluation


## Deep Learning

- Time-series modeling
- RNN
- LSTM
- GRU


<hr>


# Engineering Impact

This portfolio demonstrates how experimental fuel cell data can be transformed into practical engineering 
knowledge for:

- Improving MEA design
- Optimizing PEMFC performance
- Understanding degradation mechanisms
- Supporting future hydrogen energy systems


<div align="center">

<h2>
Electrochemical Engineering Powered by Data-Driven Analysis
</h2>

</div>
