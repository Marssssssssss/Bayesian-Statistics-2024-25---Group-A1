# Bayesian-Statistics-2024-25---Group-A1
NOx Emissions Analysis with Bayesian Causal Inference
\
This project analyzes the impact of vehicle renewal policies on NOx concentrations in Lombardy using Bayesian models.
\
Models Used:
\
CausalImpact (BSTS in R): Estimates counterfactual NOx levels using Bayesian structural time-series.
\
Spatio-Temporal Bayesian Model (Stan): Incorporates spatial correlation between monitoring stations using a Gaussian Process prior.
\
Categorical Bayesian Model (Stan): Adds station type (urban, suburban, rural) to improve accuracy in spatial predictions.
\
Files:
\
Base_Model.ipynb : AR(1) implementation with only meteorological covariates
\
Model_with_categories.ipynb : AR(1) with meteorological covariates and categories URBAN / SUB-URBAN / RURAL
\
data_map.ipynb : file for visualization of EFFECT / NO EFFECT / PARTIAL EFFECT on Lombardy 
\
comparison.R : R model in wich we use CausalImpact package as a base model for performance comparison
