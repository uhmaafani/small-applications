def fees(age):
  if (age<=17):
    return 200
  elif (age>17 and age<40):
    return 400
  else: #age is >40
    return 300
