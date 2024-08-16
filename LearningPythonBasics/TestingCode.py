
friends = ["Annabelle", "Greg", "Katya", "Sol"]
mylist = [ "a", "b", "c", "d", "e", "f"]

print(friends)


print(list(range(2, 14, 4)))

# tuple
ab = ("a", "b", "c", 4)

print(ab[0])

names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]

names_and_heights = zip(names, heights)
print(list(names_and_heights))


numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers]
print(doubled)





no_if   = [num * 2 for num in numbers]
if_only = [num * 2 for num in numbers if num < 0]
if_else = [num * 2 if num < 0 else num * 3 for num in numbers]