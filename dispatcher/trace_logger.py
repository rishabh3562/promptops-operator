# promptops/dispatcher/trace_logger.py

import datetime
import json
import os

def log_event(event_type, details):
    log_dir = os.path.join(os.path.dirname(__file__), "..", "data", "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, f"trace_{datetime.date.today()}.log")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps({
            "event": event_type,
            "details": details,
            "ts": datetime.datetime.now().isoformat()
        }) + "\n")

class TraceLogger:
    def log_event(self, event_type, details):
        log_event(event_type, details)

    def __call__(self, event_type, details):
        log_event(event_type, details)

trace_logger = TraceLogger()
