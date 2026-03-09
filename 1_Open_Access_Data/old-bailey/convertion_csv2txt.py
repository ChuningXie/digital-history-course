""" used to extract three column info from (Trial_ID Year Trial_Text) into individual txts for MALLET
    "Trial_ID_Year" is the document title & "Trial_Text" is the document content. """
    
import pandas as pd
import os
import re

# 1. Define File Paths
# Using 'r' before the string treats backslashes as literal characters (Raw String)
csv_path = r"D:\HISTORY\teaching\2026S DIGITAL HISTORY\group_projects\old bailey\test\old_bailey_all_thefts.csv"
output_folder = r"D:\HISTORY\teaching\2026S DIGITAL HISTORY\group_projects\old bailey\test\old_bailey_all_theft_txt_files"

def sanitize_filename(name):
    """Removes characters that are illegal in Windows filenames."""
    return re.sub(r'[\\/*?:"<>|]', "", str(name))

def split_csv_to_txt():
    # 2. Check if the output directory exists; if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created directory: {output_folder}")

    try:
        # 3. Load the dataset
        # We specify encoding='utf-8' to handle historical text characters correctly
        df = pd.read_csv(csv_path)
        print(f"Successfully loaded CSV with {len(df)} rows.")

        # 4. Iterate through each row in the DataFrame
        for index, row in df.iterrows():
            # Extract data from columns
            trial_id = sanitize_filename(row['Trial_ID'])
            year = sanitize_filename(row['Year'])
            trial_text = str(row['Trial_Text'])

            # 5. Construct the filename (Combining Trial_ID and Year)
            file_name = f"{trial_id}_{year}.txt"
            file_save_path = os.path.join(output_folder, file_name)

            # 6. Write the Trial_Text to the individual .txt file
            with open(file_save_path, 'w', encoding='utf-8') as f:
                f.write(trial_text)

        print(f"Process complete. Files are located in: {output_folder}")

    except FileNotFoundError:
        print("Error: The CSV file was not found. Please check the path.")
    except KeyError as e:
        print(f"Error: Column name {e} not found. Check if CSV headers match exactly.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    split_csv_to_txt()