# Program 5 - Independent Task: Unique Visitor Tracker

visitor_ids = [101, 102, 101, 103, 102, 104, 101]   # kuch visitors repeat hue
unique_visitors = set(visitor_ids)                   # set -> har ID sirf ek baar
print("Unique visitors:", len(unique_visitors))      # Output: Unique visitors: 4
print("IDs:", unique_visitors)                       # Output: IDs: {104, 101, 102, 103} (set ka order fix nahi hota)
