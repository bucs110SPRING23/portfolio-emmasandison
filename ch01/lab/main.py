import random
# Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 5
cost_per_class = (cost_per_week / classes_per_week)
print("Each class costs $",cost_per_class,"per week")
print(weeks, type(weeks))
print(classes, type(classes))
print(tuition, type(tuition))
print(cost_per_week,type(cost_per_week))
print(classes_per_week, type(classes_per_week))
print(cost_per_class, type(cost_per_class))

# Part B
mylist = ["cat", "shark", "giraffe", "salamander", "guinea pig", "hummingbird"]
random_animal = random.choice(mylist)
print(random_animal)
