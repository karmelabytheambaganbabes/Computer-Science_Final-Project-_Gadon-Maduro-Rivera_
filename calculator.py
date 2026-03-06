print("Welcome to The Cooking Mathematician!")

recipe = []

while True:
    ing = input("\nIngredient (or 'done'): ")
    if ing.lower() == "done":
        break
    
    amt = float(input("Amount: "))
    unit = input("Unit: ")
    per_serv = float(input("Per serving: "))
    servs = int(input("Servings: "))

    total = per_serv * servs
    adj = total / amt

    # Scale part (super simple)
    use_scale = input("Use scale? (y/n): ").lower()
    scale_wt = "Not used"
    if use_scale == "y":
        scale_wt = float(input("Scale weight (g): "))

    recipe.append({"ing": ing, "adj": adj, "unit": unit, "scale": scale_wt})

print(f"\nAdjusted for {servs} servings:")
for item in recipe:
    print(f"- {item['adj']:.2f} {item['unit']} of {item['ing']}")
    if item['scale'] != "Not used":
        print(f"  Scale: {item['scale']}g")

print("\nRecipe saved!")
git add calculator.py
git commit -m "Added mini scale feature to core calculator"
git push