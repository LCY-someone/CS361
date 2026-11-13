def saveAssignmentList(AssignmentList)->None:
    with open("assignmentlist.txt","w") as filelist:
        for line in AssignmentList:
            filelist.write(",".join(line)+"\n")


def main()->None:
    loopInput="1"
    AssignmentList=[]
    with open("assignmentlist.txt","r") as filelist:
        for line in filelist:
            r=line.strip().split(",")
            AssignmentList.append(r)

    while loopInput!="3":
        print("\nAssignment List\n")
        print("No.      Name       Course    Due Date     Status")
        for line in AssignmentList:
            No=line[0]
            Name=line[1]
            course=line[2]
            due=line[3]
            status=line[4]
            print(f"{No}     {Name}     {course}    {due}    {status}")
        if len(AssignmentList)==0:
            print("No assignments saved.")
        print("1. Add Assignment   2.Mark Completed   3.Exit")
        loopInput=input("Enter Option:").strip()
        while loopInput not in ["1","2","3"]:
            loopInput=input("Enter 1, 2 or 3:").strip()

        if loopInput=="1":#Add Assignment part
            print("\n    Add Assignment\n")
            print("Add assignments to keep track of your coursework and due dates.\nAll three fields are required. Cancel discards the unsaved entry.")
            confirmchoose="2"
            while confirmchoose=="2":
                addname=input("Assignment name:").strip()
                while addname=="" or "," in addname:
                    addname=input("Enter a name without commas:").strip()
            
                addcourse=input("Course:").strip()
                while addcourse=="" or "," in addcourse:
                    addcourse=input("Enter a course without commas:").strip()
                
                adddue=input("Due date(Example: 10/11/2026 or 2026-10-11):").strip()
                while adddue=="" or "," in adddue:
                    adddue=input("Enter a due date without commas:").strip()

                addchoose="3"
                while addchoose=="3":
                    print("1.Save     2.Cancel     3.More Information")
                    addchoose=input("Enter option:").strip()
                    while addchoose not in ["1","2","3"]:
                        addchoose=input("Enter 1, 2 or 3:").strip()
                    if addchoose=="3":
                        print("Save opens a confirmation before adding the assignment.")
                        print("Cancel discards this entry. New assignments start as Incomplete.")

                if addchoose=="1":
                    No=1
                    for line in AssignmentList:
                        if int(line[0])>=No:
                            No=int(line[0])+1
                    No=str(No)
                    print("\n       Confirm Assignment")
                    print("Review the assignment details before saving.")
                    print("No.      Name       Course    Due Date     Status")
                    print(f"{No}     {addname}     {addcourse}    {adddue}    Incomplete")
                    print("1.Confirm     2.Cancel")
                    confirmchoose=input("Enter option:").strip()
                    while confirmchoose not in ["1","2"]:
                        confirmchoose=input("Enter 1 or 2:").strip()
                    if confirmchoose=="1":
                        AssignmentList.append([No,addname,addcourse,adddue,"Incomplete"])
                        print("Assignment added.")
                        print("1.Continue     U.Undo")
                        messagechoose=input("Enter option:").strip().lower()
                        while messagechoose not in ["1","u"]:
                            messagechoose=input("Enter 1 or U:").strip().lower()
                        if messagechoose=="u":
                            AssignmentList.pop()
                            print("Adding the assignment was undone.")
                        else:
                            saveAssignmentList(AssignmentList)
                    else:
                        print("Returning to Add Assignment.")
                else:
                    print("Entry cancelled.")
                    break

        elif loopInput=="2":#mark assignment as complete part
            if len(AssignmentList)==0:
                print("No assignments to mark as completed.")
            else:
                print("\n    Mark Completed")
                print("Enter an assignment number or C to cancel.")
                completeNo=input("Assignment No.:").strip()
                selected=None
                while selected is None and completeNo.lower()!="c":
                    for line in AssignmentList:
                        if line[0]==completeNo:
                            selected=line
                    if selected is None:
                        completeNo=input("Enter a listed assignment number or C:").strip()
                if selected is not None:
                    if selected[4]=="Completed":
                        print("This assignment is already completed.")
                    else:
                        print("\n       Confirm Complete")
                        print("Are you sure you want to mark this assignment as completed?")
                        print("No.      Name       Course    Due Date     Status")
                        No=selected[0]
                        Name=selected[1]
                        course=selected[2]
                        due=selected[3]
                        status=selected[4]
                        print(f"{No}     {Name}     {course}    {due}    {status}")
                        print("Confirm changes the status to Completed. The assignment will not be deleted.")
                        print("1.Confirm     2.Cancel")
                        completechoose="3"
                        
                        while completechoose not in ["1","2"]:
                            completechoose=input("Enter 1 or 2:").strip()
                        
                        if completechoose=="1":
                            selected[4]="Completed"
                            print(f"Assignment {No}: {Name} marked as completed.")
                            print("1.Continue     U.Undo")
                            messagechoose=input("Enter option:").strip().lower()
                            while messagechoose not in ["1","u"]:
                                messagechoose=input("Enter 1 or U:").strip().lower()
                            if messagechoose=="u":
                                selected[4]=status
                                print("Marking the assignment as completed was undone.")
                            else:
                                saveAssignmentList(AssignmentList)
                        else:
                            print("Completion cancelled.")
                else:
                    print("Completion cancelled.")
        else:
            print("Goodbye!")


if __name__=="__main__":
    main()
