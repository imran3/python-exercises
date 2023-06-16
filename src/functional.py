def double(x): return x * 2
def isEven(x): return x % 2 == 0


# map
nums = range(0, 20)
double_nums = list(map(double, nums))
print(double_nums)

# filter
even_nums = list(filter(isEven, nums))
print(even_nums)

# lambdas: nameless, one liner functions
add = lambda x, y, z: x + y + z
print(add(1, 5 , 3))
print(list(map(lambda x: x *2, nums))) # double nums

# list comprehension: readable way of transforming elements in list
squared_nums = [x ** 2 for x in nums]
print(squared_nums)
evens_squared = [x ** 2 for x in nums if x % 2 == 0] # filter and maps nums
print(evens_squared)

# reducing: given an iterable, such as list, reduces list to one value by applying input function
from functools import reduce
def get_sum(acc, x):
    return acc + x
sum_nums = reduce(get_sum, nums)
print(sum_nums)

# combining list
# find average salary of developers, from following input data
employees = [
    {'name': 'John Doe', 'job_title': 'Developer', 'salary': 80000},
    {'name': 'Jane Smith', 'job_title': 'Data Analyst', 'salary': 60000},
    {'name': 'Mike Johnson', 'job_title': 'Project Manager', 'salary': 90000},
    {'name': 'Emily Davis', 'job_title': 'Marketing Specialist', 'salary': 55000},
    {'name': 'Emily Smith', 'job_title': 'Developer', 'salary': 55000}
]

def is_developer(employee):
    return employee['job_title'] == 'Developer'
def get_salary(employee):
    return employee['salary']
developers = list(filter(is_developer, employees))
print(developers)

developer_salaries = list(map(get_salary, developers))
print(developer_salaries)

total_dev_salaries = reduce((lambda acc, x: acc + x), developer_salaries)
average_dev_salary = total_dev_salaries / len(developer_salaries)
print(total_dev_salaries)
print(average_dev_salary)

# solution using list comprehension
devs = [x['salary'] for x in employees if x['job_title'] == 'Developer']
dev_avg_salary = sum(devs)/len(devs)
print(dev_avg_salary)