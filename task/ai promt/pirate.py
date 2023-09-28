import random

# Define lists of horror, comedy, pirate, and inspirational elements
horror_elements = [
    "creepy mansion",
    "ghostly apparition",
    "dark and stormy night",
    "haunted treasure chest",
    "eerie whispers",
]

comedy_elements = [
    "bumbling pirate crew",
    "mischievous parrot",
    "slapstick humor",
    "comical misunderstandings",
    "pratfalls",
]

pirate_elements = [
    "Captain Blackbeard",
    "sailing the high seas",
    "treasure map",
    "swords and cannons",
    "pirate code",
]

inspirational_elements = [
    "courage and determination",
    "overcoming adversity",
    "unbreakable bonds of friendship",
    "the power of teamwork",
    "never giving up",
]

# Create the story
story = []

# Introduction
story.append("Once upon a time, in a world filled with pirates and mystery...")

# Horror Element
horror_element = random.choice(horror_elements)
story.append(f"But on a {horror_element}, fear gripped the hearts of our brave crew. "
             "The mansion's ancient walls creaked, and the air was thick with dread.")

# Comedy Element
comedy_element = random.choice(comedy_elements)
story.append(f"The situation quickly turned comical as a {comedy_element} joined the crew. "
             "The crew members stumbled over each other, and the parrot played pranks on them.")

# Pirate Element
pirate_element = random.choice(pirate_elements)
story.append(f"Led by the infamous {pirate_element}, they set sail in search of a legendary treasure. "
             "Their ship, 'The Black Pearl,' cut through the turbulent waters with its tattered sails.")

# Inspirational Element
inspirational_element = random.choice(inspirational_elements)
story.append(f"Despite the challenges, their {inspirational_element} kept them going. "
             "They knew that the treasure was not just gold but a symbol of their dreams.")

# Climax
story.append("As they followed the ancient map to the treasure's location, they encountered fierce storms, "
             "rival pirates, and treacherous cliffs. Each obstacle tested their resolve and camaraderie.")

# Resolution
story.append("In the end, they reached the treasure's hidden cave, guarded by the ghostly apparition "
             "of Captain Blackbeard himself. With courage, they faced their fears and unlocked the chest.")

# Conclusion
story.append("The treasure they found wasn't just riches; it was the realization that they had become a family, "
             "forged through adversity. They sailed off into the horizon, inspired by their journey, "
             "and the world knew them as legendary pirates who found much more than gold.")

# Print the story
for index, line in enumerate(story):
    print(f"{index + 1}. {line}")

# Save the story to a text file
with open("pirate_story.txt", "w") as file:
    for line in story:
        file.write(line + "\n")

print("The detailed story has been saved to 'pirate_story.txt'.")
