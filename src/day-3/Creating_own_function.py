def hello(to = "World"):
    print("Hello,", to)


hello()
name = input('What is your name? ').strip().title()
hello(name)

# this function greets the world by default first
# Then the function greets the person whose name is passed as an argument.