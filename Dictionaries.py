x = {}
print(type(x))


file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)


file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts["txt"])


file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print("jpg" in file_counts)
print("html" in file_counts)


file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
file_counts["cfg"] = 8
print(file_counts)


file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
file_counts["csv"] = 17
print(file_counts)


file_counts = {"jpg":10, "txt":14, "csv":2, "py":23, 'cfg':8}
del file_counts["cfg"]
print(file_counts)


file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts:
  print(extension)