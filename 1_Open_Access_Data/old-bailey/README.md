# Old Bailey Datasets & Scripts

Welcome to the **Old Bailey** folder for our Digital History course. 

This folder contains data extracted from *The Proceedings of the Old Bailey* (1674-1913), focusing specifically on **theft-related trials**. I have already processed and cleaned this data for you, so it is ready to be imported directly into our course tools (such as OpenRefine, Voyant, or Gephi).

## What's in this folder?

Here is a breakdown of the files you see above and how you should use them:

### 1. The Datasets (For your assignments)
These are the files you will actually download and use for your analysis.
* **`old_bailey_all_thefts.zip`**: **START HERE.** This is the main dataset containing thousands of theft cases with their full trial texts, defendant details, and verdicts. **Please download this ZIP file and extract (unzip) it** on your computer to access the large CSV file inside. 
* **`top_100_stolen_items.csv`**: A pre-calculated list of the 100 most frequently stolen items in our dataset, generated using Natural Language Processing (NLP). You can use this for quick reference or simple visualizations.

### 2. The Python Scripts (For demonstration)
You **DO NOT** need to run these scripts to complete your assignments. I have provided them here for transparency, so you can see exactly how historians use code to gather and clean data.
* **`scraper_theft.py`**: The script I wrote to dig through thousands of raw XML files and extract only the cases involving theft.
* **`items_stolen_v2.py`**: The NLP (Natural Language Processing) script that uses machine learning to automatically read the trial texts and identify exactly *what* was stolen (e.g., extracting "silver spoon" instead of just "spoon").

---

## How to Download the Data
1. Click on **`old_bailey_all_thefts.zip`** in the file list above.
2. On the next page, click the **Download** button (or the raw download icon) on the right side.
3. Once downloaded, **unzip** the file on your computer. You can now open the resulting CSV file or import it into your digital tools.

---


**Required Citation Format for the Old Bailey:**
This data is derived from *The Proceedings of the Old Bailey* and is provided under a **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** license. 

Whenever you reference this dataset in your work, you must include the following citation:
> Tim Hitchcock, Robert Shoemaker, Clive Emsley, Sharon Howard and Jamie McLaughlin, et al., *The Old Bailey Proceedings Online, 1674-1913* (www.oldbaileyonline.org, version 9.0, Autumn 2023).
