import json
import requests
import time
from utils import logger

headers={'content-type': 'application/json'}
sender_address = "NQAPVXn7LhJoXvRSdVQAd7oKUpNKiSusNr"

class rpc:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def sendRawTx(self,rawtx):
        data = {
            "jsonrpc": "2.0",
            "method": "sendrawtransaction",
            "params": [rawtx],
            "id": 1
            }
        responseData = self.sendRequest(data)
        return responseData.get("result")
    
    def sendRequest(self, data, log=True):
        logger.loggerInstance.log(json.dumps(data,indent=4))
        # print(json.dumps(data, indent=4))
        response = requests.post(self.endpoint, data = json.dumps(data), headers = headers, timeout=10)
        responseData=response.json()
        if(log == True):
            # print(json.dumps(responseData,indent=4))
            logger.loggerInstance.log(json.dumps(responseData,indent=4))
        return responseData

    def getapplicationlog(self, txid):
        data = {
            "jsonrpc": "2.0",
            "method": "getapplicationlog",
            "params": [txid],
            "id": 1
            }
        responseData = self.sendRequest(data)
        return responseData.get("result")

    def getcontractstate(self,contracthash):
        data = {
            "jsonrpc": "2.0",
            "method": "getcontractstate",
            "params": [contracthash],
            "id": 1
            }
        responseData = self.sendRequest(data, False)
        return responseData.get("result")      

    def openwallet(walletname, password):
        data = {
            "jsonrpc": "2.0",
            "method": "openwallet",
            "params": [walletname,password],
            "id": 1
        }
        response = requests.post(self.endpoint, data = json.dumps(data), headers = headers, timeout=10)
        responseData=response.json()
        return responseData.get("result")      

    def callmethod(contract_hash, method, paramsArray, caller=sender_address, witnesscope="CalledByEntry"):
        realParamsArray = self.findmethod(contract_hash, method, paramsArray)
        if(witnesscope == "CalledByEntry"):
            scope = [
                        {	"account":caller,
                            "scopes":"CalledByEntry"
                        }
                    ]    
        else:
            scope = witnesscope
        data =  {
                "jsonrpc": "2.0",
                "method": "invokefunction",
                "params": [contract_hash,method,realParamsArray,scope
                ],
                "id": 1
        }
        responseData = self.sendRequest(data)
        return responseData["result"]


    def findmethod(self,contract_hash, method, parameters, usebuffer=False):    
        raw_result = self.getcontractstate(contract_hash)
        methods = raw_result["manifest"]["abi"]["methods"]
        result_array = []
        for item in methods:
            if item["name"] == method and len(item["parameters"]) == len(parameters):
                for i in range(len(item["parameters"])):
                    if(item["parameters"][i]["type"] != "Any" and item["parameters"][i]["type"] != "ByteArray"):
                        result_array.append({"type": item["parameters"][i]["type"], "value": parameters[i]})
                    else:
                        result_array.append({"type": "String", "value":  parameters[i]})    
        return result_array

    def wait(self, seconds = 17):
        time.sleep(seconds)

rpcIns = rpc("http://localhost:20332")        