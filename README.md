# bugslog
This is a home brewed multi-user issue tracking system based on django.

The interface is wholly based on django admin and is pretty straightforward. After runing the server and opening in browser just enter your Severities, States and Types then start posting issues.

An example config is as follows:

	Severity:
		Comment
		Trivial
		Normal
		Important
		Critical
		
	State:
		Opened
		Closed
		Under Review
		
	Type:
		Bug
		Feature
		
Whenever an issue is created or edited, a "Posted by" read-only field is filled by the currently logged in user. The issue can also be appointed to any user through the "Appointed to" field.

##Installation
Clone repository then issue a `python manage.py syncdb` command.

##Dependencies
None
