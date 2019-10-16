---
layout: page
title: Input Data
---

*Work in Progress*

# Input Data

---
CONTENTS

1. [Base Year Geodatabase](#base-year-geodatabase) 
2. [Base Year Zoning](#base-year-zoning)

---

# Base Year GeoDatabase
Bay Area UrbanSim requires a representation of the region's parcels, buildings, households, and employees for the base simulation year (2015). This data is assembled and recoded by the BASIS project, enhanced with propietary and inhouse data, imputed to ensure buildings can hold all households/employees, and household/employees are allocated to specific buildings. 

## BASIS Processing
The BASIS team produces three files: parcel geometry, parcel attributes, and buildings. 

## Basemap Enhancement

### Schools


### Additional Buildings


### Commercial Real Estate


### Fill In Missing Values Using xxxx






### Tag Parcels with Zones
zone_id, taz22, maz, school districts


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



# Base Year Zoning
