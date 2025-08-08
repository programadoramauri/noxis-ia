import re
from plugins.plugin_interface import ChatPlugin


class CalculatorPlugin(ChatPlugin):
    def should_handle(self, query: str) -> bool:
        return bool(re.search(r"\d+[\+\-\*/]\d+", query))

    def handle(self, query: str) -> str:
        return str(eval(re.search(r"\d+[\+\-\*/]\d+", query).group()))
