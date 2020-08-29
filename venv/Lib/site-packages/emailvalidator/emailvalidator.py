#!/usr/bin/env python
import re

def endsWith(email,suffix):
    if email[-len(suffix):] == suffix:
        return True
    else:
        return False
    
def validateEmail(email):
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return True
        else:
            return False
    return False

def corporateEmail(email):
    if(validateEmail(email)):
        banned_domains = ["gmail.com","google.com","google.co.in","hotmail.com","yahoo.com","yahoo.in","yahoo.co.in","rediffmail.com","indiatimes.com","ymail.com","vsnl.com","in.com","vsnl.net","rediff.com","sify.com","aol.in","mtnl.net.in","live.com","facebook.com"];
        for domain in banned_domains:
            if(endsWith(email,domain)):
                return False
        return True
    return False


'''
    How to use :
    
    import emailValidator
    isval =  emailValidator.validateEmail("rohit.sonawane.genie@gmail.com")
    
    if isval == True:
        print "yes"
        
    isval =  emailValidator.corporateemail("rohit.sonawane.genie@rediff.com")
    print isval

'''
