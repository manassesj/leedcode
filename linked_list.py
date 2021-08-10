sum = 0

current_node = head

while True:
    if current_node is None:
        break
    else:
        sum += 1
        current_node = current_node.next

print(sum)
