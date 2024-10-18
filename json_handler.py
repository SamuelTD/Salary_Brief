import json

def GetEmployeesDictionary() -> dict:
    """
    Load the lists of employees from json file. Return a dictionary where keys are subsidiaries' names.
    Each value is a list of dictionaries, each dictionaries holding one employee's informations.    
    """
    with open("employes_data.json") as json_file:       
        return json.load(json_file)