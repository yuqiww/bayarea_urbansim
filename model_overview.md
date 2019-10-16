
---
layout: page
title: Model Overview
---

*Work in Progress*

# Model Overview

---
CONTENTS
 
1. [Introdution](#introduction)
2. [Setup and Configuration](#setup-and-configuration)
3. [Input Files](#input-files)
4. [Model Exectution](#model-exectution)
5. [Output Files](#output-files)
6. [Model Schematic](#model-schematic)

---

## Introduction
Bay Area UrbanSim (BAUS) is a land use or urban economic model used to forecast metropolitan growth, study urban policies, and evaluate transportation projects at the Metropolitan Transportation Commission (MTC). It is written in Python and is a customized version of the popular UrbanSim model developed by Professor Paul Waddell over the last few decades. 

## Approach
BAUS is used to forecast the future by advancing through repeated steps that chart out a potential pathway for future urban growth. In BAUS each step represents a five year period. Most steps repeat the same set of sub-steps. In UrbanSim, each of these sub-steps is called a "model".  The file used to run BAUS (baus.py) sets the number steps and the order in which the models are are run. 

A forecast with BAUS begins with a basemap. This is a detailed geodatabase containing all of the region's buildings, households, employees, policies, and transport network for a recent year. This roughly corresponds to tooday's conditions but is a few years in the past due to data collection lag. The buildings are largely an accurate collection of every structure gathered from assessor's data, commercial read estate databases, and other sources. The households and employees are representred at the micro level but their characteristics our built through synthesis (i.e., we only have samples of this informations so we build a full repsresentation that is consistent with these samples. Policies such as zoning and growth limits are collected for each jurisdiction and are binding unless they are explicitly changed for a forecast.

* (hazards)
* calculate accessibility
* calculate housing prices and rents
* hh/employee relcation and transition
* HH/employee location choices
* Produce summary tables


## Application Types
BAUS is used for for three typical types of application:
* Forecasting:
* Policy Studies
* Transport Project Evaluation: 



## Model System
BAUS is the middle model in an interactive suite of three model systems maintained by MTC:
* Regional economic and demographic information is supplied to BAUS from the REMI CGE model and related demographic processing scripts. BAUS outputs on housing production are used to adjust regional housing prices (and thus other variables) in REMI. 
* Accessibillity information is supplied to BAUS from the Travel Model and influences real estate prices and household and employee location choices. BAUS outputs on the location of various types of households and employees are used to establish origins and destinations in the Travel Model.

## Model Exectution

## Output Files



## Model Schematic
