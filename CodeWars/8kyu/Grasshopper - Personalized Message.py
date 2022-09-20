def greet(name, owner):
    if name == owner:
        return "Hello {}".format("boss")
    else:
        return "Hello {}".format("guest")