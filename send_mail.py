from aux_functions import send_regular_mail
from db_conns import *

try:
    subs = get_subs()
    for sub in subs:
        print(sub)
        send_regular_mail(sub[0], sub[1], sub[2])
except:
    pass