import sys
import requests
from bs4 import BeautifulSoup
import re
from twilio.rest import TwilioRestClient
import os.path

# set up twilio API 
def alert(msg, account, token, toNumber, fromNumber):
    account_sid = account
    auth_token = token
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(body=msg,
    to = toNumber, # Replace with your phone number
    from_ = fromNumber) # Replace with your Twilio number


def monitor(url, keyword, msg, account, token, toNum, fromNum, fileName):
    while (True):
        try:
            request = requests.get(url)
        except:
            print "invalid url"
            sys.exit(0)
        requestSoup = BeautifulSoup(request.text)

        texts = requestSoup.findAll(text=True)

        texts = ''.join(texts).encode('utf-8')
        p = re.compile(keyword, re.IGNORECASE)
        number = len(p.findall(texts))
        
         # check if the number of occurences of keyword has changed
        with open(fileName, "r+") as f:
            data = f.readline()
            
            # put new number in the file
            f.seek(0)
            f.write(str(number))
            f.truncate()

            if data != '':
                try:
                    storedNumber = int(data)
                except ValueError:
                    print "invalid file content"
                    sys.exit(0)
                if storedNumber != number:
                    try:
                        alert(msg, account, token, toNum, fromNum)
                    except:
                        print "invalid Twilio Settings"
                        sys.exit(0)
            

if __name__ == "__main__":
  if len(sys.argv) == 1:
    print "usage: python monitor.py [web url] [keyword] [message] [twilio account sid] \
[auth token] [phone number to] [phone number from] [file name] "
  elif len(sys.argv) != 9:
    print "invalid arguments"
  else:
    args = sys.argv
    monitor(args[1], args[2], args[3], args[4], args[5], args[6], args[7], args[8])
