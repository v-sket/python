import numpy as np
import matplotlib.pyplot as plt

user = ["A", "B", "C", "D", "E", "F", "G", "G", "H", "I"]
star = [4, 1, 5, 3, 2, 1, 4, 4, 5, 3]

plt.bar(user, star)
plt.xlabel("User")
plt.ylabel("Star")
plt.show()

plt.scatter(user, star)
plt.xlabel("User")
plt.ylabel("Star")
plt.show()

print(np.mean(star))