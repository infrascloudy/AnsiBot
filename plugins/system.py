from cloudbot import hook


@hook.command(autohelp=False)
def about():
    """Gives information about AnswerBot"""
    return "AnswerBot comments can be added to https://github.com/ansible/proposals/issues/48. These will be discussed in the Core meetings."
