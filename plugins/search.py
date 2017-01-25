from cloudbot import hook

@hook.command("search", "doc")
def search(text, chan, conn, bot, notice, message):
    """ search <text> returns ansible docs url.
    working to include top results"""
    res_string = ''
    for word in text.split():
        print(word)
        res_string += word+'%20'
    
    message('http://docs.ansible.com/ansible/#stq='+res_string[:-3])
