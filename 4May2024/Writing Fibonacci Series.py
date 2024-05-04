fi = [0,1]


#not able to understand #now understand
for i in range (5):
    fi.append(fi[-1]+fi[-2])
print(fi)

print(','.join(str(e) for e in fi))
