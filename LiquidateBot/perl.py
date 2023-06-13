from config import configIns
from rpc import rpcIns

def getliquidationIncentiveMantissa():
    response = rpcIns.callmethod(configIns.config.get("ControllerAddress"), "getliquidationIncentiveMantissa", [])
    return (response["stack"][0]["value"])

# getliquidationIncentiveMantissa
# getCloseFactor
# getAccountSupplyData
# getAccountBorrowData
