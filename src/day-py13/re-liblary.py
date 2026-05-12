import re
email = input("Whats your email? ").strip()


"""
r tells python to interpret the string in its raw version \is interpretted as a normal character and not as an escape sequence
A dot has a special meaning (any character). To match a real dot (period), you escape it with a backslash: \.. The raw string r"..." makes it easier to write \. without extra escaping.
\ is used in its raw format to avoid collison of the dots 
  it tells python not to treat the symbols specialy
"""




""" if re.search(r"^.+@.+\.edu$", email): """

"""
[words inside are accepted in the text]
 if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$", email):
     \w accepts any word character 
     re.IGNORECASE ignores input case,uppercase|lowercase
     
     """

"""
 (\w+\.)?  it specifies that a dot can either be there or not
 eg briannyaga@gmail.com,briannyaga@gmail.zetech.com
"""
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(com|gov)$", email, re.IGNORECASE):
    print("valid")
else:
    print("invalid")