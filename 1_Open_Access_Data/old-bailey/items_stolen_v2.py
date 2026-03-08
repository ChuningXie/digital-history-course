import pandas as pd
import spacy
from collections import Counter

print("Loading the NLP language model (this may take a few seconds)...")
# Load the English grammar model from spaCy
nlp = spacy.load("en_core_web_sm")

def extract_stolen_objects(text):
    """
    Extract stolen objects from the text.
    Logic: Find the "Direct Object" (Direct Object) of "theft-related verbs".
    """
    if not isinstance(text, str) or len(text.strip()) == 0:
        return []
    
    # Let spaCy parse the grammatical structure of the entire text
    doc = nlp(text.lower()) 
    stolen_items = []
    
    # Define our target verbs (spaCy automatically lemmatizes words, so we use the base form)
    target_verbs = {"steal", "take", "rob", "purloin", "filch", "carry"}
    
    for token in doc:
        # 1. Check if the word is a verb and if its lemma is in our target verbs list
        if token.pos_ == "VERB" and token.lemma_ in target_verbs:
            
            # 2. If yes, find the "direct object" (dobj) attached to this verb
            for child in token.children:
                if child.dep_ == "dobj":
                    
                    # 3. For precision, we also grab adjectives or noun modifiers preceding the object
                    # Example: Extract "silver spoon" instead of just "spoon"
                    modifiers = [w.text for w in child.lefts if w.dep_ in ["amod", "compound"]]
                    
                    # Combine the modifiers and the object
                    item_name = " ".join(modifiers + [child.text])
                    
                    # Exclude overly common pronouns or meaningless words
                    if item_name not in ["it", "them", "what", "which", "things"]:
                        stolen_items.append(item_name)
                        
    return stolen_items

if __name__ == "__main__":
    # Read the dataset we just created from the scraper script
    csv_file = "old_bailey_thefts_with_text.csv"
    print(f"Reading dataset: {csv_file}")
    df = pd.read_csv(csv_file)
    
    # Create a counter to tally the frequency of all items
    all_items_counter = Counter()
    
    print("Starting NLP syntax analysis and item extraction (this will take a little while)...")
    
    # Analyze Trial_Text row by row
    for index, row in df.iterrows():
        text = row['Trial_Text']
        items = extract_stolen_objects(text)
        
        # Add found items to the counter
        all_items_counter.update(items)
        
        # Print progress every 200 rows
        if (index + 1) % 200 == 0:
            print(f"Progress: Analyzed {index + 1} / {len(df)} cases...")

    print("\n=== Extraction Complete! ===")
    print("Top 20 Most Stolen Items in Old Bailey History:\n")
    
    # Print the top 20 most frequent items
    for item, count in all_items_counter.most_common(20):
        print(f"🔹 {item.ljust(20)} : {count} times")
        
    # (Optional) If you want to save the ranking to a CSV file, use the lines below:
    items_df = pd.DataFrame(all_items_counter.most_common(), columns=['Item', 'Count'])
    items_df.to_csv("top_stolen_items.csv", index=False)
    print("Ranking saved to top_stolen_items.csv")