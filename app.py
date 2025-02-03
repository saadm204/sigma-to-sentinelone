from flask import Flask, request, jsonify
from flask_cors import CORS
from sigma.collection import SigmaCollection
from sigma.backends.sentinelone_pq import SentinelOnePQBackend
from sigma.pipelines.pipeline import ProcessingPipeline

app = Flask(__name__)
CORS(app)

@app.route("/convert", methods=["POST"])
def convert():
    data = request.json
    sigma_yaml = data.get("sigma_yaml", "")

    try:
        sigma_collection = SigmaCollection.from_yaml(sigma_yaml)
        backend = SentinelOnePQBackend(pipeline=ProcessingPipeline())
        converted_query = sigma_collection.convert(backend)
        return jsonify({"query": converted_query})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)