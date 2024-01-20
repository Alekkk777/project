weight=8.4;
comment="Ground Shipping";
cost_ground_premium = 125.00;
if weight <= 20:
  cost_ground = weight * 1.5 + 20;
elif weight >20 and weight <=60:
  cost_ground = weight * 2 + 20;
elif weight >60 and weight <=100:
  cost_ground = weight * 2.5 + 30;
else:
  cost_ground = weight * 3 + 30;
print("Ground Shipping basic $",cost_ground)
print("Ground Shipping Premium $", cost_ground_premium)
if weight <= 20:
  drone_cost_ground = weight * 3 + 20;
elif weight >20 and weight <=60:
  drone_cost_ground = weight * 2 + 20;
elif weight >60 and weight <=100:
  drone_cost_ground = weight * 2.5 + 30;
else:
  drone_cost_ground = weight * 3 + 30;
print("Ground Shipping Premium $",drone_cost_ground)