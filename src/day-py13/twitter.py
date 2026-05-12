import re


url = input("URL: ").strip()

""" username = url.replace("https://twitter.com/", "")
print(f"Username: {username}") 
url.removeprefix
"""
""" username = re.sub(r"^(https?://)?(www\.)twitter\.com/", "", url)
print(f"Username: {username}") """


"""?: means that we are grouping www. but not capturing it """
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(\w+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))
