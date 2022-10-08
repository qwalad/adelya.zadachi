
sample = ["Green", "White", "Black"]
b = ["Red" , "Pink" , "Yellow"]
c = sample + b
print(c)
d = list(c)
d[0] , d[3] = d[3] , d[0]
print(d)
z = list(d)
z[3] , z[1] = z[1] , z[3]
print(z)
w = list(z)
w[2] , w[3] = w[3] , w[2]
print(w)
