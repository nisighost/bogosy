import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt #mampiasa dp 

categorie = ["LAHY","VAVY"]
valeur = [1598462,1000000]
colors = ['purple', 'magenta']

plt.bar(categorie , valeur, color = colors)

plt.title("iSA")
plt.xlabel("TAUX")
plt.ylabel("ISA")

plt.show()