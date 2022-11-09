import smtplib

username = 'pixelizedgaming1@outlook.com'
password = '*81P0K&9Jq'

def send(message, email):
	auth = (username, password)

	# Establish a secure session with gmail's outgoing SMTP server using your gmail account
	server = smtplib.SMTP( "smtp.office365.com", 587 )
	server.starttls()
	server.login(auth[0], auth[1])

	# Send text message through SMS gateway of destination number
	server.sendmail( auth[0], email, '\n' + message)

