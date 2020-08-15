from basic import db,Puppy

my_puppy = Puppy('rufus',12)

db.session.add(my_puppy)
db.session.commit()

print("showing all data")
all_puppies=Puppy.query.all()
print(all_puppies)

print("selecting by id")
one_puppy=Puppy.query.get(1)
print(one_puppy.name)

print("using filters")
puppy_lucy=Puppy.query.filter_by(name='lucy')
print(puppy_lucy.all())

print("update")
first_puppy=Puppy.query.get(1)
first_puppy.age=10
db.session.add(first_puppy)
db.session.commit()
print("showing all data")
all_puppies=Puppy.query.all()
print(all_puppies)

print("delete")
second_puppy=Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()
print("showing all data")
all_puppies=Puppy.query.all()
print(all_puppies)








