class Teacher:

    def addMark(self, studentName, mark):
        try:
            file = open("students_mark.txt", "a")
            file.write(studentName + ":" + mark + "\n")
            print(studentName + "'s mark " + str(mark) + " is added")
        except Exception :
            print("ERROR!!!\n")
        finally:
            file.close()

    def removeMark(self, studentName):
        try:
            file = open("students_mark.txt")
            lines = file.readlines()
            file.close()

            found = False
            for line in lines:
                if studentName in line:
                    found = True
                    lines.remove(line)
                    break

            if found:
                file = open("students_mark.txt", "w")
                for line in lines:
                    file.write(line)
                file.close()
                print(studentName + "'s marks removed")
            else:
                print(studentName + " doesn't exist")

        except Exception :
            print("ERROR!!!\n")

    def searchMark(self, studentName):
        try:
            file = open("students_mark.txt")
            lines = file.readlines()
            found = False
            for line in lines:
                if studentName in line:
                    found = True
                    (name, mark) = line.split(":")
                    print(name + "'s mark : " + mark)
                    break
            if not found:
                print(studentName + " cannot be found")
        except Exception as e:
            print("ERROR!!!\n", e)
        finally:
            file.close()

class Student:

    def searchMark(self, studentName):
        try:
            file = open("students_mark.txt")
            lines = file.readlines()
            found = False
            for line in lines:
                if studentName in line:
                    found = True
                    (name, mark) = line.split(":")
                    print(name + "'s mark : " + mark)
                    break
            if not found:
                print(studentName + " cannot be found")
        except Exception as e:
            print("ERROR!!!\n", e)
        finally:
            file.close()


class Parent:

    def searchMark(self, studentName):
        try:
            file = open("students_mark.txt")
            lines = file.readlines()
            found = False
            for line in lines:
                if studentName in line:
                    found = True
                    (name, mark) = line.split(":")
                    print(name + "'s mark : " + mark)
                    break
            if not found:
                print(studentName + " cannot be found")
        except Exception as e:
            print("ERROR!!!\n", e)
        finally:
            file.close()


class UserTypeInputError(Exception):
    def __str__(self):
        return "\nPlease enter valid input"


class UserActionInputError(Exception):
    def __str__(self):
        return "\nPlease enter valid input"


if __name__ == "__main__":

    # ask user type
    userIn = input(
        "If you are a teacher, type 'T'\nIf you are a student, type 'S'"
        "\nIf you are a parent, type 'P'\nTo exit type 'E'\n")
    while userIn.upper() != "E":
        try:
            if userIn.lower() not in ["t", "s", "p", "e"]:
                raise UserTypeInputError
            else:
                if userIn.upper() == "T":
                    # Teacher
                    teacher = Teacher()

                    # ask user
                    userIn = input(
                        "\nTo add marks type 'add'\nTo remove marks type 'remove'"
                        "\nTo search marks type 'search'\nTo exit type 'exit'\n")
                    while userIn != "exit":
                        try:
                            if userIn not in ["add", "remove", "search", "exit"]:
                                raise UserActionInputError
                            else:
                                if userIn == "add":
                                    name = input("\nEnter student's name to add : ")
                                    mark = input("Enter " + name + "'s marks (1~10) : ")
                                    teacher.addMark(name, mark)
                                elif userIn == "remove":
                                    name = input("\nEnter student's name to remove : ")
                                    teacher.removeMark(name)
                                elif userIn == "search":
                                    name = input("\nEnter student's name to search : ")
                                    teacher.searchMark(name)
                        except UserActionInputError as e:
                            print(e)
                        finally:
                            userIn = input(
                                "\nTo add marks type 'add'\nTo remove marks type 'remove'"
                                "\nTo search marks type 'search'\nTo exit type 'exit'\n")

                elif userIn.lower() == "s" :
                    # Student
                    # ask user
                    student = Student()
                    userIn = input("\nTo search marks type 'search'\nTo exit type 'exit'\n")
                    while userIn != "exit":
                        try:
                            if userIn not in ["search", "exit"]:
                                raise UserActionInputError
                            else:
                                if userIn == "search":
                                    name = input("\nEnter student's name to search : ")
                                    student.searchMark(name)
                        except UserActionInputError as e:
                            print(e)
                        finally:
                            userIn = input("\nTo search marks type 'search'\nTo exit type 'exit'\n")

                elif userIn.lower() == "p":
                    # Parent
                    # ask user
                    parent = Parent()
                    userIn = input("\nTo search marks type 'search'\nTo exit type 'exit'\n")
                    while userIn != "exit":
                        try:
                            if userIn not in ["search", "exit"]:
                                raise UserActionInputError
                            else:
                                if userIn == "search":
                                    name = input("\nEnter student's name to search : ")
                                    parent.searchMark(name)
                        except UserActionInputError as e:
                            print(e)
                        finally:
                            userIn = input("\nTo search marks type 'search'\nTo exit type 'exit'\n")
        except UserTypeInputError as e:
            print(e)
        finally:
            # ask user type
            userIn = input(
                "\nIf you are a teacher, type 'T'\nIf you are a student, type 'S'"
                "\nIf you are a parent, type 'P'\nTo exit type 'E'\n")

    print("Good bye, Dear User!")