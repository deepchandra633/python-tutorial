# Program to check whether a student passed in all subjects

math = int(input("Enter marks in Math: "))
science = int(input("Enter marks in Science: "))
english = int(input("Enter marks in English: "))

if math >= 33:

    if science >= 33:

        if english >= 33:
            print("Student Passed in all subjects")

        else:
            print("Failed in English")

    else:
        print("Failed in Science")

else:
    print("Failed in Math")

    if science >= 33:

        if english >= 33:
            print("But Student Passed in Science and English subjects")

        else:
            print("But Student Passed only in Science subject")

    else:

        if english >= 33:
            print("But Student Passed only in English subject")

        else:
            print("Student Failed in all subjects")