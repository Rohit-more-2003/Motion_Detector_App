import smtplib
import imghdr
from email.message import EmailMessage

from info import password, sender, receiver

def send_email(image_path):
	email_message = EmailMessage()
	email_message["Subject"] = "New person in sight!"
	email_message.set_content("Hey, just spotted a new person!")
	
	with open(image_path, "rb") as file: # reads the image as binary
		content = file.read() # content of file as binary is stored
	
	email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))
	
	gmail = smtplib.SMTP("smtp.gmail.com", 587)
	gmail.ehlo()
	gmail.starttls()
	gmail.login(sender, password)
	
	gmail.sendmail(sender, receiver,
	               email_message.as_string())
	
	gmail.quit()
	
if __name__ == "__main__":
	send_email(image_path="images/12.png")