import pandas as pd

# Load the ODS file
ods_file_path = r'C:\Users\Stephan\Desktop\finaldataforstreamlit.ods'  # Update this to your file's path
df = pd.read_excel(ods_file_path, engine='odf')

# Define the output XLSX file path
xlsx_file_path = r'C:\Users\Stephan\Desktop\finaldataforstreamlit.xlsx'  # Update this to your desired output path

# Save the DataFrame as an XLSX file
df.to_excel(xlsx_file_path, index=False)

print(f"File has been converted and saved to {xlsx_file_path}")
