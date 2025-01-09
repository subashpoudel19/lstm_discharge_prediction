import os
import pandas as pd
import re

def createfolder(path):
    os.makedirs(path, exist_ok=True)
def process_csv_file(file_path, parameter_name):
    try:
        df = pd.read_csv(file_path)
        df.rename(columns={df.columns[0]: parameter_name}, inplace=True)
        df['Date'] = pd.to_datetime(df['imageId'], format='%Y%m%d')
        third_column_name = df.columns[2]
        return df.pivot(index='Date', columns=third_column_name, values=parameter_name)
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame to handle gracefully


def process_files_in_folder(input_folder, output_folder):
    pattern = re.compile(r'^(?P<parameter>[\w_]+)_(?P<year>\d{4}).csv$')
    parameters_data = {}

    for file_name in os.listdir(input_folder):
        match = pattern.match(file_name)
        if match:
            parameter = match.group('parameter')
            file_path = os.path.join(input_folder, file_name)
            processed_df = process_csv_file(file_path, parameter)
            parameters_data.setdefault(parameter, []).append(processed_df)
    
    for parameter, data_frames in parameters_data.items():
        combined_df = pd.concat(data_frames).reset_index().sort_values(by='Date')
        combined_df.to_csv(os.path.join(output_folder, f'{parameter}.csv'), index=False)
        print(f"Combined data for {parameter} saved to {os.path.join(output_folder, f'{parameter}.csv')}")

# Example usage
input_folder = 'H:/My Drive/GEE_MRB'
output_folder = 'Data/GEE'
createfolder(output_folder)
process_files_in_folder(input_folder, output_folder)
