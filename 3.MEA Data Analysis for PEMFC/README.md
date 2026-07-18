# ⚡ PEMFC MEA Activation Data Analysis & Electrochemical Performance Intelligence

## Overview

This project presents an end-to-end **data analysis and visualization framework** for understanding 
the activation behavior of **Proton Exchange Membrane Fuel Cells (PEMFCs)**.

The objective is to analyze how operational conditions, membrane composition, and activation protocols 
influence fuel cell performance by transforming experimental electrochemical data into meaningful 
engineering insights.

The project combines:

- Electrochemical engineering
- Experimental data analysis
- Statistical investigation
- Scientific visualization
- Performance optimization

to understand the complex relationship between **Membrane Electrode Assembly (MEA) properties** 
and PEMFC output performance.


---

#  Background: The Challenge of PEM Fuel Cell Optimization

Proton Exchange Membrane Fuel Cells (PEMFCs) are promising clean energy technologies due to their:

- High efficiency
- Zero-emission operation
- Fast response characteristics
- Potential applications in transportation and stationary power generation


However, PEMFC performance depends on complex interactions between:

- Membrane properties
- Catalyst layer structure
- Gas pressure
- Humidity
- Temperature
- Activation procedures
- Electrochemical resistance


Traditional fuel cell development requires extensive experimental testing.

This project demonstrates how **data-driven analysis can accelerate PEMFC optimization** by extracting 
patterns from experimental measurements.


---

#  Dataset Description

The dataset was generated from experimental investigations performed on:

**Nafion 112 Membrane-Based PEM Fuel Cells**

The experiments investigated the impact of:

- Hydrogen and oxygen pressure
- Relative humidity
- Nafion content
- Membrane compression
- Activation strategies


The dataset contains multiple electrochemical measurements including:


## Polarization Performance Data

Measurements include:

- Current density (mA/cm²)
- Cell voltage (V)
- Power density (mW/cm²)

These measurements describe the relationship between electrical output and operating conditions.


## Electrochemical Impedance Spectroscopy (EIS)

Impedance measurements provide information about internal fuel cell behavior:

- Ohmic resistance
- Charge transfer resistance
- Electrochemical losses

Variables include:

- ZReal (Ω)
- -ZImage (Ω)


## Activation Protocol Data

Multiple MEA activation strategies were investigated:

### Cycling Potential Activation

Voltage cycling between:

Ultrasonication treatment further improved MEA activation performance.
---
<h2>Visualization Utilities</h2>

<p>
A reusable visualization module for analyzing <strong>PEM fuel cell</strong> experimental data.
The toolkit automates data loading, preprocessing, filtering, and scientific visualization,
allowing rapid comparison of electrochemical performance under different operating conditions.
The module follows a <strong>function-based modular architecture</strong>, where specialized
analysis functions reuse a common plotting engine to produce consistent scientific figures.
</p>

<h3>Key Features</h3>

<ul>
  <li><strong>Data Loading & Parsing</strong> – Import CSV datasets and convert them into NumPy arrays for analysis.</li>
  <li><strong>Data Filtering</strong> – Automatically filter experiments by voltage, pressure, relative humidity (RH), membrane compression, Nafion content, or experimental set.</li>
  <li><strong>Nyquist (EIS) Visualization</strong> – Generate impedance plots for Electrochemical Impedance Spectroscopy (EIS) analysis.</li>
  <li><strong>Polarization Analysis</strong> – Plot current density vs. cell voltage (I–V curves).</li>
  <li><strong>Power Density Analysis</strong> – Visualize current density vs. power density (I–P curves).</li>
  <li><strong>Comparative Performance Evaluation</strong> – Compare multiple operating conditions or experimental sets.</li>
  <li><strong>Reusable Plotting Engine</strong> – All visualization functions reuse <code>plot_func()</code> for consistent formatting, legends, markers, and styling.</li>
</ul>

<h3>Function Architecture</h3>

<ul>
  <li><code>load_data()</code> → Import and preprocess experimental datasets.</li>
  <li><code>format_number()</code> → Format numeric labels for plots.</li>
  <li><code>impedance_plot1()</code> → Prepare impedance data grouped by voltage.</li>
  <li><code>impedance_plot2()</code> → Filter data by RH, pressure, or voltage.</li>
  <li><code>polarization_plot1()</code> → Generate polarization and power density curves.</li>
  <li><code>polarization_plot2()</code> → Compare multiple experimental sets.</li>
  <li><code>plot_func()</code> → Shared plotting function used by all visualization modules.</li>
</ul>

<h3>Techniques</h3>

<p>
<strong>Modular Function Design</strong>, <strong>NumPy</strong>,
<strong>Boolean Indexing</strong>, <strong>CSV Data Processing</strong>,
<strong>Matplotlib</strong>, <strong>Electrochemical Impedance Spectroscopy (EIS)</strong>,
<strong>Polarization Curve Analysis</strong>, and
<strong>Scientific Data Visualization</strong>.
</p>

<h3>Example</h3>

<pre><code class="language-python">
data = load_data("data/impedance.csv")
impedance_plot2(data, V=0.7, P=25)
</code></pre>

<p>
Loads the experimental dataset, filters the measurements by voltage and pressure,
and generates a comparative Nyquist (EIS) plot.
</p>

<img src="Plot/pemfc_project_overview.gif" width="850">
<img src="Plot/pemfc_project_overview.gif" width="850">
---

#  Future Machine Learning Applications

The processed dataset provides a foundation for predictive modeling:

### Performance Prediction

Potential models:

- Random Forest Regression
- XGBoost
- Gradient Boosting
- Neural Networks


Prediction targets:

- Power density
- Voltage response
- Activation performance


### Optimization

Future optimization approaches:

- Bayesian Optimization
- Genetic Algorithms
- Particle Swarm Optimization


to identify optimal:

- Humidity
- Pressure
- Nafion content
- Activation strategy
---

#  Technology Stack

**Programming**
- Python
- NumPy
- Pandas

**Visualization**
- Matplotlib

**Domain Knowledge**
- Proton Exchange Membrane Fuel Cells (PEMFC)
- Membrane Electrode Assembly (MEA)
- Electrochemical Impedance Spectroscopy (EIS)
- Hydrogen Energy Systems


---

#  Impact

This project demonstrates how experimental electrochemical datasets can be converted into 
engineering intelligence by combining:

**Fuel Cell Experiments + Data Analysis + Visualization**

The workflow supports:

- Faster PEMFC development.
- Improved MEA activation strategies.
- Data-driven clean energy research.
- Future machine learning-based fuel cell optimization.