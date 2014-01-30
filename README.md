PyEmailTest
===========

This tool is intended to test internal email MTAs whether they be an 
smtp-sink, a true email server, or an email security product.

This tool does not include any authentication features for MTAs that
do require authentication.

Usage:

	PyEmailTest.py
    
The terminal will ask you for answers but you can choose to use the default values of:

	Sender Address:      sender@PyEmailTest.test
	Recipient Address:   recipient@PyEmailTest.test
	Subject:             Test Subject From PyEmailTest.py
	Message Body:        This is a test email message body
	Port Number:         25
  
You can also choose to customize the above values.

You must always enter a value for the Server Address.

You may choose to add one attachment to the message.

You may choose how many times to continuously send the message.


For bugs, questions, comments, and recommendations, please contact Dave Pany at DFIRDave@gmail.com

Special thanks to Finn Ramsland since I borrowed several lines of code from one of his scripts.
