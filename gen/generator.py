# this file regroup everything to generate the final code
import ast
from mappings import *
from lines import Lines
from extractor import extract_value
from event_class import Event
import store_global as store_global
import handler as handler

with open("code.py","r") as f:
    file=f.read()

Tree=ast.parse(file)

for node in Tree.body:
    node:ast.AST

    # EVENT and FUNCTIONS
    if isinstance(node,ast.FunctionDef):
        result=handler.handle_fun_def(node)
        if result=="continue":
            continue
    
    # VAR
    if isinstance(node,ast.AnnAssign):
        handler.handle_ann_assign(node)

with open("skript.sk","w") as f:
    final=""
    for line in Lines:
        final+=(line+"\n")
    f.write(final)