import numpy as np
import pandas as pd
from urbansim.utils import misc
import orca
import datasources
from utils import nearest_neighbor
from urbansim_defaults import utils
from urbansim_defaults import variables


#####################
# HOUSEHOLDS VARIABLES
#####################


# used to pretent a segmented choice model isn't actually segmented
@orca.column('households', 'ones', cache=True)
def income_decile(households):
    return pd.Series(1, households.index)


@orca.column('households', 'tmnode_id', cache=True)
def node_id(households, buildings):
    return misc.reindex(buildings.tmnode_id, households.building_id)


#####################
# HOMESALES VARIABLES
#####################


@orca.column('homesales', cache=True)
def general_type(buildings):
    return buildings.general_type


BUILDING_AGE_BREAK = 40
@orca.column('homesales', cache=True)
def building_age(homesales):
    return 2014 - homesales.year_built


@orca.column('homesales', cache=True)
def building_age_recent(homesales):
    s = homesales.building_age
    return s * (s < BUILDING_AGE_BREAK)


@orca.column('homesales', cache=True)
def building_age_old(homesales):
    s = homesales.building_age
    return s * (s >= BUILDING_AGE_BREAK)


@orca.column('homesales', 'juris_ave_income', cache=True)
def juris_ave_income(parcels, homesales):
    return misc.reindex(parcels.juris_ave_income, homesales.parcel_id)


@orca.column('homesales', cache=True)
def zonal_veryhighinc(homesales, taz):
    return misc.reindex(taz.veryhighinc, homesales.zone_id).\
        reindex(homesales.index).fillna(0)


@orca.column('homesales', 'is_sanfran', cache=True)
def is_sanfran(parcels, homesales):
    return misc.reindex(parcels.is_sanfran, homesales.parcel_id)


@orca.column('homesales', 'node_id', cache=True)
def node_id(homesales, parcels):
    return misc.reindex(parcels.node_id, homesales.parcel_id)


@orca.column('homesales', 'tmnode_id', cache=True)
def tmnode_id(homesales, parcels):
    return misc.reindex(parcels.tmnode_id, homesales.parcel_id)


@orca.column('homesales', 'zone_id', cache=True)
def zone_id(homesales, parcels):
    return misc.reindex(parcels.zone_id, homesales.parcel_id)


@orca.column('homesales', cache=True)
def modern_condo(homesales):
    # this is to try and differentiate between new
    # construction in the city vs in the burbs
    return ((homesales.year_built > 2000) *
            (homesales.building_type_id == 3)).astype('int')


@orca.column('homesales', cache=True)
def new_construction(homesales):
    return (homesales.year_built > 2000).astype('int')


@orca.column('homesales', cache=True)
def historic(homesales):
    return (homesales.year_built < 1940).astype('int')


@orca.column('homesales', cache=True)
def base_price_per_sqft(homesales):
    s = homesales.price_per_sqft.groupby(homesales.zone_id).quantile()
    return misc.reindex(s, homesales.zone_id)


@orca.column('homesales', cache=True)
def transit_type(homesales, parcels_geography):
    return misc.reindex(parcels_geography.tpp_id, homesales.parcel_id).\
        reindex(homesales.index).fillna('none')


#####################
# COSTAR VARIABLES
#####################


@orca.column('costar', 'juris_ave_income', cache=True)
def juris_ave_income(parcels, costar):
    return misc.reindex(parcels.juris_ave_income, costar.parcel_id)


@orca.column('costar', 'is_sanfran', cache=True)
def is_sanfran(parcels, costar):
    return misc.reindex(parcels.is_sanfran, costar.parcel_id)


@orca.column('costar', 'general_type')
def general_type(costar):
    return costar.PropertyType


@orca.column('costar', 'node_id')
def node_id(parcels, costar):
    return misc.reindex(parcels.node_id, costar.parcel_id)


@orca.column('costar', 'tmnode_id')
def tmnode_id(parcels, costar):
    return misc.reindex(parcels.tmnode_id, costar.parcel_id)


@orca.column('costar', 'zone_id')
def zone_id(parcels, costar):
    return misc.reindex(parcels.zone_id, costar.parcel_id)


@orca.column('costar', cache=True)
def transit_type(costar, parcels_geography):
    return misc.reindex(parcels_geography.tpp_id, costar.parcel_id).\
        reindex(costar.index).fillna('none')


#####################
# JOBS VARIABLES
#####################


@orca.column('jobs', 'tmnode_id', cache=True)
def tmnode_id(jobs, buildings):
    return misc.reindex(buildings.tmnode_id, jobs.building_id)


@orca.column('jobs', 'naics', cache=True)
def naics(jobs):
    return jobs.sector_id


@orca.column('jobs', 'empsix', cache=True)
def empsix(jobs, settings):
    return jobs.naics.map(settings['naics_to_empsix'])


@orca.column('jobs', 'empsix_id', cache=True)
def empsix_id(jobs, settings):
    return jobs.empsix.map(settings['empsix_name_to_id'])


#####################
# BUILDINGS VARIABLES
#####################


# I want to round this cause otherwise we'll be underfilling job spaces
# in the aggregate because of rounding errors - this way some spaces will
# be underfilled and othersoverfilled which should yield an average of
# the sqft_per_job table
@orca.column('buildings', 'job_spaces', cache=False)
def job_spaces(buildings):
    return (buildings.non_residential_sqft /
            buildings.sqft_per_job).fillna(0).round().astype('int')


@orca.column('buildings', cache=True)
def building_age(buildings, year):
    return (year or 2014) - buildings.year_built


@orca.column('buildings', cache=True)
def building_age_recent(buildings):
    s = buildings.building_age
    return s * (s < BUILDING_AGE_BREAK)


@orca.column('buildings', cache=True)
def building_age_old(buildings):
    s = buildings.building_age
    return s * (s >= BUILDING_AGE_BREAK)


@orca.column('buildings', cache=True)
def zonal_veryhighinc(buildings, taz):
    return misc.reindex(taz.veryhighinc, buildings.zone_id).\
        reindex(buildings.index).fillna(0)


@orca.column('buildings', cache=True)
def transit_type(buildings, parcels_geography):
    return misc.reindex(parcels_geography.tpp_id, buildings.parcel_id).\
        reindex(buildings.index).fillna('none')


@orca.column('buildings', cache=False)
def unit_price(buildings):
    return buildings.residential_price * buildings.sqft_per_unit


@orca.column('buildings', cache=True)
def base_price_per_sqft(homesales, buildings):
    s = homesales.price_per_sqft.groupby(homesales.zone_id).quantile()
    return misc.reindex(s, buildings.zone_id).reindex(buildings.index)\
        .fillna(s.quantile())


@orca.column('buildings', 'tmnode_id', cache=True)
def tmnode_id(buildings, parcels):
    return misc.reindex(parcels.tmnode_id, buildings.parcel_id)


@orca.column('buildings', 'juris_ave_income', cache=True)
def juris_ave_income(parcels, buildings):
    return misc.reindex(parcels.juris_ave_income, buildings.parcel_id)


@orca.column('buildings', 'is_sanfran', cache=True)
def is_sanfran(parcels, buildings):
    return misc.reindex(parcels.is_sanfran, buildings.parcel_id)


@orca.column('buildings', 'sqft_per_unit', cache=True)
def unit_sqft(buildings):
    return (buildings.building_sqft /
            buildings.residential_units.replace(0, 1)).clip(400, 6000)


@orca.column('buildings', cache=True)
def modern_condo(buildings):
    # this is to try and differentiate between new construction
    # in the city vs in the burbs
    return ((buildings.year_built > 2000) * (buildings.building_type_id == 3))\
        .astype('int')


@orca.column('buildings', cache=True)
def new_construction(buildings):
    return (buildings.year_built > 2000).astype('int')



@orca.column('buildings', cache=True)
def historic(buildings):
    return (buildings.year_built < 1940).astype('int')


@orca.column('buildings', cache=True)
def vmt_res_cat(buildings, vmt_fee_categories):
    return misc.reindex(vmt_fee_categories.res_cat, buildings.zone_id)


#####################
# PARCELS VARIABLES
#####################


@orca.column('parcels', cache=True)
def vmt_res_cat(parcels, vmt_fee_categories):
    return misc.reindex(vmt_fee_categories.res_cat, parcels.zone_id)


@orca.column('parcels', cache=True)
def pda(parcels, parcels_geography):
    return parcels_geography.pda_id.reindex(parcels.index)


@orca.column('parcels', cache=True)
def juris(parcels, parcels_geography):
    return parcels_geography.juris_name.reindex(parcels.index)


@orca.column('parcels', 'ave_sqft_per_unit')
def ave_sqft_per_unit(parcels, zones, settings):
    s = misc.reindex(zones.ave_unit_sqft, parcels.zone_id)
    clip = settings.get("ave_sqft_per_unit_clip", None)
    if clip is not None:
        s = s.clip(lower=clip['lower'], upper=clip['upper'])
    return s


# these are actually functions that take parameters, but are parcel-related
# so are defined here
@orca.injectable('parcel_average_price', autocall=False)
def parcel_average_price(use, quantile=.5):
    # I'm testing out a zone aggregation rather than a network aggregation
    # because I want to be able to determine the quantile of the distribution
    # I also want more spreading in the development and not keep it localized
    if use == "residential":

        # get node price average and put it on parcels
        s = misc.reindex(orca.get_table('nodes')[use],
                         orca.get_table('parcels').node_id) * 1.3

        # apply shifters
        cost_shifters = orca.get_table("parcels").cost_shifters
        price_shifters = orca.get_table("parcels").price_shifters
        s = s / cost_shifters * price_shifters

        # just to make sure
        s = s.fillna(0).clip(150, 1250)
        return s

    if 'nodes' not in orca.list_tables():
        return pd.Series(0, orca.get_table('parcels').index)

    return misc.reindex(orca.get_table('nodes')[use],
                        orca.get_table('parcels').node_id)


@orca.injectable('parcel_sales_price_sqft_func', autocall=False)
def parcel_sales_price_sqft(use):
    s = parcel_average_price(use)
    if use == "residential":
        s *= 1.0
    return s

#############################
# Functions for Checking
# Allowed Uses and Building
# Types on Parcels
#############################


@orca.injectable('parcel_is_allowed_func', autocall=False)
def parcel_is_allowed(form):
    settings = orca.get_injectable('settings')
    form_to_btype = settings["form_to_btype"]
    # we have zoning by building type but want
    # to know if specific forms are allowed
    allowed = [orca.get_table('zoning_baseline')
               ['type%d' % typ] > 0 for typ in form_to_btype[form]]
    s = pd.concat(allowed, axis=1).max(axis=1).\
        reindex(orca.get_table('parcels').index).fillna(False)

    return s


@orca.column('parcels', 'first_building_type_id')
def first_building_type_id(buildings, parcels):
    df = buildings.to_frame(
        columns=['building_type_id', 'parcel_id'])
    return df.groupby('parcel_id').building_type_id.first()


@orca.injectable('parcel_first_building_type_is', autocall=False)
def parcel_first_building_type_is(form):
    settings = orca.get_injectable('settings')
    form_to_btype = settings["form_to_btype"]
    parcels = orca.get_table('parcels')
    s = parcels.first_building_type_id.isin(form_to_btype[form])
    return s

#############################
# Summary by TAZ for
# Output to Travel Model
#############################


@orca.column('zones')
def ave_unit_sqft(buildings):
    return buildings.sqft_per_unit.groupby(buildings.zone_id).quantile(.6)


@orca.column('taz', 'gqpop')
def gqpop(zones, zone_forecast_inputs, year):
    str1 = "gqpop" + str(year)[-2:]
    s = zone_forecast_inputs[str1]
    return s


@orca.column('taz', 'totacre')
def totacre(zone_forecast_inputs):
    s = zone_forecast_inputs.totacre_abag
    return s


@orca.column('taz', 'shpop62p')
def shpop62p(zone_forecast_inputs):
    s = zone_forecast_inputs.sh_62plus
    return s


@orca.table('buildings_subset')
def buildings_subset(buildings):
    df = buildings.to_frame(columns=['zone_id',
                                     'building_type_id',
                                     'residential_units',
                                     'building_sqft',
                                     'lot_size_per_unit'])
    return df


@orca.column('taz', 'newdevacres')
def newdevacres(buildings_subset):
    df = buildings_subset.to_frame()
    s = (df.query("building_sqft > 0").
         groupby('zone_id').lot_size_per_unit.sum()) / 43560
    return s


@orca.column('taz', 'resunits')
def resunits(buildings_subset):
    df = buildings_subset.to_frame()
    s = df.groupby('zone_id').residential_units.sum()
    return s


@orca.column('taz', 'mfdu')
def mfdu(buildings_subset):
    df = buildings_subset.to_frame()
    s = df.query("building_type_id == 3 or building_type_id == 12").\
        groupby('zone_id').residential_units.sum()
    return s


@orca.column('taz', 'sfdu')
def sfdu(buildings_subset):
    df = buildings_subset.to_frame()
    s = df.query("building_type_id == 1 or building_type_id == 2").\
        groupby('zone_id').residential_units.sum()
    return s


@orca.table('households_subset')
def households_subset(households):
    zone_id = households.zone_id
    income = households.income
    persons = households.persons
    df = pd.DataFrame(data={'zone_id': zone_id, 'income': income,
                            'persons': persons})
    return df


@orca.column('taz', 'hhinq1')
def hhinq1(households_subset):
    df = households_subset.to_frame()
    s = df.query("income < 25000").\
        groupby('zone_id').size()
    return s


@orca.column('taz', 'hhinq2')
def hhinq2(households_subset):
    df = households_subset.to_frame()
    s = df.query("income >= 25000 and income < 45000").\
        groupby('zone_id').size()
    return s


@orca.column('taz', 'hhinq3')
def hhinq3(households_subset):
    df = households_subset.to_frame()
    s = df.query("income >= 45000 and income < 75000").\
        groupby('zone_id').size()
    return s


@orca.column('taz', 'hhinq4')
def hhinq4(households_subset):
    df = households_subset.to_frame()
    s = df.query("income >= 75000").\
        groupby('zone_id').size()
    return s


@orca.column('taz', 'veryhighinc')
def hhinq4(households_subset, taz):
    df = households_subset.to_frame()
    s = df.query("income >= 75000").\
        groupby('zone_id').size()
    return s / taz.tothh.replace(0, 1)


@orca.column('taz', 'tothh')
def tothh(households_subset):
    df = households_subset.to_frame()
    s = df.groupby('zone_id').size()
    return s


@orca.column('taz', 'hhpop')
def hhpop(households_subset):
    df = households_subset.to_frame()
    s = df.groupby('zone_id').persons.sum()
    return s


@orca.column('taz', 'resvacancy')
def resvacancy(taz):
    s = (taz.resunits - taz.tothh) / \
        taz.resunits.replace(0, 1)
    return s


@orca.table('jobs_subset')
def jobs_subset(jobs):
    zone_id = jobs.zone_id
    empsix = jobs.empsix
    df = pd.DataFrame(data={'zone_id': zone_id, 'empsix': empsix})
    return df


@orca.column('taz', 'totemp')
def totemp(jobs_subset):
    df = jobs_subset.to_frame()
    s = df.groupby('zone_id').size()
    return s


@orca.column('taz', 'agrempn')
def agrempn(jobs_subset):
    df = jobs_subset.to_frame()
    s = df.query("empsix == 'AGREMPN'").\
        groupby('zone_id').size()
    return s


@orca.column('taz', 'mwtempn')
def mwtempn(jobs_subset):
    df = jobs_subset.to_frame()
    s = df.query("empsix == 'MWTEMPN'").\
        groupby('zone_id').size()
    return s


@orca.column('taz', 'retempn')
def retempn(jobs_subset):
    df = jobs_subset.to_frame()
    s = df.query("empsix == 'RETEMPN'").\
        groupby('zone_id').size()
    return s


@orca.column('taz', 'fsempn')
def fsempn(jobs_subset):
    df = jobs_subset.to_frame()
    s = df.query("empsix == 'FPSEMPN'").\
        groupby('zone_id').size()
    return s


@orca.column('taz', 'herempn')
def herempn(jobs_subset):
    df = jobs_subset.to_frame()
    s = df.query("empsix == 'HEREMPN'").\
        groupby('zone_id').size()
    return s


@orca.column('taz', 'othempn')
def othempn(jobs_subset):
    df = jobs_subset.to_frame()
    s = df.query("empsix == 'OTHEMPN'").\
        groupby('zone_id').size()
    return s


@orca.column('taz', 'sd')
def sd(taz_geography):
    s = taz_geography.superdistrict
    return s


@orca.column('taz', 'county')
def sd(taz_geography):
    s = taz_geography.county
    return s

# @orca.column('taz','totpop')
# def totpop(taz):
#     s = taz.gqpop
#     s1 = taz.hhpop
#     s2 = s1+s
#     return s2


@orca.column('taz', 'density')
def density(taz):
    s = (taz.totpop + (2.5 * taz.totemp)) / taz.totacre
    return s


@orca.column('taz', 'areatype')
def density(taz):
    import numpy as np
    s = pd.cut(taz.density, bins=[0, 6, 30, 55,
                                  100, 300, np.inf], labels=[5, 4, 3, 2, 1, 0])
    return s


@orca.column('taz', 'ciacre')
def ciacre(parcels, taz):
    f = orca.get_injectable('parcel_first_building_type_is')
    s = f('select_non_residential')
    s1 = parcels.get_column('zone_id')
    s2 = parcels.parcel_acres * s
    df = pd.DataFrame(data={'zone_id': s1, 'ciacre': s2})
    s3 = df.groupby('zone_id').ciacre.sum()
    return s3


@orca.column('taz', 'resacre')
def resacre(parcels):
    f = orca.get_injectable('parcel_first_building_type_is')
    s = f('residential') | f('mixedresidential')
    s1 = parcels.get_column('zone_id')
    s2 = parcels.parcel_acres * s
    df = pd.DataFrame(data={'zone_id': s1, 'residential_acres': s2})
    s3 = df.groupby('zone_id').residential_acres.sum()
    return s3


@orca.column('parcels', 'juris_ave_income', cache=True)
def juris_ave_income(households, buildings, parcels_geography, parcels):
    h = orca.merge_tables("households",
                          [households, buildings, parcels_geography],
                          columns=["jurisdiction", "income"])
    s = h.groupby(h.jurisdiction).income.quantile(.5)
    return misc.reindex(s, parcels_geography.jurisdiction).\
        reindex(parcels.index).fillna(s.median()).apply(np.log1p)


# returns the newest building on the land and fills missing values with 1800 -
# for use with development limits
@orca.column('parcels', 'newest_building')
def newest_building(parcels, buildings):
    return buildings.year_built.groupby(buildings.parcel_id).max().\
        reindex(parcels.index).fillna(1800)


@orca.column('parcels', cache=True)
def manual_nodev(parcel_rejections, parcels):
    df1 = parcels.to_frame(['x', 'y']).dropna(subset=['x', 'y'])
    df2 = parcel_rejections.to_frame(['lng', 'lat'])
    df2 = df2[parcel_rejections.state == "denied"]
    df2 = df2[["lng", "lat"]]  # need to change the order
    ind = nearest_neighbor(df1, df2)

    s = pd.Series(False, parcels.index)
    s.loc[ind.flatten()] = True
    return s.astype('int')


@orca.column('parcels', 'oldest_building_age')
def oldest_building_age(parcels, year):
    return year - parcels.oldest_building.replace(9999, 0)


@orca.column('parcels', 'is_sanfran', cache=True)
def is_sanfran(parcels_geography, buildings, parcels):
    return (parcels_geography.juris_name == "San Francisco").\
        reindex(parcels.index).fillna(False).astype('int')


# actual columns start here
@orca.column('parcels', 'max_far', cache=True)
def max_far(parcels, scenario, scenario_inputs):
    s = utils.conditional_upzone(scenario, scenario_inputs,
                                 "max_far", "far_up").\
        reindex(parcels.index)
    return s * ~parcels.nodev


# returns a vector where parcels are ALLOWED to be built
@orca.column('parcels')
def parcel_rules(parcels):
    # removes parcels with buildings < 1940,
    # and single family homes on less then half an acre
    s = (parcels.oldest_building < 1940) | \
        ((parcels.total_residential_units == 1) & (parcels.parcel_acres < .5))
    s = (~s.reindex(parcels.index).fillna(False)).astype('int')
    return s


@orca.column('parcels', 'total_non_residential_sqft', cache=True)
def total_non_residential_sqft(parcels, buildings):
    return buildings.non_residential_sqft.groupby(buildings.parcel_id).sum().\
        reindex(parcels.index).fillna(0)


@orca.column('parcels')
def nodev(zoning_baseline, parcels):
    return zoning_baseline.nodev.reindex(parcels.index).\
        fillna(0).astype('bool')


@orca.column('parcels', 'max_dua', cache=True)
def max_dua(parcels, scenario, scenario_inputs):
    s = utils.conditional_upzone(scenario, scenario_inputs,
                                 "max_dua", "dua_up").\
        reindex(parcels.index)
    return s * ~parcels.nodev


@orca.column('parcels', 'max_height', cache=True)
def max_height(parcels, zoning_baseline):
    return zoning_baseline.max_height.reindex(parcels.index)


# these next two are just indicators put into the output
@orca.column('parcels', 'residential_purchase_price_sqft')
def residential_purchase_price_sqft(parcels):
    return parcels.building_purchase_price_sqft


@orca.column('parcels', 'residential_sales_price_sqft')
def residential_sales_price_sqft(parcel_sales_price_sqft_func):
    return parcel_sales_price_sqft_func("residential")


@orca.column('parcels', 'general_type')
def general_type(parcels, buildings):
    s = buildings.general_type.groupby(buildings.parcel_id).first()
    return s.reindex(parcels.index).fillna("Vacant")


# for debugging reasons this is split out into its own function
@orca.column('parcels', 'building_purchase_price_sqft')
def building_purchase_price_sqft(parcels):
    price = pd.Series(0, parcels.index)
    gentype = parcels.general_type
    for form in ["Office", "Retail", "Industrial", "Residential"]:
        # convert to yearly
        factor = 1.0 if form == "Residential" else 20.0
        # raise cost to convert from industrial
        if form == "Industrial":
            factor *= 3.0
        if form == "Retail":
            factor *= 2.0
        if form == "Office":
            factor *= 1.4
        tmp = parcel_average_price(form.lower())
        price += tmp * (gentype == form) * factor

    return price.clip(150, 2500)


@orca.column('parcels', 'building_purchase_price')
def building_purchase_price(parcels):
    # the .8 is because we assume the building only charges for 80% of the
    # space - when a good portion of the building is parking, this probably
    # overestimates the part of the building that you can charge for
    # the second .85 is because the price is likely to be lower for existing
    # buildings than for one that is newly built
    return (parcels.total_sqft * parcels.building_purchase_price_sqft *
            .8 * .85).reindex(parcels.index).fillna(0)


@orca.column('parcels', 'land_cost')
def land_cost(parcels):
    s = pd.Series(20, parcels.index)
    s[parcels.general_type == "Industrial"] = 150.0
    return parcels.building_purchase_price + parcels.parcel_size * s


@orca.column('parcels', 'county')
def county(parcels, settings):
    return parcels.county_id.map(settings["county_id_map"])


@orca.column('parcels', 'cost_shifters')
def cost_shifters(parcels, settings):
    return parcels.county.map(settings["cost_shifters"])


@orca.column('parcels', 'price_shifters')
def price_shifters(parcels, settings):
    return parcels.pda.map(settings["pda_price_shifters"]).fillna(1.0)


@orca.column('parcels', 'node_id', cache=True)
def node_id(parcels, net):
    s = net["walk"].get_node_ids(parcels.x, parcels.y)
    fill_val = s.value_counts().index[0]
    s = s.reindex(parcels.index).fillna(fill_val).astype('int')
    return s


@orca.column('parcels', 'tmnode_id', cache=True)
def node_id(parcels, net):
    s = net["drive"].get_node_ids(parcels.x, parcels.y)
    fill_val = s.value_counts().index[0]
    s = s.reindex(parcels.index).fillna(fill_val).astype('int')
    return s


@orca.column('parcels', 'vmt_res_cat', cache=True)
def vmt_code(parcels, vmt_fee_categories):
    return misc.reindex(vmt_fee_categories.res_cat, parcels.zone_id)

GROSS_AVE_UNIT_SIZE = 1000

###################################
#   Zoning Capacity Variables
###################################


@orca.column('parcels_zoning_calculations', 'zoned_du', cache=True)
def zoned_du(parcels):
    s = parcels.max_dua * parcels.parcel_acres
    s2 = parcels.max_far * parcels.parcel_size / GROSS_AVE_UNIT_SIZE
    s3 = parcel_is_allowed('residential')
    return (s.fillna(s2) * s3).reindex(parcels.index).fillna(0).astype('int')


@orca.column('parcels_zoning_calculations', 'effective_max_dua', cache=True)
def effective_max_dua(parcels):
    s = parcels.max_dua
    s2 = parcels.max_far * parcels.parcel_size / \
        GROSS_AVE_UNIT_SIZE / parcels.parcel_acres
    s3 = parcel_is_allowed('residential')
    return (s.fillna(s2) * s3).reindex(parcels.index).fillna(0).astype('float')


@orca.column('parcels_zoning_calculations',
             'effective_max_office_far', cache=True)
def effective_max_office_far(parcels):
    s = parcels.max_far
    s2 = parcels.max_height / 11
    s3 = parcel_is_allowed('office')
    return (s.fillna(s2) * s3).reindex(parcels.index).fillna(0).astype('float')


########################################
# there are a number of variables
# here that try to get at zoned capacity
########################################


@orca.column('parcels_zoning_calculations', 'zoned_du_underbuild')
def zoned_du_underbuild(parcels, parcels_zoning_calculations):
    # subtract from zoned du, the total res units, but also the equivalent
    # of non-res sqft in res units
    s = (parcels_zoning_calculations.zoned_du -
         parcels.total_residential_units -
         parcels.total_non_residential_sqft /
         GROSS_AVE_UNIT_SIZE).clip(lower=0)
    ratio = (s / parcels.total_residential_units).replace(np.inf, 1)
    # if the ratio of additional units to existing units is not at least .5
    # we don't build it - I mean we're not turning a 10 story building into an
    # 11 story building
    s = s[ratio > .5].reindex(parcels.index).fillna(0)
    return s.astype('int')


@orca.column('parcels_zoning_calculations')
def zoned_du_underbuild_nodev(parcels, parcels_zoning_calculations):
    return (parcels_zoning_calculations.zoned_du_underbuild *
            parcels.parcel_rules).astype('int')


@orca.column('parcels_zoning_calculations', 'office_allowed')
def office_allowed(parcels):
    office_allowed = parcel_is_allowed('office')
    return office_allowed


@orca.column('parcels_zoning_calculations', 'retail_allowed')
def retail_allowed(parcels):
    retail_allowed = parcel_is_allowed('retail')
    return retail_allowed


@orca.column('parcels_zoning_calculations', 'industrial_allowed')
def industrial_allowed(parcels):
    industrial_allowed = parcel_is_allowed('industrial')
    return industrial_allowed


@orca.column('parcels_zoning_calculations', 'cat_r')
def cat_r(parcels_zoning_calculations):
    s = ~parcels_zoning_calculations.office_allowed &\
        parcels_zoning_calculations.retail_allowed
    s2 = pd.Series(index=parcels_zoning_calculations.index).fillna('R')
    return s * s2


@orca.column('parcels_zoning_calculations', 'cat_ind')
def cat_ind(parcels_zoning_calculations):
    s = ~parcels_zoning_calculations.office_allowed &\
        ~parcels_zoning_calculations.retail_allowed &\
        parcels_zoning_calculations.industrial_allowed
    s2 = pd.Series(index=parcels_zoning_calculations.index).fillna('I')
    return s * s2


@orca.column('parcels_zoning_calculations', 'office_high')
def office_high(parcels_zoning_calculations):
    s = parcels_zoning_calculations.effective_max_office_far > 4
    s2 = pd.Series(index=parcels_zoning_calculations.index).fillna('OH')
    s3 = s * s2
    return s3


@orca.column('parcels_zoning_calculations', 'office_medium')
def office_medium(parcels_zoning_calculations):
    s = parcels_zoning_calculations.effective_max_office_far > 1
    s2 = parcels_zoning_calculations.effective_max_office_far <= 4
    s3 = pd.Series(index=parcels_zoning_calculations.index).fillna('OM')
    return (s & s2) * s3


@orca.column('parcels_zoning_calculations', 'office_low')
def office_low(parcels_zoning_calculations):
    s = parcels_zoning_calculations.effective_max_office_far < 1
    s2 = parcels_zoning_calculations.office_allowed
    s3 = pd.Series(index=parcels_zoning_calculations.index).fillna('OL')
    return (s & s2) * s3


@orca.column('parcels_zoning_calculations', 'non_res_categories')
def non_res_categories(parcels_zoning_calculations):
    pzc = parcels_zoning_calculations
    s = pzc.office_high + pzc.office_medium + \
        pzc.office_low + pzc.cat_r + pzc.cat_ind
    return s
