<div align="center">

<h1>
Time Series using Deep Learning for PEMFC Degradation Prediction & RUL Estimation
</h1>

<h3>
Proton Exchange Membrane Fuel Cell (PEMFC) Prognostics using RNN, LSTM, and GRU
</h3>

<p>
Remaining Useful Life (RUL) Prediction and Fuel Cell Degradation Modeling Using Deep Learning
</p>

</div>

<hr />


<!-- Project Demo Video -->
<h2 align="center">🎥 Project Demo</h2>

<p align="center">
  <a href="https://www.youtube.com/watch?v=YOUR_VIDEO_ID">
    <img src="https://img.youtube.com/vi/YOUR_VIDEO_ID/maxresdefault.jpg"
         width="850">
  </a>
</p>

<p align="center">
Click the image above to watch the PEMFC degradation prediction and RUL estimation demo.
</p>


<hr />


<h2> Project Overview</h2>
    <p>
      Accurate Remaining Useful Life (RUL) prediction of Proton Exchange Membrane Fuel Cells (PEMFCs) is essential for predictive maintenance,
      improved durability, and reliable performance. This project develops and compares <strong>recurrent deep learning models</strong> —
      RNN, LSTM, and GRU — to forecast long-term stack voltage degradation and estimate RUL under dynamic operating conditions.
    </p>
    <p>
      The models are trained and validated using the <strong>IEEE PHM 2014 Data Challenge dataset</strong>, which contains real experimental PEMFC degradation data.
    </p>
 <hr />

<h2> Aim & Objectives</h2>
    <h3>Primary Goal</h3>
    <p>Develop robust time-series models to predict PEMFC stack voltage degradation and estimate RUL.</p>

 <h3>Objectives</h3>
    <ul>
      <li>Preprocess high-frequency PEMFC operational data and remove noise.</li>
      <li>Transform time-series data into supervised learning format.</li>
      <li>Develop RNN, GRU, and LSTM models for degradation prediction.</li>
      <li>Optimize model hyperparameters using <strong>Optuna</strong>.</li>
      <li>Benchmark against classical time-series models (ARIMA, SARIMA, Prophet).</li>
      <li>Evaluate models using RMSE and MAE.</li>
      <li>Provide insights for predictive maintenance and durability planning.</li>
    </ul>

 <hr />

<h2> Dataset</h2>
    <h3>Source</h3>
    <p>IEEE PHM 2014 Data Challenge (FCLAB Research Federation, France)</p>

 <h3>Data Description</h3>
    <p>The dataset contains measurements from two five-cell PEMFC stacks over ~7 weeks, including:</p>

<table>
      <thead>
        <tr>
          <th>Feature</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>U1–U5</td>
          <td>Individual cell voltages</td>
        </tr>
        <tr>
          <td>Utot</td>
          <td>Stack voltage</td>
        </tr>
        <tr>
          <td>I, J</td>
          <td>Current and current density</td>
        </tr>
        <tr>
          <td>Tin/Tout (H2, AIR, WAT)</td>
          <td>Inlet/outlet temperatures</td>
        </tr>
        <tr>
          <td>Pin/Pout (H2, AIR)</td>
          <td>Inlet/outlet pressures</td>
        </tr>
        <tr>
          <td>Din/Dout (H2, AIR)</td>
          <td>Inlet/outlet flow rates</td>
        </tr>
        <tr>
          <td>DWAT</td>
          <td>Cooling water flow rate</td>
        </tr>
        <tr>
          <td>HrAIRFC</td>
          <td>Air humidity</td>
        </tr>
      </tbody>
    </table>

 <hr />

<h2> Exploratory Data Analysis (EDA)</h2>
    <p>Key observations:</p>
    <ul>
      <li>Voltage distribution shows a stable operating point with gradual degradation.</li>
      <li>Degradation curve displays long-term voltage decline due to aging mechanisms.</li>
      <li>Cell voltage imbalance increases over time, indicating heterogeneous degradation.</li>
      <li>Thermal stress (ΔT) negatively impacts voltage performance.</li>
      <li>Short-term voltage volatility captures operational events and system instability.</li>
    </ul>
    <p>
      These insights justify the use of <strong>time-series deep learning models</strong> to capture both long-term trends and transient behavior.
    </p>

<hr />

<h2> Data Preprocessing</h2>
    <ol>
      <li>Resample data to <strong>hourly intervals</strong></li>
      <li>Apply <strong>Savitzky–Golay smoothing</strong></li>
      <li>Define <strong>failure threshold</strong>:
        <ul>
          <li>96% of initial stack voltage</li>
          <li>FC1 threshold = <strong>3.2028 V</strong></li>
        </ul>
      </li>
      <li>Convert time series to supervised format using <strong>1-step lag</strong></li>
      <li>Split data:
        <ul>
          <li>Train: 50%</li>
          <li>Validation: 10%</li>
          <li>Test: 40%</li>
        </ul>
      </li>
      <li>Apply <strong>Min-Max scaling</strong>
        <ul>
          <li>Scaler fit only on training data (prevents data leakage)</li>
        </ul>
      </li>
    </ol>

<hr />

<p align="center">
  <img src="../Time-Series--Deep-Learning-PEMFC-Performance-Prediction-Optimization-Degradation-Modeling/Plot/1.png" width="850">
</p>

  
<h2> Modeling & Hyperparameter Optimization</h2>

<h3>Models Used</h3>
    <ul>
      <li><strong>RNN</strong> (Baseline)</li>
      <li><strong>LSTM</strong></li>
      <li><strong>GRU</strong></li>
    </ul>

 <h3>Hyperparameter Optimization</h3>
    <ul>
      <li><strong>Optuna</strong> with Hyperband pruning</li>
      <li><strong>500 trials</strong></li>
      <li>Tuned parameters:
        <ul>
          <li>dropout rate</li>
          <li>optimizer (Adam, SGD)</li>
          <li>learning rate</li>
          <li>momentum (for SGD)</li>
        </ul>
      </li>
    </ul>

<hr />

 <h2> Classical Time-Series Benchmark Models</h2>
    <table>
      <thead>
        <tr>
          <th>Model</th>
          <th>Strength</th>
          <th>Limitation</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>ARIMA</td>
          <td>Captures global trend</td>
          <td>Weak short-term dynamics</td>
        </tr>
        <tr>
          <td>SARIMA</td>
          <td>Strong trend modeling</td>
          <td>Residual heteroskedasticity</td>
        </tr>
        <tr>
          <td>Prophet</td>
          <td>Robust to noise</td>
          <td>Underestimates end-of-life behavior</td>
        </tr>
      </tbody>
    </table>

 <hr />

<h2> Deep Learning Results</h2>

<h3>Model Performance Summary</h3>
    <table>
      <thead>
        <tr>
          <th>Model</th>
          <th>MAE</th>
          <th>RMSE</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>GRU</strong></td>
          <td><strong>0.015</strong></td>
          <td>—</td>
        </tr>
        <tr>
          <td><strong>LSTM</strong></td>
          <td>0.025</td>
          <td><strong>0.18</strong></td>
        </tr>
        <tr>
          <td><strong>RNN</strong></td>
          <td>0.045</td>
          <td>—</td>
        </tr>
      </tbody>
    </table>

<p><strong>Insight:</strong> GRU demonstrates the best performance, while LSTM provides strong robustness. Vanilla RNN shows poor long-term dependency learning.</p>

 <hr />
 
<p align="center">
<img src="Plot/5.png" width="700">
</p>

 <h2> RUL Estimation Results</h2>
    <h3>Failure Threshold</h3>
    <p><strong>3.2028 V</strong></p>

<h3>Prediction Outcome</h3>
    <ul>
      <li>The LSTM model <strong>does not predict failure within the test window</strong>.</li>
      <li>The predicted failure index lies outside the test range.</li>
      <li><strong>RUL cannot be computed</strong> within the available test data.</li>
    </ul>

 <hr />

<h2> Key Conclusions</h2>
    <ul>
      <li>Gated recurrent architectures (LSTM and GRU) outperform vanilla RNN.</li>
      <li>GRU provides the best accuracy and computational efficiency.</li>
      <li>LSTM offers stable and robust long-term prediction.</li>
      <li>Classical models serve as baselines but are insufficient for complex nonlinear degradation.</li>
      <li>RUL estimation requires longer test horizons for accurate failure detection.</li>
    </ul>

 <hr />

 <h2> Future Work</h2>
    <ul>
      <li>Integrate additional stack-level measurements to improve robustness.</li>
      <li>Develop hybrid models combining statistical and deep learning approaches.</li>
      <li>Implement online RUL estimation for real-time maintenance.</li>
      <li>Add uncertainty quantification for better decision-making.</li>
    </ul>

<hr />

<h2> Skills Demonstrated</h2>
    <ul>
      <li>Time-series forecasting and RNN architectures</li>
      <li>Hyperparameter tuning with Optuna</li>
      <li>Preventing data leakage & robust preprocessing</li>
      <li>Model benchmarking (classical vs deep learning)</li>
      <li>PEMFC domain knowledge and prognostics</li>
      <li>Evaluation using multiple metrics and insights extraction</li>
    </ul>

 <hr />
</body>
</html>
