import json
import os

from azure.eventhub import EventData, EventHubProducerClient

from helper import (
    define_nodeuuids_to_work_with,
    generate_incidents_from_critical_nodes,
    generate_nodeuuid_rndcritical_events,
    generate_nodeuuid_severity_events,
    load_ref_ids,
    select_random_ref_ids,
    split_array,
    take_random_nodeuuid,
)
from variables import DEBUG, ROTTEN_UUID


incidentstream_connection_str = os.environ.get(
    "INCIDENTSTREAM_CONNECTION_STRING"
)
incidentstrem_name = os.environ.get("INCIDENTSTREAM_EVENTHUB_NAME")
f_connection_str = os.environ.get("FAULTSTREAM_CONNECTION_STRING")
f_eventhub_name = os.environ.get("FAULTSTREAM_EVENTHUB_NAME")


def _required_setting(name, value):
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def send_to_f_incidentstream(generated_incidents):
    producer = EventHubProducerClient.from_connection_string(
        conn_str=_required_setting(
            "INCIDENTSTREAM_CONNECTION_STRING", incidentstream_connection_str
        ),
        eventhub_name=_required_setting(
            "INCIDENTSTREAM_EVENTHUB_NAME", incidentstrem_name
        ),
    )
    event_data_batch = producer.create_batch()

    for incident in generated_incidents:
        message = json.dumps(incident)
        event_data_batch.add(EventData(message))

    producer.send_batch(event_data_batch)
    producer.close()

    if DEBUG:
        print(f"Number of sent rows to incident stream: {len(generated_incidents)}")


def send_to_f_eventstream(generated_rows):
    producer = EventHubProducerClient.from_connection_string(
        conn_str=_required_setting("FAULTSTREAM_CONNECTION_STRING", f_connection_str),
        eventhub_name=_required_setting("FAULTSTREAM_EVENTHUB_NAME", f_eventhub_name),
    )
    event_data_batch = producer.create_batch()

    for row in generated_rows:
        message = json.dumps(row)
        event_data_batch.add(EventData(message))

    producer.send_batch(event_data_batch)
    producer.close()

    if DEBUG:
        print(f"Number of sent rows to eventhub: {len(generated_rows)}")
