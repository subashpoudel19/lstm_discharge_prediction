import ee

# Initialize the Earth Engine library.
ee.Initialize()

# Define HUC-2 codes for the Mississippi River Basin.
mississippi_huc_codes = ['05', '06', '07', '08', '10', '11']

# Load the HUC-2 feature collection.
huc2 = ee.FeatureCollection("USGS/WBD/2017/HUC02")

# Filter for the Mississippi River Basin HUC codes.
mississippi_basin = huc2.filter(ee.Filter.inList('huc2', mississippi_huc_codes))

# Set up the export task to Google Drive.
export_task = ee.batch.Export.table.toDrive(
    collection=mississippi_basin,
    description='Mississippi_River_Basin_HUC2',
    fileFormat='SHP'
)

# Start the export task.
export_task.start()

print("Export started. Check your Google Drive for the file after the export completes.")
