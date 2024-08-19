import re
import Responses as resp

def Mprobability (UserMess , RecWords , single = False , ReqWords = [] ):
    certainty = 0
    hasReqWords = True

    for word in UserMess :
        if word in RecWords:
            certainty +=1

    percent = float(certainty)/float(len(RecWords))

    for word in ReqWords:
        if word not in UserMess:
            hasReqWords = False
            break

    if hasReqWords or single:
        return int(percent*100)
    else:
        return 0

def CheckAll (Mess):
    highestProb = {}

    def Response (botResp , listWords , single = False , RecWords = []):
        nonlocal highestProb
        highestProb[botResp] = Mprobability(Mess, listWords , single , RecWords)

    Response(resp.Rgreet, ["hi" , "hey" , "hello"] , single=True)
    Response(resp.Rbye, ["bye","goodbye","buh bye"], single=True)
    Response(resp.Raskhow, ["how","are","you","doing"], RecWords=["how"])
    Response(resp.Rwelc,["thanks","thank"], single= True)
    Response(resp.Rsure,["can","i","ask","question"],RecWords=["i","ask","question"])

    Response(resp.Rsci1a, ["what","is","the","largest","planet","in","the","solar","system"], RecWords=["what","largest","planet","solar","system"])
    Response(resp.Rsci1b, ["what","is","jupiter"],RecWords=["what","jupiter"])
    Response(resp.Rsci2a, ["what","is","the","gas","that","plants","use","take","to","make","have","food"], RecWords=["what","gas","plants","food"])
    Response(resp.Rsci2b, ["what","is","carbon dioxide"], RecWords=["what","carbpn dioxide"])
    Response(resp.Rsci3a, ["what","do","bees","collect","from","flowers","to","make","honey"],RecWords=["what","bees","flowers","honey"])
    Response(resp.Rsci3b, ["what","is","nectar"],RecWords=["what","nectar"])
    Response(resp.Rsci4,["how","many","legs","does","on","a","spider","have"], RecWords=["how","many","legs","spider"])
    Response(resp.Rsci5a, ["what","is","the","process","when","plants","make","their","food","using","sunlight","plant"],RecWords=["what","plant","process","plants","food","sunlight"])
    Response(resp.Rsci5b, ["what","is","photosynthesis"],RecWords=["what","photosynthesis"])
    Response(resp.Rsci6a, ["what","is","the","at","center","of","an","atom"],RecWords=["what","center","atom"])
    Response(resp.Rsci6b, ["what","is","a","nucleas"],RecWords=["what","nucleas"])
    Response(resp.Rsci7a, ["what","is","the","force","that","makes","objects","pulls","down","to","earth"],RecWords=["what","force","down","earth"])
    Response(resp.Rsci7b, ["what","is","gravity"],RecWords=["what","gravity"])
    Response(resp.Rsci8a, ["what","is","the","main","gas","found","in","air","we","breathe"],RecWords=["what","main","gas","air"])
    Response(resp.Rsci8b, ["what","is","nitrogen"],RecWords=["what","nitrogen"])
    Response(resp.Rsci9a, ["what","planet","is","known","as","the","red"],RecWords=["what","red","planet"])
    Response(resp.Rsci9b, ["what","is","mars"],RecWords=["what","mars"])
    Response(resp.Rsci10, ["what","temprature","does","water","boil","at","boiling point"], RecWords=["what","boil","boiling point","water"])
    Response(resp.Rsci11a, ["what","is","the","part","of","plants","plant","absorbs","nutrients","from","soil"],RecWords=["what","plants","plants","nutrients","soil"])
    Response(resp.Rsci11b, ["what","is","are","root","roots"],RecWords=["what","root","roots"])
    Response(resp.Rsci12a, ["what","is","water","called","in","as","a","solid","state"],RecWords=["what","water","solid"])
    Response(resp.Rsci12b, ["what","is","ice"],RecWords=["what","ice"])
    Response(resp.Rsci13a, ["what","is","the","name","of","someone","who","studies","rocks","scientist"],RecWords=["what","studies","rocks"])
    Response(resp.Rsci13b, ["what","is","a","geologist"], RecWords=["what","geologist"])
    Response(resp.Rsci14, ["how","what","is","many","planets","are","the","in","our","the","solar","system","number","of"], RecWords=["how","many","what","number","planets","solar","system"])
    Response(resp.Rsci15a, ["what","is","the","smallest","unit","of","life"], RecWords=["what","smallest","unit","life"])
    Response(resp.Rsci15b, ["what","is","a","cell","cells","are"], RecWords=["what","cell","cells","is","are"])
    Response(resp.Rsci16a, ["what","is","the","chemical","symbol","of","water"], RecWords=["what","chemical","symbol","water"])
    Response(resp.Rsci16b, ["what","is","h2o"],RecWords=["what","h2o","is"])
    Response(resp.Rsci17a, ["what","is","the","closest","star","to","earth"],RecWords=["what","closest","star","earth"])
    Response(resp.Rsci17b, ["what","is","the","sun"],RecWords=["what","is","sun"])
    Response(resp.Rsci18a, ["what","are","animals","who","only","eat","plants","called","name","of","that"], RecWords=["what","animals","only","eat","plants"])
    Response(resp.Rsci18b, ["what","are","herbivores"], RecWords=["what","are","herbivores"])
    Response(resp.Rsci19, ["how","many","bones","in","a","human","adult","body","are","the"], RecWords=["how","many","bones","human","adult","body"])
    Response(resp.Rsci20a, ["what","is","the","organ","that","helps","make","us","breathe"], RecWords=["what","organ","breathe"])
    Response(resp.Rsci20b, ["what","are","lungs"],RecWords=["what","lungs","are"])






    AppropResp = max(highestProb, key= highestProb.get)
    return resp.NotAvail() if highestProb[AppropResp] < 1 else AppropResp


def getResp (userInput):
    splitMessage = re.split(r'\s+|[.!?;:,-]\s*', userInput.lower())
    response = str(CheckAll(splitMessage))
    return response

while True:
    print("Bot: " + getResp(input("User: ")))




