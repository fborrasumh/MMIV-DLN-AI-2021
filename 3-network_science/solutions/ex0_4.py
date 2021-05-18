# get list of degrees
deg = [d for n,d in G.degree]
# density=True does normalization for us
plt.hist(deg, density=True)
plt.xticks(deg)
plt.show()