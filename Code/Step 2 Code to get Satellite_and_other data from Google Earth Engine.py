import ee

class DataExporter:
    def __init__(self, aoi_id, dataset_id, parameters, start_year, end_year):
        # Initialize the Earth Engine
        ee.Initialize(project = 'ee-074bce151')
        
        # Set instance attributes
        self.AOI = ee.FeatureCollection(aoi_id)
        self.dataset_id = dataset_id
        self.parameters = parameters
        self.start_year = start_year
        self.end_year = end_year

    def export_data(self):
            # Access the dataset
            dataset = ee.ImageCollection(self.dataset_id)
            
            # Loop through years and parameters for data export
            for year in range(self.start_year, self.end_year + 1):
                for parameter in self.parameters:
                    
                    # Set up the time range
                    start_date = ee.Date.fromYMD(year, 1, 1)
                    end_date = ee.Date.fromYMD(year + 1, 1, 1)
                    
                    # Filter dataset for the given time range and select the parameter
                    filtered_collection = dataset.filterDate(start_date, end_date).select(parameter)
                    
                    # Define a function for mapping over the filtered collection
                    def map_function(image):
                        return image.reduceRegions(
                            reducer=ee.Reducer.mean().setOutputs([parameter]),
                            collection=self.AOI,
                            scale=250
                        ).map(lambda feature: feature.set('imageId', ee.String(image.id())))
    
                    # Flatten the results and prepare for export
                    feature_collection = filtered_collection.map(map_function).flatten()
    
                    selectors = [parameter, 'imageId', 'huc2']
                    
                    # Set up the export task
                    task = ee.batch.Export.table.toDrive(
                        collection=feature_collection,
                        description=f'{parameter}_{year}',
                        folder='GEE_MRB',
                        fileNamePrefix=f'{parameter}_{year}',
                        fileFormat='CSV',
                        selectors=selectors
                          # Add other needed properties
                    )
                    task.start()
                    print(f'Exporting {parameter} for year {year} to Drive...')

exporter = DataExporter(
    'users/074bce151saurav/MRB_HUC2',
    "ECMWF/ERA5_LAND/DAILY_AGGR",
    [
        'temperature_2m', 'dewpoint_temperature_2m', 'soil_temperature_level_1', 'soil_temperature_level_2', 'soil_temperature_level_3', 'soil_temperature_level_4', 'surface_pressure', 'total_precipitation_sum', 'surface_runoff_sum', 'sub_surface_runoff_sum', 'evaporation_from_vegetation_transpiration_sum', 'potential_evaporation_sum', 'surface_solar_radiation_downwards_sum', 'surface_net_thermal_radiation_sum', 'u_component_of_wind_10m', 'v_component_of_wind_10m', 'surface_latent_heat_flux_sum', 'snow_depth', 'snow_depth_water_equivalent', 'surface_net_solar_radiation_sum'
    ],
    1980,
    2023
)
exporter.export_data()