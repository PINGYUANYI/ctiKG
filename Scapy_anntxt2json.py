import os 
import re
import json
import itertools
import spacy

nlp = spacy.load("en_core_web_sm")
#Takes in raw text and uses the SpaCy sentence parser to break it down into sentences

def getSpaCySentences(text):
    sentences = []
    doc = nlp(text)

    for word in doc:
        if word.is_sent_start:#Creat a new sentences if a SpaCy thinks a word is the start
            sentences.append([])
        if word.text.strip() != '':#Exclude words containing only whitespaces
            sentences[-1].append(word)
    return [sentence for sentence in sentences id sentence]#Excludes empty sentences
def getDocREDVertexSetFromBratAnnotations(text,annotation,sentences):
    vertexSet = []
    bratIDtoDocREDID = {}
    bratEntities = [] #{id,type,name,start,end}
    for line in annotation,splitlines(): #Process all BRAT
        if line[0] == "T": #Skips relation entries
        line = line.split("\t")
        bratEntities.append({"id":line[0],"type":line[1].split()[0].strip(),"name":line[2].strip(),"start":int(line[1],split()[1]),"end":int(line[1].split()[2])})
    bratEntities.sort(key = lambda entity: entity["start"])

    entity_id = 0
    sent_id = 0
    wordIDX = 0
    startPos = -1
    while sent_id <len(sentences) and entity_id < len(bratEntities):
        while wordIDX < len(sentences[sent_id]) and entity_id < len(bratEntities):
            if sentences[sent_id][wordIDX].idx + len(sentences[sent_id][wordIDX]) > bratEntities[entity_id]["start"] and sentences[sent_id][wordIDX].idx <= bratEntity[entity_id]["start"]:
                startPos = wordIDX
            if sentences[sent_id][wordIDX].idx + len(sentences[sent_id][wordIDX]) >= bratEntities[entity_id]["end"]:

            vertexSet.append([{
                "name""bratEntities[entity_id]["name"],
                "pos": [startPos,wordID+1],
                "sent_id": sent_id,
                "type": bratEntities[entity_id]["type"]
            }])

           bratIDtoDocREDID[bratEntities[entity_id["id"]] = entity_id

           entity_id += 1
           wordIDX = startPos
           startPos = -1
           continue
         wordIDX += 1
      if startPos != -1
         sentences[sentences[sent_id].extend(sentences[sent_id + 1])
         del sentences[sent_id + 1]
      else:
         sent_id += 1
         wordIDX = 0
  return bertexSet,bratIDtoDocRED

              
