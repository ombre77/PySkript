# this file registrate actions for the generator like send_message who would add code to the final file

import ast
from lines import Lines,write
from extractor import extract_value

def generate_send(node:ast.AST):
    player_node = None
    message_node = None

    if getattr(node, 'keywords', None):
        for kw in node.keywords:
            if kw.arg == 'receiver':
                player_node = kw.value
            elif kw.arg == 'message':
                message_node = kw.value

        if player_node is None and len(node.keywords) >= 1:
            player_node = node.keywords[0].value
        if message_node is None and len(node.keywords) >= 2:
            message_node = node.keywords[1].value

    if (player_node is None or message_node is None) and getattr(node, 'args', None):
        if len(node.args) >= 2:
            if player_node is None:
                player_node = node.args[0]
            if message_node is None:
                message_node = node.args[1]
        elif len(node.args) == 1:
            if message_node is None:
                message_node = node.args[0]

    if player_node is None or message_node is None:
        return

    player = extract_value(player_node)
    message = extract_value(message_node)
    write(f'send "{message}" to {player}')
