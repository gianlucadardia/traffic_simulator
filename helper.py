import json  
import datetime  
import random  
import time
from  variables import FAULTYPE, ROTTEN_UUID, DEBUG
from scipy.stats import truncnorm
import numpy as np
import random


minimal_row = {
    "NODE_UUID": "",  # Placeholder
    "TIMESTAMP": "",  # Placeholder  
    "SEVERITY": "", #placeholder  
    "FAULT_TYPE": "" #placeholder
}


minimal_incident = {
    "Number":"", #placeholder
    "NODE_UUID": "",  # Placeholder
    "State":"", #placeholder
    "Short_description":"", #placeholder
    "Priority":"", #placeholder
    "Opened": "", #placeholder
    "Causale_chiusura_TLC":"",
    "Block_type_TLC":"",
    "External_ticket_ID":""
    
    #State 
    #["Accepted"]
    
    #Short_description
    #["No Connessione","cambio voip","No Fex","UP senza rete","Problema fax","LIENA BACKUP DOWN","no switch","router primario down"]
    
    #Priority
    #["1 - Critical","2 - High","3 - Moderate","4 - Low","5 - Planning"]
    
    #Number
    #gnerate ID
    
    #Opened (TImestamp)


}

short_descirption_arr=["No Connessione","cambio voip","No Fex","UP senza rete","Problema fax","LIENA BACKUP DOWN","no switch","router primario down"]
priority_arr=["1 - Critical","2 - High","3 - Moderate","4 - Low","5 - Planning"]


def get_rnd_element(_array):
    if not _array:
        return None  # Return None if the array is empty
    return random.choice(_array)

def generate_unique_id():
    timestamp = int(time.time())  # Current time in milliseconds
    return f"INC{timestamp}"

def generate_gaussian_random():
    mean = 0.8
    std_dev = 0.1
    lower, upper = 0, 1
    return round(truncnorm(
        (lower - mean) / std_dev, (upper - mean) / std_dev, loc=mean, scale=std_dev
    ).rvs(),1)

def load_ref_ids(file_path):
    with open(file_path, 'r') as file:
        ref_ids = [line.strip() for line in file]
        return ref_ids

def select_random_ref_ids(ref_ids, num_ids):
    return random.sample(ref_ids, num_ids)

def rnd_fault_type():
    return random.choice(FAULTYPE)

def generate_nodeuuid_severity_events(_nodeuuids,_severity,_faulttype):
    rows = []
    current_time = datetime.datetime.utcnow()  
    
    for nodeuuid in _nodeuuids:
        row = minimal_row.copy() 
        row["TIMESTAMP"] = current_time.isoformat() + "Z" 
        row["NODE_UUID"] = nodeuuid
        row["SEVERITY"] = _severity
        row["FAULT_TYPE"] = _faulttype
        rows.append(row)
    
    if DEBUG:
        print("Number of " + _severity + " rows generated: " +str(len(rows)))

    return rows

def generate_incidents(_nodeuuids,_severity,_incidenttype):
    incidents = []
    current_time = datetime.datetime.utcnow() 
    f_current_time = current_time.strftime("%Y-%m-%dT%H:%M:%S")
    
    for nodeuuid in _nodeuuids:
        incident = minimal_incident.copy() 
        incident["Number"] = generate_unique_id()
        incident["NODE_UUID"] = nodeuuid
        incident["State"] = "Accepted"
        incident["Short_description"] = get_rnd_element(short_descirption_arr)
        incident["Priority"] = get_rnd_element(priority_arr)
        incident["Opened"] = f_current_time 
        incident["Causale_chiusura_TLC"] = ""
        incident["Block_type_TLC"]=""
        incident["External_ticket_ID"]=""


        incidents.append(incident)
    
    #if DEBUG: print("Number of " + _severity + " incident generated: " +str(len(incidents)))

    return incidents

def generate_nodeuuid_rndcritical_events(_nodeuuids,_severity,_faulttype):
    rows = []
    current_time = datetime.datetime.utcnow()  
    
    for nodeuuid in _nodeuuids:
        row = minimal_row.copy() 
        row["TIMESTAMP"] = current_time.isoformat() + "Z" 
        row["NODE_UUID"] = nodeuuid
        row["SEVERITY"] = _severity
        row["FAULT_TYPE"] = rnd_fault_type()
        rows.append(row)
    
    if DEBUG:
        print("Number of critical rows generated: " +str(len(rows)))

    return rows



def split_array(main_array, split_ratio):
    array1 = main_array.copy()
    array2 = random.sample(array1, int(len(main_array) * split_ratio))
    array1 = [item for item in array1 if item not in array2]
    return array1, array2


def take_random_nodeuuid(_nodeuuid):

    # Calculate the number of elements to take
    num_elements_to_take = int(len(_nodeuuid) * generate_gaussian_random())
    print(f"Taking {num_elements_to_take} random elements")

    # Generate random indices
    random_indices = np.random.choice(len(_nodeuuid), num_elements_to_take, replace=False)
    
    # Select elements based on random indices
    random_nodeuuid = [_nodeuuid[i] for i in random_indices]
    
    return random_nodeuuid


def define_nodeuuids_to_work_with():
    # Load nodeuuids from a file
    nodeuuids = load_ref_ids('data/nodeuuid.txt')
    if DEBUG:
        print("Current nodes are: " + str(len(nodeuuids)))


    #delete rotten uuids from the list
    nodeuuids = [uuid for uuid in nodeuuids if uuid not in ROTTEN_UUID]

    if DEBUG:
        print("Deleted ROTTEN nodeuuid -  Current nodes are: " + str(len(nodeuuids)))

    # split based on given ratio , given array in two separate array.
    # Second array is %ratio of the first array
    split_ratio = 0.1
    node_ok, node_critical = split_array(nodeuuids, split_ratio)

    if DEBUG:
        print("Splitting nodes based on ratio: " + str(split_ratio))
        print("OK nodes are: " + str(len(node_ok)))
        print("Critical nodes are: " + str(len(node_critical)))


    # Select random nodeuuids
    rnd_ok_nodeuuids = take_random_nodeuuid(node_ok)
    rnd_critical_nodeuuids = take_random_nodeuuid(node_critical)

    if DEBUG:
        print("Random OK nodes are: " + str(len(rnd_ok_nodeuuids)))
        print("Random Critical nodes are: " + str(len(rnd_critical_nodeuuids)))

    return rnd_ok_nodeuuids, rnd_critical_nodeuuids

def generate_incidents_from_critical_nodes(_critcalnodes):

    print ("------------GENERATING INCIDENTS START---------------------")
    print(_critcalnodes)

    split_ratio = 0.1
    node_no_incidents, node_yes_incidents = split_array(_critcalnodes, split_ratio)

    if DEBUG:
        print("Splitting nodes based on ratio: " + str(split_ratio))
        print("Nodes withous incidents are: " + str(len(node_no_incidents)))
        print("Node with incidents  are: " + str(len(node_yes_incidents)))

    print(node_yes_incidents)
    my_incidents=generate_incidents(node_yes_incidents,"MYSEVERITY","MYINCIDENTTYPE")

    print(my_incidents)
    
    print ("------------GENERATING INCIDENTS END---------------------")
    return (my_incidents)
    #return (node_yes_incidents)