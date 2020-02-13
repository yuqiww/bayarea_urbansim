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
Bay Area UrbanSim (BAUS) is written in python and has been run using MacOS, Windows, and Linux operating systems. The code (except for the pandana sub-model) is single-threaded. The current model generally requires around 20G of memory. 

## Setup and Configuration
BAUS is 


## Input Files
Input files are all in text (csv or yaml) format stored in three locations:
* Most input data files are csv files in the [/data](https://github.com/BayAreaMetro/bayarea_urbansim/tree/master/data) directory.
* Several larger csv files are stored on [Box](https://mtcdrive.box.com/s/3cr52b8ccx1l1e59l1zvrud6srmsg0yc) because their large size is doesn't work well with GitHub.
* Various settings are contained in yaml files in the [/configs](https://github.com/BayAreaMetro/bayarea_urbansim/tree/master/configs) folder.

## Model Exectution
All Bay Area UrbanSim run [modes](https://github.com/BayAreaMetro/bayarea_urbansim/blob/4166c25a798f2b8d045546e5b6cef45a5ca9fa4c/baus.py#L244) are initiated by running [baus.py](https://github.com/BayAreaMetro/bayarea_urbansim/blob/master/baus.py). [Simulation](https://github.com/BayAreaMetro/bayarea_urbansim/blob/4166c25a798f2b8d045546e5b6cef45a5ca9fa4c/baus.py#L263) is used to build forecasts. Other modes preprocesses the base year data (only done once until something is changed), estimate model parameters, debug the model, etc. The scenario number can also be specified at run time using "-s 4" etc. Various other settings are covered in baus.py incliuding: log creations; output formatting; and automatic output notifications (slack and maps).

### Simulation Mode
Simulation mode is used to build forecasts or "run UrbanSim", is the most common mode in daily use, and is the default mode when running baus.py. Simulations in BAUS consist of a list of steps that are exececuted in order for each forecast time period. Other simulation options in baus.py include: setting the time period (e.g., 5-year stepos); setting the start and end years; optionally skipping the first year (otherwise the model forecasts an "end of the base year" forecast which is different from the base year); whether a random seed is used for probability calculations; and what historic runs the current run is compared with. 

## Output Files
Each Bay Area UrbanSim run (r#) produces output files. Some are only output at the start and/or finish of the run, but most are produced every in each 5th year of the run (yr).
* run[r#].log shows livetime run progress which includes info on scenario numbers, inputs, model execution, and performance
* run[r#]\_superdistrict_summaries\_[yr].csv contain a summary of select variables at the Super District level (n=33)
* run[r#]\_juris_summaries\_[yr].csv contain a summary of select variables at the juridictional level (n=108)
* run[r#]\_taz_summaries\_[yr].csv contain a summary of select variables at the Travel Analysis Zone level (n=1454)
* run[r#]\_baseyear\_pda_summaries\_2010.csv contain a summary at the PDA level for the START of 2010 (the other 2020 summary occurs at the end of the year 2010 and so contains one year of model forecast)




## Model Schematic
