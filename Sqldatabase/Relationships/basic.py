from relationships import db,Puppy,Owner,Toy

lucy=Puppy('Lucy')
bear=Puppy('Bear')

db.session.add_all([lucy,bear])

db.session.commit()

print(Puppy.query.all())

lucy=Puppy.query.filter_by(name='Lucy').first()

srikar=Owner('Srikar',lucy.id)

toy1=Toy('Ball', lucy.id)
toy2=Toy('Roll', lucy.id)

db.session.add_all([srikar,toy1,toy2])
db.session.commit()

lucy=Puppy.query.filter_by(name='Lucy').first()

print(lucy)

lucy.report_toys()