'''author:Savio Bijo Thomas
 date:08-10-2024
purpose:String concatination&slicing'''

first_name=input("enter first name:")
last_name=input("enter last name:")
full_name=first_name+" "+last_name
print(full_name)
length=len(last_name)
extract_last_name=full_name[length +1:]
print(extract_last_name)

