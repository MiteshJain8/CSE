def stable_matching(men_preferences, women_preferences):
    free_men = list(men_preferences.keys())
    engagements = {woman: None for woman in women_preferences.keys()}
    proposals = {man: [] for man in men_preferences.keys()}

    while free_men:
        man = free_men.pop(0)
        man_pref = men_preferences[man]

        for woman in man_pref:
            if woman not in proposals[man]:
                proposals[man].append(woman)
                if engagements[woman] is None:  # woman is free
                    engagements[woman] = man
                    break
                else:
                    current_partner = engagements[woman]
                    woman_pref = women_preferences[woman]

                    if woman_pref.index(man) < woman_pref.index(current_partner):
                        engagements[woman] = man
                        free_men.append(current_partner)
                        break

    result = [(engagements[woman], woman) for woman in engagements]
    return result

men_preferences = {
    "Abe": ["Abi", "Eve", "Cat"],
    "Col": ["Eve", "Cat", "Abi"],
    "Bob": ["Cat", "Abi", "Eve"]
}

women_preferences = {
    "Eve": ["Abe", "Bob", "Col"],
    "Abi": ["Bob", "Abe", "Col"],
    "Cat": ["Col", "Abe", "Bob"]
}

matches = stable_matching(men_preferences, women_preferences)

print("Stable matches:")
for man, woman in matches:
    print(f"{man} is matched with {woman}")