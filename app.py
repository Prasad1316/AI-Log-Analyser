from flask import Flask, render_template
import re
from collections import Counter, defaultdict
from datetime import datetime

app = Flask(__name__)

LOG_FILE = "sample_logs.log"

LOG_PATTERN = re.compile(
    r"\[(.*?)\]\s\[(.*?)\]\s\[(.*?)\]\s\[(.*?)\]\s(.*)"
)

def parse_logs():

    logs = []
    counts = Counter()

    counts["INFO"] = 0
    counts["WARNING"] = 0
    counts["ERROR"] = 0
    counts["CRITICAL"] = 0

    trace_map = defaultdict(list)

    with open(LOG_FILE, "r", encoding="utf-8") as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            match = LOG_PATTERN.match(line)

            if match:

                timestamp, level, module, trace_id, message = match.groups()

                log = {
                    "timestamp": timestamp,
                    "level": level,
                    "module": module,
                    "trace_id": trace_id,
                    "message": message
                }

                logs.append(log)

                counts[level] += 1

                trace_map[trace_id].append(log)

    # SORT ALL LOGS
    logs.sort(
        key=lambda x: datetime.strptime(
            x["timestamp"],
            "%Y-%m-%d %H:%M:%S"
        )
    )

    # SORT EACH TRACE
    for trace_id, trace_logs in trace_map.items():

        trace_logs.sort(
            key=lambda x: datetime.strptime(
                x["timestamp"],
                "%Y-%m-%d %H:%M:%S"
            )
        )

    return logs, counts, trace_map


@app.route("/")
def dashboard():

    logs, counts, trace_map = parse_logs()

    failed_traces = {}

    for trace_id, trace_logs in trace_map.items():

        has_failure = any(
            log["level"] in ["ERROR", "CRITICAL"]
            for log in trace_logs
        )

        if has_failure:

            probable_cause = "No warning detected before failure"

            for log in trace_logs:

                if log["level"] == "WARNING":
                    probable_cause = log["message"]
                    break

            failed_traces[trace_id] = {
                "logs": trace_logs,
                "root_cause": probable_cause
            }

    return render_template(
        "index.html",
        counts=counts,
        failed_traces=failed_traces,
        total_logs=len(logs)
    )


if __name__ == "__main__":
    app.run(debug=True)
