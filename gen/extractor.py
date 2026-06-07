import ast
from constant_mappings import TARGET_MAPPINGS

def extract_value(node):
    if isinstance(node, ast.Constant):
        return node.value

    if isinstance(node, ast.Attribute):
        full_path = build_attribute_path(node)

        if full_path.startswith("pyskript.target."):
            target_name = full_path.split(".")[-1]
            return TARGET_MAPPINGS.get(target_name, target_name)

        value_part = extract_value(node.value)
        return f"{value_part}-{node.attr}"

    if isinstance(node, ast.Name):
        return node.id

    if isinstance(node, ast.JoinedStr):
        result = ""

        for value in node.values:
            if isinstance(value, ast.Constant):
                result += str(value.value)

            elif isinstance(value, ast.FormattedValue):
                expr = value.value

                # player.name -> %player-name%
                if isinstance(expr, ast.Attribute):
                    result += "%" + extract_value(expr) + "%"

                # username -> %{username}%
                elif isinstance(expr, ast.Name):
                    result += "%{" + expr.id + "}%"

                else:
                    result += "%{" + extract_value(expr) + "}%"

        return result

    raise Exception(f"Unsupported node: {type(node)}")

def build_attribute_path(node):
    if isinstance(node, ast.Name):
        return node.id

    if isinstance(node, ast.Attribute):
        return f"{build_attribute_path(node.value)}.{node.attr}"

    return ""