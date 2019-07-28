import os
import sys

# Get this directory path
thisPath = os.path.realpath('./')

# Get the parent folder path - os.sep for windows is '\\\\'
mainPath = os.sep.join(thisPath.split(os.sep)[:-1])

# Set the data folder path
dataPath = os.path.join(mainPath,'Data')

# Set the plots folder path
plotPath = os.path.join(mainPath,'Plots')

# Set the statistics folder path
statisticsPath = os.path.join(mainPath,'StatisticalResults')

# Set the scripts folder path
scriptsPath = os.path.join(mainPath,'Scripts')

# Set the outputs folder path
outputPath = os.path.join(mainPath,'Output')

# Create directories if they don't exist
for dtory in [dataPath,plotPath,statisticsPath,scriptsPath,outputPath]:
	if not os.path.isdir(dtory):
		print('Creating directory: {}'.format(dtory))
		os.mkdir(dtory)
