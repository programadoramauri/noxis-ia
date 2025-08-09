import re
import math
from plugins.plugin_interface import ChatPlugin


class CalculatorPlugin(ChatPlugin):
    def should_handle(self, query: str) -> bool:
        return bool(
            re.search(
                r"(\d+[\+\-\*\/\^]+\d+|calcular|quanto é|raiz|quadrado|cubo)",
                query.lower(),
            )
        )

    def handle(self, query: str) -> str:
        try:
            # Extrai expressões matemáticas
            expr = re.findall(
                r"(\d+\.?\d*[\+\-\*\/\^]\d+\.?\d*|\d+\.?\d*\s*[\+\-\*\/\^]\s*\d+\.?\d*)",
                query,
            )
            if expr:
                result = eval(expr[0].replace("^", "**"))
                return f"Resultado: {expr[0]} = {result}"

            # Operações especiais
            if "raiz" in query.lower():
                num = re.findall(r"\d+", query)
                if num:
                    root = math.sqrt(float(num[0]))
                    return f"Raiz quadrada de {num[0]} = {root:.2f}"

            if "quadrado" in query.lower():
                num = re.findall(r"\d+", query)
                if num:
                    square = float(num[0]) ** 2
                    return f"Quadrado de {num[0]} = {square}"

            if "cubo" in query.lower():
                num = re.findall(r"\d+", query)
                if num:
                    cube = float(num[0]) ** 3
                    return f"Cubo de {num[0]} = {cube}"

            return "Não consegui identificar uma expressão matemática válida."
        except Exception as e:
            return f"Erro no cálculo: {str(e)}"
