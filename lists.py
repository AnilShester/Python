name_lists = ["Kritika", "Ambika", "Amrit"]
print(name_lists[2] + " cannot make it to the party.")

new_person = "Ajeep"
name_lists.remove("Amrit")
name_lists.append(new_person)
print(name_lists)

name_lists.insert(0, "Shreya")
name_lists.insert(1, "Nani chhori")
name_lists.append("prashya")

print(name_lists)

print("There is space for only two guests.")

guest_removed_1 = name_lists.pop()
print(guest_removed_1 + "You are removed.")
guest_removed_2 = name_lists.pop()
print(guest_removed_2 + "You are removed.")
guest_removed_3 = name_lists.pop()
print(guest_removed_3 + "You are removed.")
guest_removed_4 = name_lists.pop()
print(guest_removed_4 + "You are removed.")

print(name_lists)

del name_lists[0]
del name_lists[0]
print(name_lists)