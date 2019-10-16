
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
Bay Area UrbanSim (BAUS) is a land use or urban economic model used to forecast metropolitan growth, study urban policies, and evaluate transportation projects at the Metropolitan Transportation Commission (MTC). It is written in Python and is a customized version of the popular UrbanSim model developed by Professor Paul Waddell over the last few decades. BAUS simulates the movement of households and employees within the region, and the construction of new buildings to hold those households and employees. In this manner, it is usedf to incrementally forecast potential future urban growth trajectories.

## Approach
A forecast with BAUS begins with a basemap. This is a detailed geodatabase containing all of the region's buildings, households, employees, policies, and transport network for a recent year. This roughly corresponds to tooday's conditions but is a few years in the past due to data collection lag. The buildings are largely an accurate collection of every structure gathered from assessor's data, commercial read estate databases, and other sources. The households and employees are representred at the micro level but their characteristics our built through synthesis (i.e., we only have samples of this informations so we build a full repsresentation that is consistent with these samples. Policies such as zoning and growth limits are collected for each jurisdiction and are binding unless they are explicitly changed for a forecast.

BAUS is used to forecast the future by advancing through repeated steps that chart out a potential pathway for future urban growth. In BAUS each step represents a five year period. Most steps repeat the same set of sub-steps. In UrbanSim, each of these sub-steps is called a "model".  The file used to run BAUS (baus.py) sets the number steps and the order in which the models are are run. The major model steps are: 
* (Hazards): This optional model simulates the impact of earthquakes and sea level rise by destroying buildings and displacing their inhabitants.
* Calculate accessibility: Logsum accessibility measures are brought in from the Travel Model and pedestrian accessibility is calculated within UrbanSim
* Calculate housing prices and rents: Hedonic regression models are applied to current conditions to reestimate current prices and rents
* HH/employee relcation and transition: Some households and employeees are selected to move. Additiional households and employees are added or subtracted to reflect the exogenous control totals.
* Add buildings from the Development Projects list: Buildings are forced into the model (as opposed to being explicitly modeled). These represent institutional plans (e.g., universities and hospitals), large approved projects (e.g., Treasure Island), and development that has occurred between the basemap year and the current year (i.e., constructed 2016-2020).
* Build new market-rate housing units and commercial space: The for-profit real estate development process is simulated and new buildings are built where they are most feasible. This also build deed-restricted unit that are produced through the market-rate process (e.g., inclusionary zoning).
* Build new deed-restricted affordable units:: A similar not-for-profit real estate development process produces affordable housing units based on money available within BAUS Accounts (e.g., bond measures).
* HH/employee location choices: Households and employees are assigned to new locations based on logistic regresssion models that capture the preferences of particular segments (e.g., lower income households, retail jobs).
* Produce summary tables: Numerous zonal summaries of the detailed geodatabaase are produced for analysis of urban change and for use in the Travel Model.

Typically, a set of BAUS inputs or assumptions are modified to produce a scenario. Policies such as zoning or fees can be modified. Control totals can be adjusted. Assumptions about preferences or financical situations can be adjsuted. The package of changes is then simulated to forecast its impact on the future urban landscape and these outcomes are often enterered into the travel model to predict future year travel patterns or greenhouse gas emmissions.


## Application Types
BAUS is used for for three typical types of application:
* Forecasting: UrbanSim produces a complete map for each five year interval into the future. 
* Policy Studies
* Transport Project Evaluation: 



## Model System
BAUS is the middle model in an interactive suite of three model systems maintained by MTC:
* Regional economic and demographic information is supplied to BAUS from the REMI CGE model and related demographic processing scripts. BAUS outputs on housing production are used to adjust regional housing prices (and thus other variables) in REMI. 
* Accessibillity information is supplied to BAUS from the Travel Model and influences real estate prices and household and employee location choices. BAUS outputs on the location of various types of households and employees are used to establish origins and destinations in the Travel Model.

## Model Exectution

## Output Files



## Model Schematic
