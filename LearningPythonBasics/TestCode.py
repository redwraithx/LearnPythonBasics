# just random things I ran across on Twitter where I was testing my theory of a code snipit and what the results \
# were than testing those results

print('{:,}'.format(1112223334))
print(3*1**3)


# returns false true
d1 = {"1": 'TATA', "2": 'FORD'}
d2 = {"1": 'TATA', "2": 'FORD'}
print(d1 is d2)
print(d1 == d2)


# returns ""
s = "python"
print("S:"+ s[6:] + "Next line")


# Quiz time len of set
# can only add unique, size is 3
cities = set()
cities.add("Delhi")
cities.add("Mumbai")
cities.add("Banglore")
cities.add("Mumbai")
cities.add("Bhopal")
cities.remove("Mumbai")
print("cities len:", len(cities))



# built in priority Queue
import queue

# create a priority queue
pq = queue.PriorityQueue()

# add items to the queue with a priority number
pq.put((1, 'Task with Priority 1'))
pq.put((3, 'Task with Priority 3'))
pq.put((2, 'Task with Priority 2'))

# retrieve items from the queue
while not pq.empty():
    priority, task = pq.get()
    print(f'Priority: {priority}, Task: {task}')



# daily test
my_list = [1, 2, 3, 4, 5]
new_list = my_list[1:4]
new_list.append(6)
print(len(my_list), len(new_list))


# daily test
my_dict = {"name": "John"}
print(my_dict.values() == my_dict.values())

# daily test
x = ['a', 'b', 'c', 'd']
y = x[2:]
y[1] = 'f'

print(y)
print(x)


# daily test
def add_to_list(lst, item):
    lst = lst + [item]
    return lst


a = [1, 2, 3]
print(add_to_list(a, 4))
print(a)

# daily test
L = ['a', 'b', 'c', 'd']
res = ''.join(L)
print(res)


# daily test
list1 = [1, 2, 3]
list2 = list1
list1.append(list2)
print(list1)


# daily first time using classes
class Car:
    def printSize(selfself):
        print("small")

class HatchBack(Car):
    def printSize(selfself):
        super().printSize()
        print("medium")


hatch = HatchBack()
hatch.printSize()


# daily
def func(x=1, y=2):
    x = x + y
    y += 1
    print(x, y)


# = 3 3
func(y=2, x=1)


# daily

