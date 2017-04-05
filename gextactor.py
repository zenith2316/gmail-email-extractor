import imaplib, email
 
def split_addrs(s):
    #split an address list into list of tuples of (name,address)
    if not(s): return []
    outQ = True
    cut = -1
    res = []
    for i in range(len(s)):
        if s[i]=='"': outQ = not(outQ)
        if outQ and s[i]==',':
            res.append(email.utils.parseaddr(s[cut+1:i]))
            cut=i
    res.append(email.utils.parseaddr(s[cut+1:i+1]))
    return res
 
mail=imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(userid,password)
mail.select("INBOX")
result,data=mail.search(None,"ALL")
ids=data[0].split()
msgs = mail.fetch(','.join(ids),'(BODY.PEEK[HEADER])')[1][0::2]
addr=[]
for x,msg in msgs:
    msgobj = email.message_from_string(msg)
    addr.extend(split_addrs(msgobj['to']))
    addr.extend(split_addrs(msgobj['from']))
    addr.extend(split_addrs(msgobj['cc']))
