# Program 4 - Independent Task: Build a Shopping List Interactively

shopping_list = []
item = input("Enter item (or 'done' to finish): ")      # input: milk
while item != "done":                                   # 'done' aate hi ruk jao
    shopping_list.append(item)
    item = input("Enter item (or 'done' to finish): ")  # input: bread, eggs, done

print("Your shopping list:", shopping_list)  # Output: Your shopping list: ['milk', 'bread', 'eggs']
print("Total items:", len(shopping_list))   # Output: Total items: 3
