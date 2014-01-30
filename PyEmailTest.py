#!/usr/bin/python
#	PyEmailTest.py
#	Version 1.0

#	Author: David Pany - DavidPany@gmail.com
#	Special thanks to Finn Ramsland from whom I borrowed several lines of code.

#	This tool can be used to send emails with custom Sender Address, Recipient Address, Subject,
#	Message Body, Server Address, and Port Number.
#
# 	The Server must not require authentication. This tool is meant for internal testing only.

# http://git-scm.com/book/en/Git-Basics-Getting-a-Git-Repository

import os
import smtplib 
from email import Encoders
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.Utils import formatdate
from Tkinter import Tk
from tkFileDialog import askopenfilename

def main():
	UseDefault = AskQuestion("\tUse Default message settings? ")
	
	print
	if UseDefault:
		Sender = "sender@PyEmailTest.test"
		Recipient = "recipient@PyEmailTest.test"
		Subject = "Test Subject From PyEmailTest.py"
		MessageBody = "This is a test email message body"
		ServerAddress = raw_input("\tServer Address: ").strip()
		PortNum = "25"
		
		print 
		print "\tYou have chosen to use the following default values:"
		print "\t\tSender:\t\t{}".format(Sender)
		print "\t\tRecipient:\t{}".format(Recipient)
		print "\t\tSubject:\t{}".format(Subject)
		print "\t\tMessage Body:\t{}".format(MessageBody)
		print "\t\tServer Address:\t{}".format(ServerAddress)
		print "\t\tPort:\t\t{}".format(PortNum)
	else:
		Sender = raw_input("\tSender Email Address:\t\t").strip()
		Recipient = raw_input("\tRecipient Email Address:\t").strip()
		Subject = raw_input("\tMessage Subject:\t\t").strip()
		MessageBody = raw_input("\tMessage Body:\t\t\t").strip()
		ServerAddress = raw_input("\tServer Address:\t\t\t").strip()
		PortNum = IsInt("\tPort #:\t\t\t\t")
	
	Message = MIMEMultipart()
	Message["From"] = Sender
	Message["Subject"] = Subject
	Message["Date"] = formatdate(localtime=True)
	Message.attach(MIMEText(MessageBody))
	
	print
	if(AskQuestion("\tDo you want to include an attachment? ")):
		Tk().withdraw()
		FilePath = askopenfilename()
		
		Attachment = open(FilePath, "rb")
		part = MIMEBase('application', "octet-stream")
		part.set_payload(Attachment.read())
		Encoders.encode_base64(part)
		part.add_header('Content-Disposition', 'attachment; filename ="{}"'.format(FilePath))
		Message.attach(part)
		Attachment.close()   
	
	print
	TimesToSend = IsInt("\tHow many times would you like to send this message? ")
	
	TimesSent = 0
	while TimesSent < TimesToSend:
		Transfer = smtplib.SMTP(ServerAddress, PortNum)
		Transfer.sendmail(Sender, Recipient, Message.as_string())
		Transfer.close()
		
		TimesSent += 1
	
def AskQuestion(QuestionText):
	AcceptableAnswer = False
	Answer = raw_input(QuestionText)
	
	if Answer[0].lower() == 'y':
		AcceptableAnswer = True
		ReturnValue = True
	elif Answer[0].lower() == 'n':
		AcceptableAnswer = True
		ReturnValue = False
	else:
		AcceptableAnswer = False
	
	while not AcceptableAnswer:
		Answer = raw_input("Unacceptable answer. {} (y/n): ".format(QuestionText))
		if Answer[0].lower() == 'y':
			AcceptableAnswer = True
			ReturnValue = True
		elif Answer[0].lower() == 'n':
			AcceptableAnswer = True
			ReturnValue = False
		else:
			AcceptableAnswer = False
	return ReturnValue
	
def IsInt(QuestionText):
	AcceptableInt = False
	Answer = raw_input(QuestionText).strip()
	while not AcceptableInt:
		try:
			ReturnValue = int(Answer)
			return ReturnValue
		except:
			Answer = raw_input(QuestionText + "Must be an integer")
	
	
main()