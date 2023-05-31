import numpy as np
print("Hello world.")

x = np.random.randn(1000, 2)
output = "\n".join([",".join(_.astype(str)) for _ in x])

with open("results.csv", "w") as o:
    o.write(output)
