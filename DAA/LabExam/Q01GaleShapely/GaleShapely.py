def stable_match(men_prefs, women_prefs):
    # Initialize all men and women as free
    free_men = list(men_prefs.keys())
    engagements = {}
    # While there are free men
    while free_men:
        man = free_men.pop(0)
        # Get the preferences of the man
        man_pref = men_prefs[man]
        # Propose to the first woman in the man's preference list
        woman = man_pref.pop(0)
        fiance = engagements.get(woman)
        # If the woman is not engaged, engage her with the current man
        if not fiance:
            engagements[woman] = man
        else:
            # If the woman prefers the current man over her fiance
            if women_prefs[woman].index(man) < women_prefs[woman].index(fiance):
                engagements[woman] = man
                free_men.append(fiance)
            else:
                # The woman rejects the proposal
                free_men.append(man)
    return engagements
# Note: Take user input in exam
men_prefs = {
    'm1': ['w1', 'w2', 'w3'],
    'm2': ['w2', 'w3', 'w1'],
    'm3': ['w3', 'w1', 'w2']
}
women_prefs = {
    'w1': ['m2', 'm3', 'm1'],
    'w2': ['m1', 'm2', 'm3'],
    'w3': ['m1', 'm3', 'm2']
}

stableMatches = stable_match(men_prefs, women_prefs)
print("Stable Matches:")
for woman, man in stableMatches.items():
    print(f"{man} engaged to {woman}")