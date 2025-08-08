class QueryRouter:
    def __init__(self, plugin_manager):
        self.plugin_manager = plugin_manager

    def route(self, query: str) -> str:
        if self.plugin_manager.get_plugin(query):
            return "plugin"
        return "general"
