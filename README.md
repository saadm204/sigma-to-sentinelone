# Sigma to SentinelOne PowerQuery Converter

This tool converts **Sigma rules** (YAML format) into **SentinelOne PowerQuery syntax**.

## 🚀 Features
- Convert Sigma rules via **Flask API**
- Convert YAML files via **command-line**
- Uses **pySigma-backend-sentinelone-pq** for accurate conversion

## 🛠 Installation
```bash
git clone https://github.com/YOUR_GITHUB/sigma-to-sentinelone.git
cd sigma-to-sentinelone
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 🔄 Convert Sigma Rule via API
Start the API:
```bash
python app.py
```
Convert a Sigma rule:
```bash
curl -X POST http://localhost:5001/convert -H "Content-Type: application/json" -d '{"sigma_yaml": "---\ntitle: Suspicious Query"}'
```

## 🔄 Convert Sigma Rule via Command-Line
```bash
python convert.py sigma_rules/example_rule.yaml
```
```
✅ Converted SentinelOne PowerQuery:
event.type="Process Creation" AND ...
```
