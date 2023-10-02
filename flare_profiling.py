##########################
# Creating Flare Profiles for SolarNN Training
#
# Joshua D. Ingram
#
# 07/05/2023
##########################

# import modules
import numpy as np
import pandas as pd

# load data
flare_data = pd.read_csv('/Users/joshuaingram/Main/Projects/SolarFlareNN/data/FlaresGoes161718Wavelet.csv')
print(sum(flare_data['Flare'] == 1))
print(sum(flare_data['Wavelet'] == 1))

# create function to create profiles training dataset for SolarNN



#def flare_pofiler():
#    # create empty dataframe
#
#


# 10-20 before, 20-35 after window width?
# local max for adjacent probabilities to identify flare peak
# look at the fraction of the time that the sun spends near the cycle minimum
# use the noise during that time for the training set for null cases for flare peaks
