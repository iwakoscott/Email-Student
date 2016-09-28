import csv, re, subprocess, smtplib, mimetypes, email, email.mime.application

# The collection commented out below was used for testing purposes...
#collection = [["1", "MAT", "UG", "997488942", "Iwako, Satoshi", "ssiwako@ucdavis.edu"], ["2", "MAT", "UG", "99988833", "Chumakova, Darya", "dchumakova@ucdavis.edu"], ["3", "ECI", "UG", "99837437", "Iwako, Timothy", "jfdjskfd@ucdavis.edu"]]
collection = [["0", "0", "0", "SID", "Hernandez Ambriz, Rene", "rhernadez@ucdavis.edu"]]
#HW Number:
#HW_Number = int(raw_input("Homework #: "))
raw_input("Send ----> Programming Project")
raw_input("[ENTER TO CONTINUE...]")

#FOLDER NAME:
#FOLDER_NAME = "Homework-%d/GRADED_HOMEWORK_0%d" % (HW_Number, HW_Number)
FOLDER_NAME = "Programming-Project/GRADED_PROJECTS_OFFICIAL"

#with open('csv_Files/MAT167-emails.csv') as csvFile:
#	csvReader = csv.reader(csvFile)
#	collection = list(csvReader)
#	collection.remove(collection[0])

# Defined functions
def getUserName(student):
	return re.sub("@ucdavis.edu$", '', student[5])

def getNickName(student):
	return re.sub('[A-Za-z]*, ', '', student[4])

def makeMessage(student):
	message_header = "Dear " + getNickName(student) + ",\n\n"
	message_body = """As you may already know Smartsite is down and maybe down for the rest of the quarter, so, until Smartsite comes back I will be returning the graded homework and the programming project via email. Attached to this email is the graded programming assignment.""" + """\n\n\tThanks, \n\n\t\t The Reader\n[This is an automated message.]\n(P.S. IF YOU ARE VIEWING THE ATTACHMENT ON YOUR PHONE YOU MAY NOT BE ABLE TO SEE THE ANNOTATIONS THAT I MADE ON EACH HOMEWORK ASSIGNMENT. PLEASE VIEW THE ATTACHMENT ON YOUR COMPUTER TO SEE THE ANNOTATIONS. IF THERE ARE ANY ERRORS WITH YOUR GRADE, PLEASE SEE PROFESSOR PUCKETT.)"""
	message = message_header + message_body
	return message

# Code necessary to get into gmail
smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
smtpObj.ehlo()
smtpObj.starttls()


# Log in
myemail = raw_input("gmail: ")
while True:
	password = raw_input("Password: ")
	try:
		smtpObj.login(myemail, password)
		print "Logged in successfully."
		break
	except:
		print "Wrong password."

for student in collection:
	msg = email.mime.Multipart.MIMEMultipart()
	msg['Subject'] = "GRADED Programming Project"
	msg['From'] = myemail
	msg['To'] = student[5]
	body = email.mime.Text.MIMEText(makeMessage(student))
	msg.attach(body)

	try:
		filename = FOLDER_NAME + "/Programming_Project_" + getUserName(student) + "_GRADED.pdf"
		with open(filename, 'rb') as fp:
			att = email.mime.application.MIMEApplication(fp.read(),_subtype="pdf")
		att.add_header('Content-Disposition','attachment', filename=filename)
		msg.attach(att)
	except:
		print "%s's pdf was not found..." % (getUserName(student))
		continue


	print "emailing %s ... %s" % (getNickName(student), filename)

	smtpObj.sendmail(myemail, student[5], msg.as_string())