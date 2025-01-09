# Mississippi River Basin Data Analysis

This repository contains Python scripts and Jupyter Notebooks used for extracting, processing, and analyzing hydrological and meteorological data for the Mississippi River Basin.

## Table of Contents
- [File Descriptions](#file-descriptions)
- [Folder Structure](#folder-structure)
- [Usage](#usage)

## File Descriptions

1. **Step 1 Code to get Watershed shapefile.py**
   - **Purpose**: Extracts HUC2-level watershed shapefiles for the Mississippi River Basin using Google Earth Engine.
   - **Key Features**:
     - Filters HUC2 codes for the Mississippi Basin.
     - Exports the filtered shapefile to Google Drive in SHP format.

2. **Step 2 Code to get Satellite_and_other data from Google Earth Engine.py**
   - **Purpose**: Downloads climate and hydrological parameters from Google Earth Engine for specified regions and timeframes.
   - **Key Features**:
     - Supports annual data extraction (1980-2023) for parameters like precipitation, temperature, runoff, and evaporation.
     - Exports data as CSV files to Google Drive.

3. **Step 3 Code to process the GEE downloaded data.py**
   - **Purpose**: Processes and combines CSV files downloaded from Google Earth Engine.
   - **Key Features**:
     - Reads and pivots CSV files based on date and HUC2 codes.
     - Combines multiple yearly datasets into a single CSV file for each parameter.
     - Saves processed files to a specified output folder.

4. **Step 4 Code to get available discharge data from USGS.ipynb**
   - **Purpose**: Identifies and extracts available discharge data from USGS for specific stations in the Mississippi River Basin.

5. **Step 5 pycaret_for_filling_data.ipynb**
   - **Purpose**: Implements a PyCaret regression model to fill missing discharge data for the period 1980-2023.
   - **Key Features**:
     - Compares various regression models.
     - Outputs a completed dataset with predicted values for missing data.

6. **Step 6 Code for LSTM.ipynb**
   - **Purpose**: Builds an LSTM model to predict streamflow for selected stations.
   - **Key Features**:
     - Uses cleaned discharge data to train and validate the model.
     - Provides future predictions for streamflow based on historical patterns.

## Folder Structure
- **Input and Output Data Paths**: Specified in each script.
- **Output Files**: Include shapefiles, processed CSVs, and model results.

## Usage
Run the files in sequence for complete data processing and analysis. Each script or notebook is designed to perform specific tasks, and they should be executed in the order mentioned above.
