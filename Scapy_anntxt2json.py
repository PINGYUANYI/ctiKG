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

def getDocREDlabels(text,annotation,vertexSet,bratsIDtoDocREDID,relInfo):
    labels =[]
    for line in annotation.splitlines():
        if line[0] != "R": #Skip entity entries
            continue
        line = line.split('\t')[1].split()
    
        r = list(relInfo.key())[list(relInfo.values()),index(line[0].lower())] #Find the relationship ID use the DocReed
        h = bratsIDtoDocREDID[line[1].split(':')[1]]
        t = bratsIDtoDocREDID[line[2].split(':')[1]]
        evidence = set()
        for vertex in itertools.chain(vertexSet[h],vertexSetp[t]):
            evidence.add(vertex['sent_id'])
        evidence = sorted(evidence)
        labels.append({
            "r":r,
            "h":h,
            "t":t,
            "evidence":evidence
        })
    return labels
def getDocREDDocumentObject(textFilePath,annotationFilePath,relInfoFilePath):
    with open(textFilePath,'r',encoding = 'utf-8') as textFile,open(annotatioFilePath,'r',encoding = 'utf-8') as annotationFile,open(relInfoFilePath,'r',encoding = 'utf-8')  as relInfoFile:
    text = textFile.read()
    annotation = annotationFile.read()
    sentences = getSpaCySentences(text)
    vertexSet,bratIDtoDocREDID = getDocREDVertexSetFormBratAnnotations(text,anntation,sentences)
    labels = getDocREDlabels(text,annotation,vertexSet,bratsIDtoDocREDID,json.load(relInfoFile))
    documentObject = {
        "vertexSet": vertexSet,
        "labels":labels,
        "titile":os.path.splitext(os.path.normpath(textFilePath)))[0],
        "sents": [[word.text for word in sentence] for sentence in sentence] #Get the text from the SpaCy
     }
    return documentObject
if __name__ == "__main__": #输出anotation_data.json到Preprocessing文件，目的就是从ann文件映射到json文件中，第一步是getSpaCySentences提取txt中的每个句子到sentences中，第二步为getDocREDVertexSetFromBratAnnotations从Brat标记的ann映射到能被DocRED读取的json格式，创建vertext顶点集存储实体的一些起点终点和name的信息，第三步getDocREDlabels存储关系的信息，最后就根据映射的顶点集进行文件的输出。
        documents = []
        for filename in os.listdir("input/annotations"):
            if filename[0] != '.':
                annotationFilePath = "input/annotations/" + filename
                textFilePath = "input/text/" + os.path.splitext(filename)[0] + ".txt"
                print(textFilePath)
                documents.append(getdocREDDocumentObject(textFilePath,annotationfilePath,"rel_info.json"))
        with open("../Preprocessing/annotated_data.json",'w',encoding = 'utf-8') as file:
            json.dump(documents,file)
            
