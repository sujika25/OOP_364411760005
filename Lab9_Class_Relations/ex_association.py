from ex_inderited import Teacher,Student

if __name__ == '__main__':
    # create
    s1 = Student("S001","Ton",23,"MIT",3.50)
    s2 = Student("S002","Nat",22,"AC",3.88)

    t1 = Teacher("T001","Fon",40,"MT")
    t2 = Teacher("T002","Pong",43,"MT")

    s1.add_advisor(t1)
    s1.add_advisor(t2)


    t1.add_advisee(s1)
    t1.add_advisee(s1)

    s1.display_advisor()
    t1.display_advisee()



