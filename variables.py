#adding vriable 
DEBUG = True

FAULTYPE = [
            "NodeUnmanagable",
            "CustomPollWarning",
            "InterfaceInputQueueDropsRateHigh",
            "RrgNoPrimary",
            "InterfaceDown",
            "RrgNoSecondary",
            "NodeUnreachable",
            "NodeUnmanagable",
            "IslandGroupDown",
            "NodeDown",
            "RrgMultiplePrimary",
            "NodeOrConnectionDown",
            "NodeDown"
            ]

# Define a base row template  

base_row = {  
    "MESS_SOURCE": "WIFINNM8",  
    "MESS_ID": "8768e015-e158-4e54-8b71-fe936d2c7d02",  
    "NODE_UUID": "451f3ac7-18fb-4140-a42a-fe311287bd6a",  
    "STATO_AGENZIA": "APERTA",  
    "CLASSIFICATION": "UP3",  
    "GRUPPO": "UFF_POST",  
    "MIGRATO": 1,  
    "FRAZ": 65099,  
    "REG_MODIFIED": "",  # Placeholder  
    "DENOMINAZIONE": "OLMI",  
    "COMUNE": "SAN BIAGIO DI CALLALTA",  
    "POLO": "VENEZIA",  
    "ATM_FLAG": 1,  
    "HOTSPOT": 2,  
    "SIGLA_PROVINCIA": "TV",  
    "REGIONE": "VENETO",  
    "CC": "FIELD",  
    "TIME_FIRST": "",  # Placeholder  
    "DURATA": "+000000000 00:24:17.288",  
    "NODE_NAME": "pta-65099-tv-olmi",  
    "MGMT_ADDR": "10.249.198.81",  
    "DEVICE_TYPE": "ROUTER (C.E.) T.I.R.",  
    "SOURCE_NAME": "Atm2/0/0.1",  
    "DEVICE_TYPE_1": "ROUTER (C.E.) T.I.R.",  
    "FORMATTED_MESSAGE": "Interface Down Atm2/0/0.1 - BACKUP - WAN ( Mpls; #; 42213017398; R-VE107; ge-3/0/0.1341; )",  
    "SEVERITY": "critical",  
    "OWNED_BY": "",  
    "FORCED_BY": "",  
    "NAME": "InterfaceDown",  
    "FAMILY": 92,  
    "DEVICE_ID": 2900476,  
    "MEDIA_ACCESS_TECH": 0,  
    "UMTS_FLAG": 0,  
    "TYPE": "Router",  
}  

ROTTEN_UUID = ["ad4a3e64-2b6f-4da4-bbbb-5a67afc65909", 
               "25f0dc10-5146-47ac-ac02-ccf342e8a8eb"]
