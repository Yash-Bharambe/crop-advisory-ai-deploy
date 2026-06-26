import os
from collections import Counter

DATASET="datasets/ip102_balanced/train"

classes=os.listdir(DATASET)

print("Classes:",len(classes))

counts={}

for c in classes:
    path=os.path.join(DATASET,c)
    counts[c]=len(os.listdir(path))


print("\nMAX:")
print(max(counts.values()))

print("\nMIN:")
print(min(counts.values()))

print("\nAverage:")
print(sum(counts.values())//len(counts))


print("\nFirst 10:")
for k,v in list(counts.items())[:10]:
    print(k,v)