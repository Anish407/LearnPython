age=10
tax=0.05
name="John's name"
is_student=True
tax_int= int(tax*100)
char='a'
float_num= (int)(10.5)
concat_data= str(age) + " " + name
print("age:",age)   
print("tax_int:",tax_int)
concat_demo2= f"here is the tax {tax_int} and age {age}"
print (concat_demo2)

name2 =input("Press please enter a name")
age2= input("Press please enter a age")
age_int= int(age2)
print(f"Hello {name2}, you are {age_int} years old")
