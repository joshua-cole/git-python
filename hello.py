# a simple dice simulator
import numpy as np

msg = "Roll a dice!"
print(msg)

result = np.random.randint(1,20)
print(result)

if result == 20:
    print("Nat 20 baby!")
elif result >= 11:
    print("Good roll")
elif result >= 2:
    print("Ouch")
else: 
    print("You're screwed")