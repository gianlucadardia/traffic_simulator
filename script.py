import os
import random
import time

from helper import generate_nodeuuid_severity_events, load_ref_ids
from variables import FAULTYPE


f_connection_str = os.environ.get("FAULTSTREAM_CONNECTION_STRING")
f_eventhub_name = os.environ.get("FAULTSTREAM_EVENTHUB_NAME")


def rnd_fault_type():
    return random.choice(FAULTYPE)


def run_scripts():
    for i in range(1, 3):
        print(f"Step {i}: executing...")
        time.sleep(2)
    print("Script completed")
    print("Fault type: ", rnd_fault_type())

    fault_type = None
    myevents = generate_nodeuuid_severity_events(
        load_ref_ids("data/nodeuuid.txt"), "ok", fault_type
    )
    print(f"Generated {len(myevents)} events")
    if f_connection_str and f_eventhub_name:
        print("Fault stream configuration loaded")
    else:
        print("Fault stream configuration is not set")


run_scripts()
