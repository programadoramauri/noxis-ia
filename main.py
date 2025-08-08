from llm.local_llm import load_llm
from core.query_router import QueryRouter
from plugins.plugin_manager import PluginManager

plugin_manager = PluginManager()
router = QueryRouter(plugin_manager)

query = "Quanto é 80*3?"
if router.route(query) == "plugin":
    plugin = plugin_manager.get_plugin(query)
    print(plugin.handle(query))

llm = load_llm()
response = llm.invoke("O que é inteligência artificial?")
print(response)
