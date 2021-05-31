import spacy
import json
import re

nlp = spacy.load('en_core_web_sm')

cleansedFile = "rightMove1.json"
with open(cleansedFile, 'r') as myfile:
    data = json.load(myfile)

for aProperty in data:
    aProperty['currency'] = aProperty['price'][:3]
    aProperty['price'] = int(aProperty['price'][3:].replace(',' , ''))
    aProperty['price'] = int(aProperty['price'][3:].replace(',' , ''))
    aProperty['bedrooms'] = int(aProperty['BEDROOMS'].replace('x', ''))
    aProperty.pop(aProperty['BEDROOMS'])
    aProperty['size'] =  int(re.findall('[0-9]+', aProperty['SIZE']))
    aProperty['sizeUnit'] =  re.findall('[a-zA-Z]+', aProperty['SIZE'])
    aProperty['address'] = findThePostCodeDistrict
    
    # we start description NLP
    doc = nlp(a)
    noun_adj_pairs = []
    for i,token in enumerate(doc):
        if token.pos_ not in ('NOUN','PROPN'):
            continue
        for j in range(i+1,len(doc)):
            if doc[j].pos_ == 'ADJ':
                noun_adj_pairs.append((token,doc[j]))
                break
    aProperty['nounAdjectivePairs'] = str(noun_adj_pairs)
    


nlp = spacy.load('en_core_web_sm')
a = 'A rare opportunity to purchase a garage in Wandsworth.\r<b>Description</b>This is a rare opportunity to purchase one of five unique garages located just off Wandle Road. The garages are single storey and been complete re built within the last year with electricity being provided to each garage. They have private and secure access from behind Wandle Road.<b>Location</b>Wandle Road is a popular residential street close to the open space of Wandsworth Common and the wonderful shops and restaurants, including Chez Bruce, on Bellevue Road.  The area is renowned for its many good local schools and there are good transport links from Wandsworth Common mainline station directly into Victoria or by the Northern Line from Tooting Bec.Square Footage: 156 sq ft\rLeasehold with approximately 121 years remaining.'
doc = nlp(a)
noun_adj_pairs = []
for i,token in enumerate(doc):
    if token.pos_ not in ('NOUN','PROPN'):
        continue
    for j in range(i+1,len(doc)):
        if doc[j].pos_ == 'ADJ':
            noun_adj_pairs.append((token,doc[j]))
            break
noun_adj_pairs

# extract filter on schools restaurants shops transport station garden Bus Train Hospital Leisure
# keep the rest as text
