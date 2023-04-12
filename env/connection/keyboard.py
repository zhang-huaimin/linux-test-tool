"""
Keyboard Escape.

Always you want to simulated keyboard, Expecially ctrl + c.
"""


key_escape = {
    'ctrl_a': chr(1),
    'ctrl_c': chr(3),
    'ctrl_d': chr(4),
}

# reverse
rev_key_escape = dict(zip(
    key_escape.values(),
    key_escape.keys()
))