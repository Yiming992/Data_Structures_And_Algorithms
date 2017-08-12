from Deques import deques

def check_palindrome(String):
    store=deques()
    chars=list(String)
    for cha in chars:
        store.addRear(cha)

    while store.size()>1 and store.isEmpty==False:
        if store.removeFront()!=store.removeRear():
            return False
    return True

print(check_palindrome('toot'))
