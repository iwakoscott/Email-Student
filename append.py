import os, subprocess, sys

while True:
	#hw_num = int(raw_input("HW#: "))
	raw_input("Enter to continue...")
	try:
		subprocess.call("mkdir Programming-Project/GRADED_PROJECTS", shell=True)
		break
	except:
		print "GRADED_PROJECTS ALREADY EXISTS"
		exit(1)

student_homework = subprocess.check_output("ls Programming-Project/ORIGINAL/PDF/*.pdf", shell=True).strip('\n').split('\n')

for homework in student_homework:
	newFileName = os.path.splitext(homework)[0] + "_GRADED" + ".pdf"
	filenameNOPATH = newFileName[33:]
	try:
		subprocess.call("pdfunite " + "Programming-Project/rubric/rubric.pdf " + homework + " " + filenameNOPATH, shell=True)
		print "%s: Success." % (filenameNOPATH)
	except:
		print "pdfunite failed on %s" % (homework)

	try:
		print "moving %s..." % (filenameNOPATH)
		subprocess.call("mv " + filenameNOPATH + " Programming-Project/GRADED_PROJECTS", shell=True)
	except:
		print "unable to mv %s" % (filenameNOPATH)

print "DONE."