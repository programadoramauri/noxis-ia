from plugins.builtin_plugins.calculator import CalculatorPlugin


class PluginManager:
    def __init__(self):
        self.plugins = [CalculatorPlugin()]

    def get_plugin(self, query: str):
        for plugin in self.plugins:
            if plugin.should_handle(query):
                return plugin
        return None
