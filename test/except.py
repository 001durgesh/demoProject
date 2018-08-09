try:
    a = 10
    print a
    raise NameError("customException")

except NameError as e:
    print("This statement is raising an exception")
    print(e)
finally:
    print("It's finally..")

print "Outside of Try block"
