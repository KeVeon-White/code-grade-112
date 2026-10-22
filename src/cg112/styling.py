err_style = "red bold"
warn_style = "yellow italic"

def print_err(msg: str):
    from cg112.cli import console
    console.print(msg, style=err_style)

def print_warning(msg: str):
    from cg112.cli import console
    console.print(msg, style=warn_style)
