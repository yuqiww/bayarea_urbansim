---
layout: page
title: Input Data
---

*Work in Progress*

# Input Data

---
CONTENTS

1. [Base Year Geodatabase](#base-year-geodatabase) 
2. [Existing Planned Land Use](#existing-planned-land-use)
2. [Scenario Planned Land Use](#scenario-planned-land-use)
2. [Other Urban Policies](#other-urban-policies)

---

# Base Year GeoDatabase
The basemap is a geodatabase containing the region's parcels, buildings, households, and jobs in the baseyear (2015 for PBA50). It is built in two major stages:
1. The assembly and cleaning of raw dataset. This is done through manual data cleaning in excel and python scripts in ArcGIS Pro and is described at https://github.com/BayAreaMetro/petrale/edit/master/basemap/basemap_assembly_steps.md
2. Imputation of missing data to conform to regional totals. This is done through python scripts integrated into Bay Area UrbanSim and is described here.

### Table Modifications
The input tables are transformed in the process below into new versions with "preproc" appended to the names:
* parcels.csv becomes parcels_
* buildings
* households.csv becomes households_preproc.csv with the following changes:
1. 

tenure
unittype
unit_num
unit_id
* jobs.csv becomes jobs_preproc.csv with 
1. empsix 
2. building_id



### Fill In Missing Values Using xxxx







### [Match Aggregate]((https://github.com/MetropolitanTransportationCommission/bayarea_urbansim/blob/master/data_regeneration/match_aggregate.py))

TAZ as local control for both res and comm




### Impute Prices



## BAUS Preprocessing Mode
Run BAUS as ** and it runs only 4 models
### "preproc_jobs",


###            "preproc_households",
###            "preproc_buildings",
###            "initialize_residential_units"


### [Allocate Demand Agents to Buuldings](https://github.com/MetropolitanTransportationCommission/bayarea_urbansim/blob/master/data_regeneration/demand_agent_allocation.py)

allocate jobs from TAZ to building




### Perform Quality Control Summaries

### Export Integrated Parcels
The [export_to_h5](https://github.com/MetropolitanTransportationCommission/bayarea_urbansim/blob/master/data_regeneration/export_to_h5.py) script:

* [maps](https://github.com/MetropolitanTransportationCommission/bayarea_urbansim/blob/master/data_regeneration/export_to_h5.py#L15-L31) development_type_id to building_type_id

* sets the h5 [path](https://github.com/MetropolitanTransportationCommission/bayarea_urbansim/blob/master/data_regeneration/export_to_h5.py#L13)

* [stores](https://github.com/MetropolitanTransportationCommission/bayarea_urbansim/blob/master/data_regeneration/export_to_h5.py#L60-L67) the tables in the hdf5

* among other things 



# Existing Planned Land Use


# Scenario Planned Land Use



# Other Urban Policies

