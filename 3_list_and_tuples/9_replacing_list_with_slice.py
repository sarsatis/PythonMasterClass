computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]
print(computer_parts)

# In the below example index 3 is replaced with trackball
# computer_parts[3] = "trackball"
print(computer_parts[3:])

# In the below example items from index 3 is replaced with trackball
computer_parts[3:] = ["trackball"]
print(computer_parts)