donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

total_donations = 0
for val in donations.values():
    total_donations += val

donations.values()
donations.keys()
donations.items()

instructor = {
    'name': 'Alex'
}

'age' in instructor # false
'Alex' in instructor.values() # True