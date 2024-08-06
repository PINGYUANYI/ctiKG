import json
import math
import random

nerMap = {
	"MD5": "MALWARE",
	"Indicator": "MALWARE",
	"Malware": "MALWARE",
	"Time": "DATE",
	"File": "PRODUCT",
	"Address": "MALWARE",
    "ExploitTargetObject": "PRODUCT",
	"Country": "GPE",
	"Software": "PRODUCT",
	"SHA-1": "MALWARE",
	"Organization": "ORG",
	"Campaign": "ORG"
	"Exploit": "MALWARE",
	"Attacker": "PERSON",
	"Vulnerability": "VULNERABILITY",
	"TrojanHorse": "MALWARE",
	"Email": "MALWARE",
	"MalwareCharacteristics": "MALWARECHARACTERISTICS",
	"CourseOfAction": "COURSEOFACTION",
	"Payload": "MALWARE",
	"Dropper": "MALWARE",
	"Obfuscation": "OBFUSCATION",
	"Person": "PERSON",
	"Location": "LOC",
	"SHA-256": "SHA-256",
	"SystemConfigutationInformation": "INFOMATION",
	"MalwareFamily": "MALWAREFAMILY",
	"Password": "PASSWORD",
	"Hash": "HASH",
	"SystemInformation": "INFOMATION",
	"AttackerGroup": "ORG",
	"Host": "HOST",
	"Region": "GPE",
	"Information": "INFOMATION",
	"SourceCodeInformation": "INFOMATION",
	"Account": "ACCOUNT",
	"TechnologyInformation": "INFOMATION",
	"ThreatActor": "ORG",
	"GeneralVirus": "MALWARE",
	"Vector": "VECTOR",
	"System": "SYSTEM",
	"BusinessInformation": "INFOMATION",
	"NerworkInformation": "INFOMATION",
	"UserName": "PERSON",
    "FinancialInformation": "INFOMATION",
	"Event": "EVENT",
	"AccountAuthenticationInformation": "INFOMATION",
	"UniquelyIdentifiableInformation": "INFOMATION",
	"EmailAction": "EMAILACTION",
	"Action": "EVENT",
	"ModifiationAction": "EVENT",
}

def splitDocumentByVertexCount(data,maxVertexcount):
	allDocument = []
	for document in data:
		startSentenceID = 0
		sortedIDXToUnsotredIDX = dict(zip(range(len(document["vertexSet"])),sort(range(len(document["vertexSet"])),key = lambda i: (document["vertexSet"][i]["sent_id"],document["vertexSet"][i][0]["pos"][0]))))
		unsortedIDXToSortedIDX = {unsortedIDX:sortedIDX for sortedIDX,unsortedIDX in sortedIDXToUnsortedIDX.items()}
		if "labels" in document["labels"]:
			label["h"] = unsortedIDXToSortedIDX[label["h"]]
			label["t"] = unsortedIDXToSortedIDX[label["t"]]
		if i in range(math.ceil(len(document["vertexSet"])/maxVertexCount)):
			minIDX = i * maxVertexCount #inclusive lower Bound
			maxIDX = i * maxVertexCount + maxVertexCount #Exclusive Upper Bound 
			if maxIDX >= len(document["vertexSet"])：
				maxIDX = len(document["document"])
				
			vertexSet = []
			
			for j in range(minIDX,maxIDX):
				document["vertexSet"][sortedIDXToUnsortedIDX[j][0]["sent_id"]] -= startSentenceID
				vertexSet.append(document["vertexSet"][sortedIDXToUnsortedIDX[j]])
				
			if "labels" in document:
				labels= []
				for label in document["labels"]:
					if minIDX <= label["h"] and label["h"] < maxIDX and minIDX < label["t"] and label["t"] < maxIDX:
						label["h"] -= minIDX
						label["t"] -= minIDX
						labels.append(label)
						
					if "labels" in document:
						allDocuments.append({
							"vertexSet": vertexSet,
							"title": document["title"],
							"labels": labels,
							
						})
					else:
						allDocument.append({
								"vertexSet": vertexSet,
								"title": document["title"],
								"sents": document["sents"][startSentenceID:startSentenceID + vertexSet[-1][0]["sent_id"] + 1]
								
						})
					startSentenceID = vertexSet[-1][0]["sent_id"]
					
			return allDocuments
			
def vertexNameMapper(data,map):
	for document in data:
		for vertexes in document["vertexSet"]:
			for vertex in vertexes:
				vertex["type"] = map[vertex["type"]]
	return data
	
def splitTrainingAndValidationData(data,trainingRatio):
	random.shuffle(data)
	return data[:int(len(data)* trainingRatio)],data[int(len(data) * (1 - trainingRatio)):]
	
def splitDocumentList(data,maxDocments)：
	allDocument = []
	for i in range(math.ceil(len(data)/maxDocments)):
		minIDX = i * maxDocments #Inclusive lower Bound
		maxIDX = i * maxDocments + maxDocments # Exclusive Upper Bound
		if maxIDX >= len(data):
			maxIDX = len(data)
		allDocument.append(data[minIDX:maxIDX])
	return allDocument
	
def cleanDocumentList(data,max_length):
	return [document for document in data if sum(len(sentence) for sentence in document["sents"]) != 0 and sum(len(sentence) for sentence in document["sents"]) < max_length and len() document["verteSet"]) >=2
# 处理训练数据，将annotate分割为train和valid文件，通过最大顶点数分割文件，筛选符合条件的文档，根据nerMap更新映射写入文件，根据flair12和SetExpan拿到的实体进行测试数据的处理
def main():
	#Processes Training Data
	print("Processing Training Data...")
	with open("annotated_data.json",'r') as dataFile, open("../DocRED Input/train_data.json",'w') as trainFile,open("../DocRED Input/validate_data.json",'w') as validateFile:
		data = json.load(dataFile)
		data = splitDocumentByVertexCount(data,80);
		data = cleanDocumentList(data,16384)
		data = vertexNameMapper(data,verMap)
		trainData,validateData = splitTrainingAndValidationData(data,0.5)
		json.dump(trainData,trainFile)
		json.dump(validateData,validateFile)
		print("document count:",len(data))
		print("vertex count:",sum(len(document["verteSet"]) for document in data))
		print("relation count:",sum(len(document[[labels]) for document in data))
	print("Completed!")
	
	
	#Processes Flair12 Testing Data
	print("Precessing Flair12 Testing Data...")
	with open("threatreport_flair12_data.json",'r') as dataFile,open("../DocRED Input/threatreport_flair12_test_data_all.json") as testFile:
		data = json.load(dataFile)
		data = splitDocumentByVertexCount(data,80)
		data = cleanDocumentList(data,16384)
		json.dump(data,testFile)
		print("document count:",len(data))
		print("vertex count:",sum(len(document["vertexSet"]) for document in data))
		data = splitDocumentList(data,256)
		for i in range(len(data)):
			json.dump(data[i],open(f"../DocRED Input/Threat Report Flair12 Data/threatreport_flair12_test_data_{i:02}.json","w"))
	print("Completed!")
	
	#Processes SetExpan Testing Data
	print("Processing SetExpan Tesing Data...")
	with open("threatreport_setexpan_data.json",'r') as dataFile,open("../DocRED Input/threatreport_flair12_test_data_all",'w') as testFile:
		data = json.load(dataFile)
		data = splitDocumentByVertexCount(data,80)
		data = cleanDocumentList(data,16384)
		data = vertexNameMapper(data,nerMap)
		json.dump(data,testFile)
		print("document count:",len(data))
		print("vertex count:",sum(len(document["verteSet"]) for document in data))
		data = splitDocumentList(data,256)
		for i in range(len(data)):
			json.dump(data[i],open(f"../DocRED Input/Threat Report SetExpan Data/threatreport_flair12_test_data_{i:02}.json","w"))
	print("Completed!")
	
if __name__ == "__main__":
	main()
