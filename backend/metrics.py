from collections import defaultdict
from datetime import timedelta

def compute_worker_metrics(events):
    metrics = defaultdict(lambda: {
        "working_time": timedelta(0),
        "idle_time": timedelta(0),
        "units_produced": 0
    })

    # Sort events by time
    events = sorted(events, key=lambda e: e.timestamp)

    for i in range(len(events) - 1):
        current = events[i]
        next_event = events[i + 1]
        duration = next_event.timestamp - current.timestamp

        if current.event_type == "working":
            metrics[current.worker_id]["working_time"] += duration
        elif current.event_type == "idle":
            metrics[current.worker_id]["idle_time"] += duration

        if current.event_type == "product_count":
            metrics[current.worker_id]["units_produced"] += current.count

    return metrics
def compute_workstation_metrics(events):
    from collections import defaultdict
    from datetime import timedelta

    metrics = defaultdict(lambda: {
        "occupied_time": timedelta(0),
        "units_produced": 0
    })

    events = sorted(events, key=lambda e: e.timestamp)

    for i in range(len(events) - 1):
        current = events[i]
        next_event = events[i + 1]
        duration = next_event.timestamp - current.timestamp

        if current.event_type == "working":
            metrics[current.workstation_id]["occupied_time"] += duration

        if current.event_type == "product_count":
            metrics[current.workstation_id]["units_produced"] += current.count

    return metrics
