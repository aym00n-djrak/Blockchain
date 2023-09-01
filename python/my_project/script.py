import sys

print("Hello world!")


print(sys.version)
print(sys.executable)
print(sys.path)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("Corey"))
