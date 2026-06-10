# 🚀 AI Log Analyzer & Root Cause Detection

An AI-inspired observability platform that transforms chaotic, mixed system logs into meaningful insights. The system automatically sorts logs, correlates related events using Trace IDs, reconstructs complete request lifecycles, and identifies probable root causes through an interactive dashboard.

## 📌 What is it?

Modern applications generate thousands of logs from different services such as authentication, databases, payment gateways, and AI systems. These logs are often unordered, making debugging difficult and time-consuming.

This project helps developers understand **what happened, where it happened, and why it happened** by reconstructing the entire sequence of events leading to a failure.

## ⚙️ How It Works

Mixed Logs → Regex Parsing → Timestamp Sorting → Trace ID Correlation → Root Cause Detection → Dashboard Visualization

* **Regex Parsing:** Extracts timestamps, severity levels, modules, Trace IDs, and messages from raw logs.
* **Automatic Sorting:** Reorders mixed logs chronologically, even if they arrive out of sequence.
* **Trace Correlation:** Groups events belonging to the same request using Trace IDs.
* **Root Cause Analysis:** Identifies warnings and events that likely contributed to errors and critical failures.
* **Dashboard Visualization:** Displays log statistics, event timelines, and probable causes in an easy-to-understand interface.

## ✨ What Makes It Different?

Unlike traditional log viewers that simply display logs line by line, this system:

* Reconstructs complete request lifecycles.
* Handles unsorted and mixed logs automatically.
* Connects events across multiple services using Trace IDs.
* Provides context behind failures instead of isolated error messages.
* Presents insights through an interactive dashboard.

## 💡 Why Is It Useful?

* Reduces debugging time.
* Helps identify the origin of failures quickly.
* Improves visibility into distributed systems.
* Makes incident investigation easier.
* Demonstrates core observability concepts used in modern production environments.

## 🛠️ Tech Stack

Python • Flask • HTML/CSS • JavaScript • Chart.js • Regex

## ▶️ Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Open: `http://127.0.0.1:5000`

## 🚀 Future Improvements

* Search and filtering by Trace ID
* Real-time log streaming
* AI-based anomaly detection
* Failure prediction using machine learning
* Docker deployment
