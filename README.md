# webpageMonitor

How to use:
Prerequiste:
1. To enable the text messaging, you will need to set up a Twilio account at www.twilio.com

Usage example:
  python monitor.py [web url] [keyword] [message] [twilio account sid] [auth token] [phone number to] [phone number from] [file name] 
  python monitor.py ticketmaster.com "Taylor Swift" "Ticket is available" 123456 2w3fe 1619000000 1620000000 file

How this works:
It is a webpage monitor that monitor websites updates and send a text message to you upon such updates using Twilio. It searchs the number of occurences of the keyword in the page and stores that number in a file specified by user. It checks against the file whether the number of occurences of the keyboard has changed. If so, a text message will be sent. 

To constantly monitor webpages, you will need to have a machine that has internet access and run the program in the background. 

What is this good for:
  1. monitor availability of concert/events' ticket
  2. monitor your favorite celebrity's tweets

