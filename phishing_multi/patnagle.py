#!/usr/bin/python


import smtplib
import md5
import re
import hashlib
import time
from datetime import datetime
from time import sleep
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email import encoders
from string import digits

#initialize variables, since we use them later
#don't change the smtp server
subject = "NULL"
sender = "NULL"
baseURL = "NULL"
body = "NULL"
initialEmail = "True"
smtpServer = 'blah.com'

outputfilename = "Phishing_Results_" + datetime.now().strftime("%Y%m%d-%H%M") + ".csv"
def yes_no(question):
    yes = set(['yes', 'y', 'ye', ''])
    no = set(['no', 'n'])
    choice = raw_input(question).lower()
    if choice in yes:
        return True
    elif choice in no:
        return False
    else:
        print "not a valid answer"
        #sys.stdout.write("not a valid answer")

def send_email(recipient, emailbody, attachment, subject, sender):
    global initialEmail
    m = hashlib.md5()
    m.update(recipient)
    if 'URL_REPLACEME_URL_A' in emailbody:
        #This is used if two URLs are required.
        fullurla = baseURL + "1/?" + md5.new(recipient).hexdigest() #attach the md5 to the URL
        fullurlb = baseURL + "2/?" + md5.new(recipient).hexdigest() #attach the md5 to the URL
        emailbody = re.sub(r'URL_REPLACEME_URL_A', fullurla, emailbody) # put the link in the e-mail
        emailbody = re.sub(r'URL_REPLACEME_URL_B', fullurlb, emailbody) # put the link in the e-mail
    else:
        fullurl = baseURL  + "/?" + md5.new(recipient).hexdigest() #attach the md5 to the URL
        emailbody = re.sub("URL_REPLACEME_URL", fullurl, emailbody) # put the link in the e-mail
    temp = recipient.split(".") #create an array called temp, with each entry being part of the email, seperated by '.'
    firstname = temp[0] # take the dod email, and take everything before the first period, i.e. first name
    # take the dod email, and take everything after the second period, and remove any numbers
    lastname = temp[2].translate(None, digits)#john.k.doe.mail@mail.mil, so temp[2] should be 'doe'
    iaaccount = temp[0] + "." + temp[1] + "." + temp[2] + ".ia"
    #Looking for folks that have no middle initial, so it won't break.
    try:
        temp[4] #Checking if there is a middle initial by seeing if there is a fifth index, since we seperate by '.', it should contain 'mil', null if no middle
	
    except IndexError:
        lastname = temp[1].translate(None, digits) #If no middle initial, set the last name properly
    temp = recipient.split("@")
    #take the dod email, and save everything before the @ symbol for an account name
    account = temp[0]
    #whole bunch of checks, so it will dynamically replace any of these entries, instead of erroring out if it's not there
    if 'FIRSTNAME_REPLACEME_FIRSTNAME' in emailbody:
        emailbody = re.sub("FIRSTNAME_REPLACEME_FIRSTNAME", firstname.title(), emailbody)
    if 'LASTNAME_REPLACEME_LASTNAME' in emailbody:
        emailbody = re.sub("LASTNAME_REPLACEME_LASTNAME", lastname.title(), emailbody)
    if 'FIRSTCAPS_REPLACEME_FIRSTCAPS' in emailbody:
        emailbody = re.sub("FIRSTCAPS_REPLACEME_FIRSTCAPS", firstname.upper(), emailbody)
    if 'LASTCAPS_REPLACEME_LASTCAPS' in emailbody:
        emailbody = re.sub("LASTCAPS_REPLACEME_LASTCAPS", lastname.upper(), emailbody)
    if 'IAACCOUNT_REPLACEME_IAACCOUNT' in emailbody:
        emailbody = re.sub("IAACCOUNT_REPLACEME_IAACCOUNT", iaaccount, emailbody)
    if 'ACCOUNT_REPLACEME_ACCOUNT' in emailbody:
        emailbody = re.sub("ACCOUNT_REPLACEME_ACCOUNT", account, emailbody)
    if 'MD5HASH_REPLACEME_MD5HASH' in emailbody:
        emailbody = re.sub("MD5HASH_REPLACEME_MD5HASH", md5.new(recipient).hexdigest(), emailbody)
    if 'RECIPIENT_REPLACEME_RECIPIENT' in emailbody:
        emailbody = re.sub("RECIPIENT_REPLACEME_RECIPIENT", recipient, emailbody)
    if 'TIMEDATE_REPLACEME_TIMEDATE' in emailbody:
        emailbody = re.sub("TIMEDATE_REPLACEME_TIMEDATE", (time.strftime("%m/%d/%Y  %H:%M:%S")), emailbody)
    if 'DATE_REPLACEME_DATE' in emailbody:
        emailbody = re.sub("DATE_REPLACEME_DATE", (time.strftime("%m/%d/%Y")), emailbody)
    if 'MD5HASH_REPLACEME_MD5HASH' in subject:
        subject = re.sub("MD5HASH_REPLACEME_MD5HASH", md5.new(recipient).hexdigest(), subject)
    if 'MD5HASH_REPLACEME_MD5HASH' in sender:
        sender = re.sub("MD5HASH_REPLACEME_MD5HASH", md5.new(recipient).hexdigest(), sender)
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    msg.attach(MIMEText(emailbody))
    if attachment:
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(attachment, "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="' + attachment + '"')
        msg.attach(part)
    mailserver = smtplib.SMTP(smtpServer)
    mailserver.sendmail(sender, recipient, msg.as_string())
	#Trying to output to UTC
	#outputfilename = "Phishing_Results_" + datetime.utcnow().strftime("%Y%m%d-%H%M") + ".csv"
    if initialEmail:
        logging = "user" + "," + "md5" + "," +  "url" + "," +  "time" + "\n" + recipient + "," + md5.new(recipient).hexdigest() + "," + baseURL + "," +  datetime.utcnow().strftime("%m/%d/%Y  %H:%M:%S") + "\n" #write the email address and custom md5 to the logging file for Splunk
    else:
        logging = recipient + "," + md5.new(recipient).hexdigest() + "\n" #write the email address and custom md5 to the logging file for Splunk
    outputfile = open(outputfilename, "a")
    outputfile.writelines(logging)
    outputfile.close
    print logging
    mailserver.quit()
    initialEmail = False


# Get the file that contains the list of e-mail addresses.
# One e-mail address per line with nothing else in the file

victimfile = raw_input("[=] File with list of target e-mail addresses: ")
try:
    f = open(victimfile, "r")
    victims = f.readlines()
    f.close()
except IOError as (errno, strerror):
    print "I/O error({0}): {1}".format(errno, strerror)
except:
    print "[-] Unable to open the victim file"
    raise

# get the file that contains the body of the e-mail
bodyfile = raw_input("[=] File with the body of the e-mail: ")
try:
    f = open(bodyfile, "r")
    body = f.read()
    f.close()
except IOError as (errno, strerror):
    print "I/O error({0}): {1}".format(errno, strerror)
except:
    print "[-] Unable to open the e-mail body file"
    raise

# get the file that contains the header info of the e-mail
headerfile = raw_input("[=] File with the header of the e-mail: ")
try:
    lines = [line.rstrip('\n') for line in open(headerfile)]
    subject = lines[0]
    sender = lines[1]
    baseURL = lines[2]
    #Show the user what we imported, so they can abort if something is wrong
    print "[+] Using these settings from the headerfile."
    print "[+] Subject: " + subject
    print "[+] Sender: " + sender
    print "[+] Phishing URL: " + baseURL
    print "[+] Output file with logging: " + outputfilename
except IOError as (errno, strerror):
    print "I/O error({0}): {1}".format(errno, strerror)
except:
    print "[-] Unable to open the e-mail header file"
    raise

# see if we want to attach a file. Don't open it now but verify that we can open it.
if yes_no("[?] Do you want to attach a file? [Y/n]"):
    attachname = raw_input("[+] Path of file to attach: ")
    try:
        attachment = open(attachname, "r")
        attachment.close()
    except IOError as (errno, strerror):
        print "I/O error({0}): {1}".format(errno, strerror)
    except:
        print "[-] Unable to open the attachement file"
        raise
else:
    attachname = False
for i, person in enumerate(victims):
    if not i % 10:
        print "sleeping 3"
        sleep(3)
    send_email(person.strip(), body, attachname, subject, sender)
