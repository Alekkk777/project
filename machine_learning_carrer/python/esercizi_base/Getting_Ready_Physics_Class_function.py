# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 

def f_to_c(f_temp):
  c_temp=(f_temp - 32)*5/9;
  return c_temp
f100_in_celsius=100
print(f_to_c(f100_in_celsius))

def c_to_f(c_temp):
  f_temp=(c_temp*9/5)+32
  return f_temp
c0_in_fahrenheit=0;
print(c_to_f(c0_in_fahrenheit))

def get_force(mass,acceleration):
  force=mass*acceleration
  return force
print("The GE train supplies X Newtons of force: "+str(get_force(train_mass,train_acceleration)))

def get_energy(macc):
  c=3*10**8
  energy=macc*(c**2)
  return energy
bomb_energy=get_energy(bomb_mass)
print("A 1kg bomb supplies X Joules:"+str(bomb_energy))
def get_work(mass,acceleration,distance,fun):
  force=fun(mass,acceleration)
  train_work=force*distance
  return train_work
print("The GE train does "+str(get_work(train_mass,train_acceleration,train_distance,get_force))+" Joules of work over "+str(train_distance)+" meters")
