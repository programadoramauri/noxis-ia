from transformers.pipelines import pipeline
from config import Config


class QueryRouter:
    def __init__(self):
        self.classifier = pipeline(
            "zero-shot-classification",
            model="MoritzLaurer/deberta-v3-base-zeroshot-v2.0",
            device_map="auto",
        )

    def route(self, query: str) -> str:
        candidate_labels = ["general knowledge", "calculation", "document retrieval"]
        result = self.classifier(query, candidate_labels)
        return result["labels"][0]
