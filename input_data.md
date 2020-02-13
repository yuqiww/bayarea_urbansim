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

## Base Year GeoDatabase
The basemap is a geodatabase containing the region's parcels, buildings, households, and jobs in the baseyear (2015 for PBA50). It is built in two major stages:
1. The assembly and cleaning of raw dataset. This is done through manual data cleaning in excel and python scripts in ArcGIS Pro and is described at https://github.com/BayAreaMetro/petrale/edit/master/basemap/basemap_assembly_steps.md
2. Imputation of missing data to fill missing values and conform to regional totals. This is done by running BAUS in preprocessing mode.

### Preprocessing
BAUS's [preprocessing](https://github.com/BayAreaMetro/bayarea_urbansim/blob/master/baus/preprocessing.py) steps take raw input data and ready it for use in forecasting. This step only needs to be run once on a given instance of the base year data until something is changed. 


* Table Modifications
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



* Fill In Missing Values Using xxxx







* [Match Aggregate]((https://github.com/MetropolitanTransportationCommission/bayarea_urbansim/blob/master/data_regeneration/match_aggregate.py))

TAZ as local control for both res and comm

 [Allocate Demand Agents to Buuldings](https://github.com/MetropolitanTransportationCommission/bayarea_urbansim/blob/master/data_regeneration/demand_agent_allocation.py)

allocate jobs from TAZ to building




* Perform Quality Control Summaries

* Export Integrated Parcels
The [export_to_h5](https://github.com/MetropolitanTransportationCommission/bayarea_urbansim/blob/master/data_regeneration/export_to_h5.py) script:

* [maps](https://github.com/MetropolitanTransportationCommission/bayarea_urbansim/blob/master/data_regeneration/export_to_h5.py#L15-L31) development_type_id to building_type_id

* sets the h5 [path](https://github.com/MetropolitanTransportationCommission/bayarea_urbansim/blob/master/data_regeneration/export_to_h5.py#L13)

* [stores](https://github.com/MetropolitanTransportationCommission/bayarea_urbansim/blob/master/data_regeneration/export_to_h5.py#L60-L67) the tables in the hdf5

* among other things 



# Existing Planned Land Use
By deafult, BAUS assumes that local jurisdictions' regulations and what type and how much development can occur on a given parcel constrain development activity. This data is usually a jurisdiction's zoning but sometimes represent general plan or other modified capacity data. This information is provided by using two lookup tables:
* [2015_12_21_zoning_parcels.csv](https://mtcdrive.box.com/s/ir65mdbytf2lpjx8i41j7lpxqm4r1ujm) is stored on Box because of its size. This file links each parcel to its zoning_type_id.
* [zoning_lookup.csv](https://github.com/BayAreaMetro/bayarea_urbansim/blob/master/data/zoning_lookup.csv) joins with the file above using _id_ and provides the contraints for each zoning_type. Maximum allowable intensity is provide by max_far (Floor Area Ratio) for commercial development and by max_dua (Dwelling Units per Acre). _max_height_ constrains either type of development when it in not NULL. The 14 two-letter variables are dummy variable denoting whether each of these building types can be built in this zoning_type.

# Scenario Planned Land Use
BAUS is usually run using scenario-based inputs. These represent various potential changes to urban constraints and policies. Even "baseline" or No Project run generally use Scenario 0 which implements existing UGBs and a few minor adjustments to the basic planned land use information. The modifications to planned land use for a given scenario are not implemented within the existing planned land typology. Instead, two files contain these modfification relatiomnshiops:
* In parcels.csv inside [2015_09_01_v3.h5](https://mtcdrive.box.com/s/bo4u2dd6ed7k5bpwl2gnfc36lrxop791) each parcel is assigned to zoning modification category (zoning_mod_cat). These are the union of various zones of interest and each combination can have unique policies applied to it. The code is a concatenation of zone types and has changed through various applications:
 * In PBA50
* Each scenario-specific modfication table (e.g., for Scenario 4 see [zoning_mods_4.csv](https://github.com/BayAreaMetro/bayarea_urbansim/blob/master/data/zoning_mods_4.csv)) contains modifcations to the existing zoning including up/down-zoning and the addition/subtraction of allowed uses. If nothing is noted in a row, existing planned land use is retained in this scenario. 




# Other Urban Policies
Most urban policies beyond changes to planned land use are established in [policy.yaml](https://github.com/BayAreaMetro/bayarea_urbansim/blob/master/configs/policy.yaml), sometimes using data from a table in /data. For instance, inclusionary zoning is set up at https://github.com/BayAreaMetro/bayarea_urbansim/blob/4166c25a798f2b8d045546e5b6cef45a5ca9fa4c/configs/policy.yaml#L143,
