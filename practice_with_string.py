# using \n for next line and \t for tabs. I hope this will work. 
print ('hello! I hope you are doing well.\n\t I wanted to tell you that this line goes down with one tab.\n\n I putting this two line below. \n\t\t I hope it worked one enter or two tabs.')
print ('I hope it must had worked.') 

# I am trying to print message in lower, tittle and upper case. Also trying to put align to the center, right and left.
print ('i love you honey'.upper ())
print ('I am good.'.title().center(20))
print ('IT WAS A WONDERFUL DAY.'.lower().rjust(100))
print (f"{'I am able to print text at least in python.':>100}".upper()) # also to print in right.

#   assigning variable, changing cases, adjusting the lines, finding, replace and length of the variable. 
message = 'hello I Will come home late. I hAVe a meeting.'
print (message.upper().rjust(100))
print (f"\t{message}\n".lower().center(80))
print (f"\n\t\t\t {message:>50}\n".title())
print (len(message))
print(message[0])
print (message.lower().find ('i'))
print (message.replace('hello I Will come home late. I hAVe a meeting.', 'I am comming home late due to the meeting.'.upper()))
message = message.replace(message, message.title())
print (message)
print (message [0:5])
print (message.center (50))
print (message.lower().find('home'))

# Task:
customer = "   ashok thapa   "
email = "ASHOK@GMAIL.COM"
message = "hello ashok, welcome to python programming"

#stripping spaces from sustomer name. 
customer = customer.strip().title()
print (customer)
email = email.lower()
print (email)
print (message.capitalize())
print (len(message))
print (message.find('python'))
message = message.replace('python', 'data analytics')
print (customer.center(40))
print (f"{customer:>40}")
print (customer.split(", "))
print (email.removesuffix('.com'))
print (email.replace('@gmail',''))
