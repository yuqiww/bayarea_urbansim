---
layout: page
title: Users Guide
---

*Work in Progress*

# Users Guide

---
CONTENTS
 
1. [Computing Environment](#computing-environment)
2. [Setup and Configuration](#setup-and-configuration)
3. [Input Files](#input-files)
4. [Model Exectution](#model-exectution)
5. [Output Files](#output-files)
6. [Model Schematic](#model-schematic)

---

## Computing Environment

## Setup and Configuration

## Input Files

## Model Exectution
All Bay Area UrbanSim run [modes](https://github.com/BayAreaMetro/bayarea_urbansim/blob/4166c25a798f2b8d045546e5b6cef45a5ca9fa4c/baus.py#L244) are initiated by running [baus.py](https://github.com/BayAreaMetro/bayarea_urbansim/blob/master/baus.py). [Simulation](https://github.com/BayAreaMetro/bayarea_urbansim/blob/4166c25a798f2b8d045546e5b6cef45a5ca9fa4c/baus.py#L263) is used to build forecasts. Other modes preprocesses the base year data (only done once until something is changed), estimate model parameters, debug the model, etc. 

## Output Files
Each Bay Area UrbanSim run (r#) produces output files. Some are only output at the start and/or finish of the run, but most are produced every in each 5th year of the run (yr).
* run[r#].log shows livetime run progress which includes info on scenario numbers, inputs, model execution, and performance
* run[r#]\_superdistrict_summaries\_[yr].csv contain a summary of select variables at the Super District level (n=33)
* run[r#]\_juris_summaries\_[yr].csv contain a summary of select variables at the juridictional level (n=108)
* run[r#]\_taz_summaries\_[yr].csv contain a summary of select variables at the Travel Analysis Zone level (n=1454)
* run[r#]\_baseyear\_pda_summaries\_2010.csv contain a summary at the PDA level for the START of 2010 (the other 2020 summary occurs at the end of the year 2010 and so contains one year of model forecast)




## Model Schematic
