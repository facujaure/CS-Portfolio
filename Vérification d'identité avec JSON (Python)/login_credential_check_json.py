import json

bd = '''
{
    "usernames": ["mica@mail.co", "jerry@gma.com","alber@soup.co"],
    "pwd": ["abc123","caballitos","yoloswag"]
}
'''

users = json.loads(bd)


email = input("Enter your email:")
password = input("Enter your password:")

if email in users["usernames"]:
  index = users["usernames"].index(email)
  if password == users["pwd"][index]:
    print("OK")
  else:
    print("No match")

else:
     print("This username does not exist in our database")
