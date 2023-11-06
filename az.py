class important():
    def subfields():
        lists=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub fields in AI are")
        for subfields in lists:
            print(subfields)
            message="subfields"
        return message
    def oddeven():
        num=int(input("Enter a number:"))
        if((num%2)==0):
            print(num," is even  number")
            message="is even number"
        else:
            print(num,"is odd number")
            message="is odd number"
        return message
    def eligibilty():
        gender=input("Enter your gender:")
        age=int(input("Enter your age:"))
        if(age<=21):
            print("Not Eligible")
            message="Not Eligible"
        else:
            print("Eligible")
            message="Eligible"
        return message
    def percentage():
        sub1=int(input("subject1="))
        sub2=int(input("subject2="))
        sub3=int(input("subject3="))
        sub4=int(input("subject4="))
        sub5=int(input("subject5="))
        total=sub1+sub2+sub3+sub4+sub5
        print(("total :"),total)
        percentage=(total/5)
        print("percentage :",percentage)
        message="percentage:",percentage
        return message
    def triangle():
        H=int(input("Height :"))
        B=int(input("Breadth :"))
        print("Area formula :(Height*breadth/2)")
        AreaOfTriangle=H*B/2
        print("Area Of Triangle",AreaOfTriangle)
        message="Area Of Triangle",AreaOfTriangle
        H1=int(input("Height1 :"))
        H2=int(input("Height2 :"))
        B1=int(input("Breadth1 :"))
        print("Perimeter formula :(Height1+Height1+breadth)")
        PF=H1+H2+B1
        print("Perimeter of triangle :",PF)
        message="Perimeter of triangle:",PF
        return message