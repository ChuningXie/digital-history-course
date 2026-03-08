# A Minimalist Guide to Running MALLET on Mac (No Environmental Variables Required)

If you are a Mac user, you do not need to worry about setting up complex "Environmental Variables" or "Paths" like Windows users sometimes do. Please do not install a Windows virtual machine; your Mac is perfectly capable of running these tools natively.

By using a simple drag-and-drop trick in your Terminal, you can bypass system configurations and get straight to analyzing your data. Just follow these three simple steps:

## Step 1: Check if Java is Installed

MALLET requires Java to run. While it is not always pre-installed on modern Macs, checking for it and installing it is very straightforward.

1. Open your **Terminal** (Press `Cmd + Spacebar`, type `Terminal`, and hit Enter).
2. Type the following command and press Enter:
   ```bash
   java -version
   ```
3. **Review the Result:** * If the terminal outputs a version number (e.g., `java version "1.8.0_..."`), Java is active and you are good to go. 
   * If it says "command not found" and a Mac pop-up asks if you want to install it, simply follow the prompts to install the basic Java package or download & install an up-to-date java version of your choice.

---

## Step 2: The "Drag-and-Drop" Navigation Trick

Because we skipped the Environmental Variables setup, your computer does not automatically know where the MALLET software is located. We need to manually point your Terminal to that specific folder.

1. Unzip the `mallet-2.0.8` folder you downloaded (for example, keep it in your Downloads folder).
2. In your Terminal, type `cd ` (**Important:** Make sure to type a single **space** after 'cd').
3. Open your Mac's **Finder** and locate the unzipped `mallet-2.0.8` folder.
4. Click and **drag that folder directly into the Terminal window**. The exact file path will automatically populate in the text line.
5. Hit **Enter**. You are now "inside" the MALLET directory and ready to run the tool.

---

## Step 3: Mac Execution Commands

Because Mac and Windows operating systems read file paths differently, you need to make a tiny adjustment to the commands provided in the main tutorial. 

* **Change the slashes:** Mac uses forward slashes (`/`).
* **Add a dot:** You must add `./` at the very beginning to tell your Mac to run the program located inside the current directory.
* **Rule of thumb:** Whenever the main instructions say `bin\mallet`, Mac users must type `./bin/mallet`.

Here are your exact Mac-friendly commands for our two Topic Modeling runs. You can copy and paste these directly into your Terminal once you have completed Step 2.

### Mac Version: First Run Commands

```bash
# 1. Import data
./bin/mallet import-dir --input sample-data/fotm_texts --output fotm.mallet --keep-sequence --remove-stopwords

# 2. Train topics (20 topics)
./bin/mallet train-topics --input fotm.mallet --num-topics 20 --optimize-interval 20 --output-topic-keys fotm-keys.txt --output-doc-topics fotm-composition.txt --output-state fotm-state.gz --diagnostics-file diagnostics.xml
```

### Mac Version: Second Run Commands (Cleaned)

*Note: Make sure you have already created your `fotm_stopwords.txt` file and saved it in the main MALLET folder as instructed in the main guide.*

```bash
# 1. Import data with custom stopwords
./bin/mallet import-dir --input sample-data/fotm_texts --output fotm_clean.mallet --keep-sequence --remove-stopwords --extra-stopwords fotm_stopwords.txt

# 2. Train topics again (with top 200 words)
./bin/mallet train-topics --input fotm_clean.mallet --num-topics 20 --optimize-interval 20 --num-top-words 200 --output-topic-keys fotm-keys-clean.txt --output-doc-topics fotm-composition-clean.txt --output-state fotm-state-clean.gz --diagnostics-file diagnostics-clean.xml
```
