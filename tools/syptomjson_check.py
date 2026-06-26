import json


with open("knowledge_base/disease_guidelines.json") as f:
    diseases = json.load(f)

with open("knowledge_base/pest_guidelines.json") as f:
    pests = json.load(f)


print("Diseases:", len(diseases))
print("Pests:", len(pests))

print("\nDisease classes:")
for x in diseases:
    print(x)

print("\nPest classes:")
for x in pests:
    print(x)