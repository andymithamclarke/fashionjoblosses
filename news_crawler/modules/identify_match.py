# =========================
# Identify key phrases within a segment of article text
# =========================



# =============
#  IMPORTS 
# =============

# General Imports
import spacy

# Module imports
from news_crawler.modules import keyword_dictionary as keyword_dictionary

# Load Spacy Models
nlp_english = spacy.load("en_core_web_sm")

# =============
#  The Function
# =============

def identify_keywords_entities_numbers(dictionary):
    
    # Define an empty keyword matches list
    keyword_matches = []

    # Define an empty entities list
    entities_mentioned = []

    # Define an empty entities list
    numbers_mentioned = []

    # =============
    #  IDENTIFY KEYWORDS
    # =============

    keyword_list = keyword_dictionary.job_loss_keyword_dictionary[dictionary['language']]
        
    # Loop through saved keywords and identify a match with the article phrase
    for word in keyword_list:
        if word in dictionary['phrase']:
            keyword_matches.append(word)


    # =============
    #  IDENTIFY ENTITIES
    # =============

    doc = nlp_english(dictionary['phrase'])

    for ent in doc.ents:
        if str(ent.label_) == "PERSON" or str(ent.label_) == "ORG":
            entities_mentioned.append(str(ent))


    # =============
    #  IDENTIFY NUMBERS
    # =============

    for ent in doc.ents:
        if str(ent.label_) == "CARDINAL":
            numbers_mentioned.append(str(ent))


    # =============
    #  ADD RESULTS TO ORIGINAL DICTIONARY AND RETURN
    # =============
    
    # Add the flattened keyword_matches list to a new key in the dictionary
    dictionary['keywords'] = [y for x in keyword_matches for y in x]

    # Add the flattened entities_mentioned list to a new key in the dictionary
    dictionary['entities_mentioned'] = [y for x in entities_mentioned for y in x]

    # Add the flattened numbers_mentioned list to a new key in the dictionary
    dictionary['numbers_mentioned'] = [y for x in numbers_mentioned for y in x]
    

    # Return the dictionary to be filtered and processed in the pipeline
    return dictionary


