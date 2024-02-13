import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class Email():
	def __init__(self, username, password, smtp_='Outlook'):
		self.username = username
		self.password = password
		self.smtp_ = smtp_

	def send(self, to, subject, content, message_id=None, attachment=None, html=None):
		
		try:
			# configuring mime for email
			self.msg = MIMEMultipart("alternative")
			self.msg['From'] = self.username
			self.msg['To'] = to
			self.msg['Subject'] = subject

			self.msg.attach(MIMEText(content))

			if html:
				self.msg.attach(MIMEText(html, "html"))

			if attachment:
				with open(attachment, 'rb') as f:
					self.part = MIMEApplication(f.read())

				self.part['Content-Disposition'] = 'attachment; filename="%s"' % attachment
				self.msg.attach(self.part)

			# configuring SMTP 
			if self.smtp_ == "Gmail":
				self.server = smtplib.SMTP('smtp.gmail.com', 587)
			elif self.smtp_ == "Outlook":
				self.server = smtplib.SMTP('smtp.office365.com', 587)
			self.server.ehlo()
			self.server.starttls()
			self.server.ehlo()
			self.server.login(self.username, self.password)

			self.server.send_message(self.msg)

			self.server.quit()

			return "email sent to %s" % to
			
		except:
			pass

