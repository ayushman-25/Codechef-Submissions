from collections import defaultdict

check_login = defaultdict(str)
time_table = defaultdict(list)
time_table["Ayushman Chahar"] = ["DBMS", "Operating System"]


def login():
    while (True):
        print("Please enter your username: ")
        username = input()
        print("Please enter your password: ")
        password = input()
        if (check_login[username] == password):
            print("Logged in Successfully")
            return [username, password]
        else:
            print("Credentials don't match")
            print("Please type 'Back' to go back to the login menu or type 'Exit'")
            option = input()
            if (option == "Back"):
                continue
            else:
                return 0


def main():
    print("Welcome To Course Slot Booking System:-")
    print("Please Choose any one of the following options to proceed: ")
    print("1. Login")
    print("2. Signup")
    print("3. Exit")
    option_for_login = int(input())
    logged_in_status = False
    if (option_for_login == 3):
        return
    elif (option_for_login == 1):
        verify = login()
        if (not verify):
            return
        else:
            logged_in_status = True
            username = verify[0]
    else:
        print("Please enter the username you want: ")
        username = input()
        print("Please enter the password you want: ")
        password = input()
        check_login[username] = password
        print("Sign up Successful")
        print("Please login with your credentials created")
        verify = login()
        if (not verify):
            return
        else:
            logged_in_status = True
            username = verify[0]

    assert (logged_in_status is True)

    subjects = ["DBMS", "DSA", "Operating System", "Networks"]
    subjects_id = defaultdict(int)
    for i in range(4):
        subjects_id[subjects[i]] = i + 1

    capacities = [50, 50, 50, 50]
    availability = [48, 30, 35, 0]
    time_slot = [["Monday", [4, 5, "PM"]], ["Wednesday", [8, 9, "AM"]], ["Monday", [5, 6, "PM"]],
                 ["Monday", [6, 7, "PM"]]]
    waiting_list = [[], [], [], ["Arun Kumar", "Vimal Chaurasia", "Sai Krishna"]]

    curr_user_subjects = time_table[username]

    while (True):

        print("Choose from the following options available")
        print("1. Show Registered Courses and its Details")
        print("2. Register for the Courses")
        print("3. Delete any of the Registered Course")

        option = input()

        if (option == '1'):
            print("Your Registered Courses are as follows: ")
            if (len(curr_user_subjects) == 0):
                print("None")
            else:
                for i in range(len(curr_user_subjects)):
                    subject_id = subjects_id[curr_user_subjects[i]]
                    print((str(i + 1) + '.'), curr_user_subjects[i] + ':', "Every", time_slot[subject_id][0],
                          str(time_slot[subject_id - 1][1][0]) + time_slot[subject_id - 1][1][2] + ' - ' + str(
                              time_slot[subject_id - 1][1][1]) + time_slot[subject_id - 1][1][2])
            print("Type 'Back' to go back to menu else type 'Exit'")
            option = input()
            if (option == 'Back'):
                continue
            else:
                return

        elif (option == '2'):
            print("Courses which can be registered are as follows:")
            for i in subjects:
                if i not in curr_user_subjects:
                    idx = subjects_id[i] - 1
                    print("Name -", i)
                    print("Time Slot -", time_slot[idx][0], *time_slot[idx][1])
                    print("Availability - ", availability[idx])

            print("Enter the subject name you want to choose:")
            subject_wanted = input()
            if (subject_wanted not in subjects):
                print("Wrong subject")
                continue
            time_slot_req = time_slot[subjects_id[subject_wanted] - 1]
            poss_clash_courses = [subjects[i] for i in range(4) if
                                  time_slot[i] == time_slot_req and subjects[i] != subject_wanted]
            if (poss_clash_courses):
                print("Sorry, Current Subject Can't be taken, clashing with your other subjects")
            elif (availability[subjects_id[subject_wanted] - 1] > 0):
                print("Courses successfully registered!")
                time_table[username].append(subject_wanted)
                availability[subjects_id[subject_wanted] - 1] -= 1
            else:
                print("As of now there are no seats left for this subject")
                print("Would you like to put your name in the waiting list")
                print("1. Yes")
                print("2. No")
                print("Choose 1 or 2")
                choice = int(input())
                if (choice == 1):
                    waiting_list[subjects_id[subject_wanted] - 1].append(username)
                    print("Name in the waiting list successfully added")
            print("Type 'Back' to go back to menu else type 'Exit'")
            option = input()
            if (option == 'Back'):
                continue
            else:
                return

        elif (option == '3'):
            print("Your Registered Courses are as follows: ")
            for i in range(len(curr_user_subjects)):
                subject_id = subjects_id[curr_user_subjects[i]]
                print((str(i + 1) + '.'), curr_user_subjects[i] + ':', "Every", time_slot[subject_id][0],
                      str(time_slot[subject_id - 1][1][0]) + time_slot[subject_id - 1][1][2] + ' - ' + str(
                          time_slot[subject_id - 1][1][1]) + time_slot[subject_id - 1][1][2])
            print("Type the ID of the Subject which you want to delete")
            option = int(input())
            if (1 <= option <= len(curr_user_subjects)):
                subj = curr_user_subjects[option - 1]
                availability[subjects_id[curr_user_subjects[option - 1]] - 1] += 1
                del curr_user_subjects[option - 1]
                print("Course Successfully Deleted")
                # handle the waiting list for this particular subject
                if (waiting_list[subjects.index(subj)]):
                    first_priority = waiting_list[subjects.index(subj)].pop(0)
                    time_table[first_priority].append(subj)
                    availability[subjects_id[curr_user_subjects[option - 1]] - 1] -= 1
                print("Type 'Back' to go back to menu else type 'Exit'")
                option = input()
                if (option == 'Back'):
                    continue
                else:
                    return
            else:
                print("Wrong Choice entered")
                continue

        else:
            print("Wrong Choice entered")
            continue


if __name__ == "__main__":
    main()
