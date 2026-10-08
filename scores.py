scores = list(map(float, input("Enter scores: ").split()))

print("Sum:", sum(scores))
print("Average:", sum(scores) / len(scores))
print("Maximum:", max(scores))
print("Minimum:", min(scores))