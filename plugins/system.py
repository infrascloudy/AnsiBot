from cloudbot import hook


@hook.command(autohelp=False)
def about():
    """Gives information about AnsiBot"""
    return "AnsiBot comments can be added to https://github.com/ansible/community/issues/48. These will be discussed in the Core meetings."
