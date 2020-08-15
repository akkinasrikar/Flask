from basic import db,Puppy
import warnings
warnings.filterwarnings('ignore')
db.create_all()

sai=Puppy('lucy',3)
ram=Puppy('mike',5)

print(sai.id)
print(ram.id)

db.session.add_all([sai,ram])
db.session.commit()
 
print(sai.id)
print(ram.id)

