import logging
import smtplib
from PropertyUtil import PropertyUtil

class MailUtil:
	@staticmethod
	def composeMail(msg):
		try:
  			s = smtplib.SMTP(PropertyUtil.getAttribute('mail.smtp.host'))
			logging.debug('email result to ' + msg['To'])
			s.sendmail(msg['From'],msg['To'].split(),msg.as_string())
		except:
			logging.error('Unable to send mail to ' + msg['To'])
			logging.error(traceback.format_exc())

