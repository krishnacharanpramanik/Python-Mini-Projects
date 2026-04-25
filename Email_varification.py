email_input=input("Enter your Emali ")
if '@' in email_input and (email_input.count('@')==1):
  if len(email_input)>16:
    if email_input[0].isalpha():
      if email_input[:].islower():
        if (email_input[-4]=='.') ^ (email_input[-3]=='.'):
          for i in email_input:
            if i.isspace():
              print('Email has space')
              if i=='_' or i=='.' or i=='@':
                pass
              else:
                print('Email has some spacial carecter')
        else:
          print('Email has .')
      else:
        print('somthis upper in email')
    else:
      print("Email satrt should be alphabet")
  else:
    print("Email lenth is short")
else:
  print("Email has no @")