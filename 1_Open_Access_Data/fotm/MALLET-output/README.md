# Topic Modeling Outputs (MALLET)

Welcome to the **MALLET Output** folder. 

This folder contains the pre-calculated results of running Topic Modeling on the individual *Freedom on the Move* (FOTM) runaway ads. Topic Modeling is a computational text analysis method that scans thousands of documents to find clusters of words (topics) that frequently appear together.

To show you how data cleaning impacts our historical analysis, I ran this model **twice**.

---

## The Two Analysis Runs

### Run 1: The Initial Model (Basic)
First, I ran the texts through MALLET using its default settings to find **20 topics** and show the **top 20 words**. 
* **The issue:** The results were dominated by obvious and generic words expected in a runaway ad (e.g., "reward," "dollars," "ranaway," "negro"). While accurate, these words overshadow the deeper historical details we want to investigate.
* **Files generated:** `fotm-keys.txt`, `fotm-composition.txt`, `fotm.mallet`, `fotm-state.gz`, `diagnostics.xml`.
1.1 Import our data to create a MALLET file for analysis next: bin\mallet import-dir --input sample-data\fotm_texts --output fotm.mallet --keep-sequence --remove-stopwords
### 1.2 Train Topics (we tell MALLET to find 20 topics based on our data): 

### Run 2: The Refined Model (Cleaned)
To dig deeper, I created a new list of "stopwords" in addition to the default English stopwords MALLET uses. By filtering out the generic ad terminology, the model was forced to look for more nuanced themes (like specific skills, clothing, or locations).
* **The Stopwords:** You can view the exact words I removed in the `fotm_stopwords.txt` file.
* **The Settings:** I ran the model again to find 20 topics, but this time asked it to show the **top 200 words** in each topic.
* **Files generated:** `fotm-keys-clean.txt`, `fotm-composition-clean.txt`, `fotm_clean.mallet`, `fotm-state-clean.gz`, `diagnostics-clean.xml`.

---

## File Guide: What should you look at?

You don't need to open every file. Here is a guide to what is useful for your assignments:

** Files to open and read (Plain Text/Excel):**
* **`fotm-keys-clean.txt`**: **(Start Here)** This shows the 20 topics from our refined run. Each line represents a topic and lists the most important words that define it. 
* **`fotm-composition-clean.txt`**: This shows how much of each topic is present in *each specific* runaway ad document.
* **`each_document_visualization.xlsx`**: A spreadsheet combining the composition data for easier reading and visualization.
* **`fotm_stopwords.txt`**: The custom list of common words excluded from the second run.

** Technical Files:**
* `.mallet` files: The compiled data format used internally by the MALLET software.
* `.gz` and `.xml` files: State and diagnostic files containing complex statistical logs from the algorithm's training process. **diagnostics files** are MALLET's own diagnosis on the quality of the topics it generates.

---

## How was this done?
Here are the exact command-line prompts I used to generate these files using the MALLET software:

**First Run Commands:**
```bash
# 1. Import data to create a MALLET file for analysis
bin\mallet import-dir --input sample-data\fotm_texts --output fotm.mallet --keep-sequence --remove-stopwords

# 2. Train topics (20 topics)
bin\mallet train-topics --input fotm.mallet --num-topics 20 --optimize-interval 20 --output-topic-keys fotm-keys.txt --output-doc-topics fotm-composition.txt --output-state fotm-state.gz --diagnostics-file diagnostics.xml

**Second Run Commands:**
```bash
# 1. Create a txt file called “fotm_stopwords.txt” under MALLET main folder. Input these new stopwrods & save:
reward dollars cents paid subscriber subscriber's delivery apprehension illegible years age aged feet inches high tall negro boy man fellow woman girl person master owner belongs property county state city jail ran ranaway runaway left forward prove charges law
# 2. Create a new MALLET file based on excluding default & customized stopwords:
bin\mallet import-dir --input sample-data\fotm_texts --output fotm_clean.mallet --keep-sequence --remove-stopwords --extra-stopwords fotm_stopwords.txt
# 3. Train topics again using the new MALLET file, but this time with top 200 words in each topic:
bin\mallet train-topics --input fotm_clean.mallet --num-topics 20 --optimize-interval 20 --num-top-words 200 --output-topic-keys fotm-keys-clean.txt --output-doc-topics fotm-composition-clean.txt --output-state fotm-state-clean.gz --diagnostics-file diagnostics-clean.xml
