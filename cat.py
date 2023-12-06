# print("meow")
# print("meow")
# print("meow")

# i = 0
# while i < 3:
#     i += 1
#     print("meow")

# for _ in range(999999):
#     print("meow")

# print("meow\n" * 3, end="")

# while True:
#     n = int(input("Whats n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")


def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("Whats n? "))
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("meow")


main()
