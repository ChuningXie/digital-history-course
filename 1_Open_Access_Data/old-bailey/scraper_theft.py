import pandas as pd
import xml.etree.ElementTree as ET
from pathlib import Path
import re

def extract_all_theft_cases(folder_path):
    theft_cases = []
    folder = Path(folder_path)
    
    xml_files = list(folder.rglob('*.xml'))
    total_files = len(xml_files)
    print(f"Starting deep parsing of {total_files} files...\n")
    
    if total_files == 0:
        print("No files found. Please check your folder path.")
        return pd.DataFrame()

    for index, filepath in enumerate(xml_files, 1):
        if index % 100 == 0 or index == total_files:
            print(f"Progress: Processed {index} / {total_files} files...")

        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            
            # Key Fix 1: Use '*' instead of 'div1' to extract cases whether they are hidden in div2 or div3
            trials = root.findall(".//*[@type='trialAccount']")
            
            for trial in trials:
                # ey Fix 2: A single case might have multiple offences. Extract all of them.
                categories = [tag.get('value') for tag in trial.findall(".//interp[@type='offenceCategory']")]
                
                # If any offence category in this case includes 'theft'
                if 'theft' in categories:
                    trial_id = trial.get('id', 'unknown')
                    
                    year_tag = trial.find(".//interp[@type='year']")
                    year = year_tag.get('value') if year_tag is not None else None
                    
                    # Extract all subcategories and join them with commas (to avoid missing 'receiving')
                    subcats = [tag.get('value') for tag in trial.findall(".//interp[@type='offenceSubcategory']")]
                    subcat_str = ", ".join(filter(None, subcats)) if subcats else 'unknown'
                    
                    defendant_tag = trial.find(".//persName[@type='defendantName']")
                    if defendant_tag is not None and defendant_tag.text:
                        defendant_name = "".join(defendant_tag.itertext()).strip().replace('\n', ' ')
                    else:
                        defendant_name = 'Unknown'
                        
                    gender_tag = trial.find(".//interp[@type='gender']")
                    gender = gender_tag.get('value') if gender_tag is not None else 'unknown'
                    
                    verdict_tag = trial.find(".//interp[@type='verdictCategory']")
                    verdict = verdict_tag.get('value') if verdict_tag is not None else 'unknown'
                    
                    punish_tag = trial.find(".//interp[@type='punishmentCategory']")
                    punishment = punish_tag.get('value') if punish_tag is not None else 'none'
                    
                    # Extract and clean the plain text
                    paragraphs = trial.findall(".//p")
                    text_pieces = ["".join(p.itertext()) for p in paragraphs]
                    full_trial_text_cleaned = re.sub(r'\s+', ' ', " ".join(text_pieces)).strip()
                    
                    theft_cases.append({
                        'Trial_ID': trial_id,
                        'Year': year,
                        'Defendant': defendant_name,
                        'Gender': gender,
                        'Offence_Subcategories': subcat_str,
                        'Verdict': verdict,
                        'Punishment': punishment,
                        'Trial_Text': full_trial_text_cleaned
                    })
        except ET.ParseError:
            print(f"File corrupted or format error. Skipping: {filepath.name}")
        except Exception as e:
            print(f"Unknown error while parsing {filepath.name}: {e}")
            
    return pd.DataFrame(theft_cases)

if __name__ == "__main__":
    XML_FOLDER_PATH = r"D:\HISTORY\teaching\2026S DIGITAL HISTORY\group_projects\old bailey\oldbailey\sessionsPapers"
    
    df = extract_all_theft_cases(XML_FOLDER_PATH)
    
    if not df.empty:
        print("\n=== Parsing Complete! ===")
        print(f"Extracted a total of {len(df)} theft-related cases!\n")
        
        # Automatically count 'Receiving' (receiving stolen goods) cases to verify against the website's numbers (5.462)
        receiving_df = df[df['Offence_Subcategories'].str.contains('receiving', na=False, case=False)]
        print(f"Out of these, there are {len(receiving_df)} 'Receiving' cases!\n")
        
        output_csv = "old_bailey_all_thefts.csv"
        df.to_csv(output_csv, index=False, encoding='utf-8-sig')
        print(f"The dataset with full text has been saved as {output_csv}")