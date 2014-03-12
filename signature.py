column1 = ["over the wintry", "forest, winds howl in rage", "with no leaves to blow", "- Natsume Soseki"]
column2 = ["Ben Livingood", "", "", "PHONE/SMS: (406)285-1066"]

data = zip(column1,column2)

col_width = max(len(word) for row in data for word in row) + 25  # padding
for row in data:
    print ".".join(word.ljust(col_width) for word in row)
