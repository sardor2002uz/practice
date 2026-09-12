print("==== number =====")
# in JAVA, variable is a name storage location!  // => malumot manzilning nomlanishi
# in Python, variable is named reference!       // => veriable bu reference ning nomlanishi

count = 100
count_type = type(count)
print("count:", count, count_type)
print(f"the count: {count} and type: {count_type}")

result1 = count.bit_count()  # method
resukt2 = count.numerator  # state
print(result1, resukt2)
