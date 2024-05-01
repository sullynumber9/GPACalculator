import datetime
import platform
import subprocess

done = False

filereadname = "Grades.txt"
filewritename = "Response.txt"
counter = 0
courses = []
gpa = []
units = []
SEPARATOR = "=============================================================================="
unitsum = 0
sum = 0
four_pt_sum = 0
failed_counter = 0
failed_list = []
four_pt = []
percentage = ""
letter = ""

file = open(filereadname, "r")

for line in file.readlines():

    courses.append(line.split()[0])
    gpa.append(int(line.split()[1]))
    units.append(int(line.split()[2]))
    unitsum += int(line.split()[2])
    if (int(line.split()[1])) < 1:
        failed_counter += 1
        failed_list.append(line.split()[0])
        

    counter += 1

file.close()

for i in range(len(gpa)):
    sum += (gpa[i] * units[i])

    if gpa[i] == 12:
        four_pt.append(4.0)
    elif gpa[i] == 11:
        four_pt.append(3.9)
    elif gpa[i] == 10:
        four_pt.append(3.7)
    elif gpa[i] == 9:
        four_pt.append(3.3)
    elif gpa[i] == 8:
        four_pt.append(3.0)
    elif gpa[i] == 7:
        four_pt.append(2.7)
    elif gpa[i] == 6:
        four_pt.append(2.3)
    elif gpa[i] == 5:
        four_pt.append(2.0)
    elif gpa[i] == 4:
        four_pt.append(1.7)
    elif gpa[i] == 3:
        four_pt.append(1.3)
    elif gpa[i] == 2:
        four_pt.append(1.0)
    elif gpa[i] == 1:
        four_pt.append(0.7)
    elif gpa[i] == 0:
        four_pt.append(0)
    
    four_pt_sum += (four_pt[i] * units[i])

cGPA = (sum / (unitsum))
cGPA_four_pt = (four_pt_sum / unitsum)

if cGPA >= 12:
    letter = "A+"
    percentage = "90-100"
elif cGPA >= 11:
    letter = "A"
    percentage = "85-89"
elif cGPA >= 10:
    letter = "A-"
    percentage = "80-84"
elif cGPA >= 9:
    letter = "B+"
    percentage = "77-79"
elif cGPA >= 8:
    letter = "B"
    percentage = "73-76"
elif cGPA >= 7:
    letter = "B-"
    percentage = "70-72"
elif cGPA >= 6:
    letter = "C+"
    percentage = "67-69"
elif cGPA >= 5:
    letter = "C"
    percentage = "63-66"
elif cGPA >= 4:
    letter = "C-"
    percentage = "60-62"
elif cGPA >= 3:
    letter = "D+"
    percentage = "57-59"
elif cGPA >= 2:
    letter = "D"
    percentage = "53-56"
elif cGPA >= 1:
    letter = "D-"
    percentage = "50-52"
elif cGPA >= 0:
    letter = "F"
    percentage = "0-49"

# divide by number of terms * total units

# opening file

file = open(filewritename, "w")

file.write(SEPARATOR)
file.write("\n")
file.write("Mark generation completed on " + str(datetime.datetime.now()))
file.write("\n")
file.write(SEPARATOR)
file.write("\n")
file.write("\n")

file.write(SEPARATOR)
file.write("\nCourses:")
file.write("\nCourse:\tGPA-12pt:\tGPA-4pt\tUnits:")

for i in range(len(gpa)):
    file.write("\n")
    file.write(str(courses[i]) + "\t" + str(gpa[i]) + "\t" + str(four_pt[i]) + "\t" + str(units[i]))

file.write("\n")
file.write(SEPARATOR)
file.write("\n")

file.write("\n")
file.write(SEPARATOR)
file.write("\ncGPA - 12pt Scale: " + str(cGPA))
file.write("\ncGPA - 4pt Scale: " + str(cGPA_four_pt))
file.write("\nClosest Letter: " + letter)
file.write("\nClosest Percentage: " + percentage)
file.write("\n")
file.write(SEPARATOR)

file.write("\n")
file.write("\n")
file.write(SEPARATOR)
file.write("\n")

if failed_counter > 0:
    file.write("Failed course count: " + str(failed_counter))
    file.write("\nFailed course list: " + str(failed_list))
else:
    file.write("No failed courses")

if (cGPA < 1 or failed_counter >= 2):
    file.write("\nYear Failed")
elif (failed_counter == 1):
    file.write("\nYear Passed.  Must retake " + str(failed_list[0]))
else:
    file.write("\nYear Passed")

file.write("\n")
file.write(SEPARATOR)
file.close()

print("Data written to " + filewritename)

os = platform.system()

if os == "Windows":
    subprocess.Popen(["notepad.exe", filewritename])
elif os == "Darwin":
    subprocess.Popen(["open", "-a", "TextEdit", filewritename])
else:
    print("OS unrecognized by the program.  Please open " + filewritename + ", which is in the same directory as this program")







