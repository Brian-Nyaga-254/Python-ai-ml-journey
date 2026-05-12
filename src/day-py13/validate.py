email = input("Whats your email? ").strip()
""" if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid") """
username, domain =email.split("@")


""" if (username) and ("." in domain): """
if username and domain.endswith(".com"):    
    print("valid")
else:
    print("Invalid")