import netCDF4 as nc
import numpy as np
import cftime
import matplotlib.pyplot as plt
from datetime import datetime
import os
import requests
from astropy.io import fits

url_path16 = "https://data.ngdc.noaa.gov/platforms/solar-space-observing-satellites/goes/goes16/l2/data/xrsf-l2-flsum_science/2023/02/"
files16 = np.array([ "sci_xrsf-l2-flsum_g16_d20230202_v2-2-0", "sci_xrsf-l2-flsum_g16_d20230203_v2-2-0", "sci_xrsf-l2-flsum_g16_d20230204_v2-2-0", "sci_xrsf-l2-flsum_g16_d20230207_v2-2-0", "sci_xrsf-l2-flsum_g16_d20230208_v2-2-0", "sci_xrsf-l2-flsum_g16_d20230210_v2-2-0", "sci_xrsf-l2-flsum_g16_d20230211_v2-2-0", "sci_xrsf-l2-flsum_g16_d20230212_v2-2-0"])

for ii in np.arange(np.size(files16)):
	filnc = files16[ii] + ".nc"
	filfits = files16[ii] + ".fits"
	if not os.path.exists(filnc):
		with open(filnc,"wb") as f:
			print(url_path16 + filnc)
			r = requests.get(url_path16 + filnc)
			f.write(r.content)
			ff = nc.Dataset(filnc)
			time = np.array(ff["time"][:])
			flxB = np.array(ff["xrsb_flux"][:])
			bkgB = np.array(ff["background_flux"][:])
			cl = np.array(ff["flare_class"][:])
			intf = np.array(ff["integrated_flux"][:])
			flrid = np.array(ff["flare_id"][:])
			yy = cftime.num2pydate(ff.variables["time"][:], ff["time"].units)
			c1 = fits.Column(name='Time',array=time, format='D')
			c2 = fits.Column(name='PeakfluxB',array=flxB, format='F')
			c3 = fits.Column(name='BkgfluxB',array=bkgB, format='F')
			c4 = fits.Column(name='TotfluxB',array=intf, format='F')
			c5 = fits.Column(name='FlareClass',array=cl, format='5A')
			c6 = fits.Column(name='FlareID',array=flrid, format='16A')
			c7 = fits.Column(name='Date',array=yy, format='20A')
			t = fits.BinTableHDU.from_columns([c1,c2,c3,c4,c5,c6,c7])
			t.writeto(filfits,overwrite=True)
			print(filfits)

url_path18 = "https://data.ngdc.noaa.gov/platforms/solar-space-observing-satellites/goes/goes18/l2/data/xrsf-l2-flsum_science/2023/02/"
files18 = np.array(["sci_xrsf-l2-flsum_g18_d20230201_v2-2-0", "sci_xrsf-l2-flsum_g18_d20230203_v2-2-0", "sci_xrsf-l2-flsum_g18_d20230206_v2-2-0", "sci_xrsf-l2-flsum_g18_d20230207_v2-2-0", "sci_xrsf-l2-flsum_g18_d20230208_v2-2-0", "sci_xrsf-l2-flsum_g18_d20230209_v2-2-0", "sci_xrsf-l2-flsum_g18_d20230211_v2-2-0", "sci_xrsf-l2-flsum_g18_d20230212_v2-2-0"])

for ii in np.arange(np.size(files18)):
	filnc = files18[ii] + ".nc"
	filfits = files18[ii] + ".fits"
	if not os.path.exists(filnc):
		with open(filnc,"wb") as f:
			print(url_path18 + filnc)
			r = requests.get(url_path18 + filnc)
			f.write(r.content)
			ff = nc.Dataset(filnc)
			time = np.array(ff["time"][:])
			flxB = np.array(ff["xrsb_flux"][:])
			bkgB = np.array(ff["background_flux"][:])
			cl = np.array(ff["flare_class"][:])
			intf = np.array(ff["integrated_flux"][:])
			flrid = np.array(ff["flare_id"][:])
			yy = cftime.num2pydate(ff.variables["time"][:], ff["time"].units)
			c1 = fits.Column(name='Time',array=time, format='D')
			c2 = fits.Column(name='PeakfluxB',array=flxB, format='F')
			c3 = fits.Column(name='BkgfluxB',array=bkgB, format='F')
			c4 = fits.Column(name='TotfluxB',array=intf, format='F')
			c5 = fits.Column(name='FlareClass',array=cl, format='5A')
			c6 = fits.Column(name='FlareID',array=flrid, format='16A')
			c7 = fits.Column(name='Date',array=yy, format='20A')
			t = fits.BinTableHDU.from_columns([c1,c2,c3,c4,c5,c6,c7])
			t.writeto(filfits,overwrite=True)
			print(filfits)

print("DONE")
