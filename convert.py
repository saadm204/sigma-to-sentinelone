import sys
import yaml
from sigma.collection import SigmaCollection
from sigma.backends.sentinelone_pq import SentinelOnePQBackend
from sigma.pipelines.pipeline import ProcessingPipeline

def convert_sigma_to_sentinelone(yaml_file):
    try:
        with open(yaml_file, "r") as file:
            sigma_yaml = yaml.safe_load(file)

        sigma_collection = SigmaCollection.from_yaml(sigma_yaml)
        backend = SentinelOnePQBackend(pipeline=ProcessingPipeline())
        converted_query = sigma_collection.convert(backend)

        print("✅ Converted SentinelOne PowerQuery:")
        print(converted_query)
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Usage: python convert.py <sigma_rule.yaml>")
        sys.exit(1)

    yaml_file = sys.argv[1]
    convert_sigma_to_sentinelone(yaml_file)