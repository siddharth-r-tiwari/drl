import os
import scipy.io
import pandas as pd

# Path to the directory containing .mat files
directory_path = 'data/'

# List all files in the directory
mat_files = [filename for filename in os.listdir(directory_path) if filename.endswith('.mat')]

for mat_file in mat_files:
    # Load .mat file
    mat = scipy.io.loadmat(os.path.join(directory_path, mat_file))
    mat = {k: v for k, v in mat.items() if k[0] != '_'}
    
    # Create a DataFrame
    data = pd.DataFrame({k: pd.Series(v[0]) for k, v in mat.items()})
    
    # Save as .csv
    csv_file_name = os.path.splitext(mat_file)[0] + '.csv'
    data.to_csv(os.path.join(directory_path, csv_file_name), index=False)

print("Conversion complete.")