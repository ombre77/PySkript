import ast
from mappings import *
from constant_mappings import *
import store_global as store_global
from event_class import Event
from lines import write

def handle_fun_def(node:ast.FunctionDef):
    decos=node.decorator_list

    # find the first decorator that maps to a skript event
    sk_event = None
    for deco in decos:
        event_name=getattr(deco, "attr", None)
        sk_event=EVENT_MAPPINGS.get(event_name)
        if sk_event:
            break

    if not sk_event:
        return "continue"

    event_class = Event(node)

    # collect actions from the function body
    for part in node.body:
        if isinstance(part,ast.Expr) and isinstance(part.value,ast.Call):
            handle_action_call(part,event_class)
        elif isinstance(part,(ast.Assign,ast.AugAssign)):
            code=handle_assign(part)
            event_class.add(write,code)

    # generate the event block once
    event_class.generate(sk_event + ":")

def handle_ann_assign(node:ast.AnnAssign):
    if node.annotation.attr in store_global.globals_type:
        if node.target.id not in store_global.GLOBAL_VAR:
            store_global.GLOBAL_VAR.append(node.target.id)

def handle_action_call(expr:ast.Expr,event_class:Event):
    value:ast.Call=expr.value
    # support both attribute calls (module.func) and direct names
    name=None
    if isinstance(value.func,ast.Attribute):
        name=value.func.attr
    elif isinstance(value.func,ast.Name):
        name=value.func.id

    func = ACTION_MAPPINGS.get(name)
    if func:
        event_class.add(func,value)

def handle_assign(node):
    if isinstance(node, ast.Assign):
        name = node.targets[0].id
        value = extract_value(node.value)

        if name in store_global.GLOBAL_VAR:
            return f"set {{{name}}} to {value}"
        else:
            return f"set {{_{name}}} to {value}"
    
    elif isinstance(node, ast.AugAssign):
        name = node.target.id
        value = extract_value(node.value)

        if name in store_global.GLOBAL_VAR:
            var = f"{{{name}}}"
        else:
            var = f"{{_{name}}}"

        if isinstance(node.op, ast.Add):
            return f"add {value} to {var}"

        elif isinstance(node.op, ast.Sub):
            return f"remove {value} from {var}"

        elif isinstance(node.op, ast.Mult):
            return f"multiply {var} by {value}"

        elif isinstance(node.op, ast.Div):
            return f"divide {var} by {value}"