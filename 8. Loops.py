# While Loops & For Loops

# While Loops

x = 0                                          
while (x < 10): # 0-9                         
    print(x)     
    x = x + 1

# For Loops

for x in range(1,20): # 1-19
    print(x)

# Array
    
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for x in days:
    print(x)

# If Statement
    
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for x in days:
    if (x == "Friday"):break         # Loop Breakes
    print(x)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for x in days:
    if (x == "Friday"):continue         # Skip x
    print(x)