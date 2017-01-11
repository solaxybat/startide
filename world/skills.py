"""
Master Skill Listing

This file containts a dict of dicts that describe all the skills
available on Startide. It is a modified list from CP2020 and
some of the expansion material. Please note that not all descriptions
will be filled in, as this is still prototyping!

A skill is described by the following:
{"Skill Name":{
               "Desc":"Description of the Skill",
               "Mult":"Cost Multiplier",
               "Chip":T/F (Can be chipped),
               "Spec":T/F (Can have specialties),
               "Base":"Base Statistic to use for Rolls"
}}
"""

ALL_SKILLS = {"Personal Grooming":{
                "Desc":"This is the skill of knowing proper grooming "
                       "hair styling, etc., to maximize your physical "
                       "attractiveness. This skill can be used to boost "
                       "rolls for Relationships or Persuasion. A good "
                       "looking person would be +2, fashion models are "
                       "+6 or better.",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"EMP"},
              "Wardrobe & Style":{
                "Desc":"The skill of knowing the right clothes to wear, "
                       "when to wear them, and how to look cool even in "
                       "a spacesuit. With Wardrobe of +2 or better, you "
                       "are good at choosing clothes off the rack. At +8 "
                       "or better, you are one of those rare people whose "
                       "personal style influences fashion.",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"EMP"},
              "Endurance":{
                "Desc":"This is the ability to withstand pain or hardship, "
                       "particularly over long periods of time, by knowing "
                       "the best ways to conserve strength and energy. "
                       "Endurance skill checks are made when the character "
                       "is exhausted, but must continue - such as periods "
                       "without food, sleep or water.",
                "Mult":1,
                "Chip":False,
                "Spec":False,
                "Base":"BOD"},
              "Strength Feat":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":False,
                "Spec":False,
                "Base":"STR"},
              "Swimming":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"BOD"},
              "Interrogation":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"COOL"},
              "Intimidate":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":False,
                "Spec":False,
                "Base":"COOL"},
              "Oratory":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"COOL"},
              "Resist Torture & Drugs":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":False,
                "Spec":False,
                "Base":"COOL"},
              "Streetwise":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"COOL"},
              "Leadership":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"EMP"},
              "Social":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"EMP"},
              "Persuasion & Fast Talk":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"EMP"},
              "Perform":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":True,
                "Base":"EMP"},
              "Accounting":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"INT"},
              "Anthropology":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"INT"},
              "Awareness & Notice":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":False,
                "Spec":False,
                "Base":"INT"},
              "Biology":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"INT"},
              "Botany":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"INT"},
              "Chemistry":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"INT"},
              "Diagnose Illness":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"INT"},
              "General Education":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":False,
                "Spec":False,
                "Base":"INT"},
              "Gamble":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"INT"},
              "Geology":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"INT"},
              "Hide & Evade":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":False,
                "Spec":False,
                "Base":"INT"},
              "Library Search":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"INT"},
              "Physics":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"INT"},
              "Programming":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":False,
                "Spec":False,
                "Base":"INT"},
              "Shadow & Track":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"INT"},
              "Teaching":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"INT"},
              "Wilderness Survival":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":True,
                "Base":"INT"},
              "Zoology":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"INT"},
              "Xenobiology":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":False,
                "Spec":False,
                "Base":"INT"},
              "Archery":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"DEX"},
              "Athletics":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"REF"},
              "Brawling":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"DEX"},
              "Dance":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"REF"},
              "Dodge & Escape":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"REF"},
              "Driving":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"REF"},
              "Fencing":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"DEX"},
              "Handgun":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"DEX"},
              "Heavy Weapons":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"DEX"},
              "Melee":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"DEX"},
              "Pilot Gyro":{
                "Desc":"TBD",
                "Mult":3,
                "Chip":True,
                "Spec":False,
                "Base":"REF"},
              "Pilot Atmospheric":{
                "Desc":"TBD",
                "Mult":2,
                "Chip":True,
                "Spec":False,
                "Base":"REF"},
              "Pilot Space Craft":{
                "Desc":"TBD",
                "Mult":3,
                "Chip":True,
                "Spec":False,
                "Base":"REF"},
              "Pilot Space Ship":{
                "Desc":"TBD",
                "Mult":3,
                "Chip":True,
                "Spec":False,
                "Base":"REF"},
              "Rifle":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"DEX"},
              "Stealth":{
                "Desc":"TBD",
                "Mult":2,
                "Chip":False,
                "Spec":False,
                "Base":"REF"},
              "Submachinegun":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"DEX"},
              "Aero Tech":{
                "Desc":"TBD",
                "Mult":2,
                "Chip":True,
                "Spec":False,
                "Base":"TECH"},
              "AV Tech":{
                "Desc":"TBD",
                "Mult":3,
                "Chip":True,
                "Spec":False,
                "Base":"TECH"},
              "Basic Tech":{
                "Desc":"TBD",
                "Mult":2,
                "Chip":True,
                "Spec":False,
                "Base":"TECH"},
              "Cryotank Operation":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"TECH"},
              "Cyber Tech":{
                "Desc":"TBD",
                "Mult":2,
                "Chip":True,
                "Spec":False,
                "Base":"TECH"},
              "Demolitions":{
                "Desc":"TBD",
                "Mult":2,
                "Chip":True,
                "Spec":False,
                "Base":"TECH"},
              "Disguise":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"BOD"},
              "Electronic Security":{
                "Desc":"TBD",
                "Mult":2,
                "Chip":True,
                "Spec":False,
                "Base":"TECH"},
              "First Aid":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"TECH"},
              "Forgery":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"TECH"},
              "Gyro Tech":{
                "Desc":"TBD",
                "Mult":3,
                "Chip":True,
                "Spec":False,
                "Base":"TECH"},
              "Art":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"TECH"},
              "Pharmaceuticals":{
                "Desc":"TBD",
                "Mult":2,
                "Chip":True,
                "Spec":False,
                "Base":"TECH"},
              "Pick Lock":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"TECH"},
              "Pick Pocket":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"TECH"},
              "Play Instrument":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":True,
                "Base":"TECH"},
              "Weaponsmith":{
                "Desc":"TBD",
                "Mult":2,
                "Chip":True,
                "Spec":False,
                "Base":"TECH"},
              "Zero G Manuever":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":False,
                "Spec":False,
                "Base":"REF"},
              "Zero G Combat":{
                "Desc":"TBD",
                "Mult":2,
                "Chip":False,
                "Spec":False,
                "Base":"DEX"},
              "Prospecting":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"INT"},
              "Aikido":{
                "Desc":"TBD",
                "Mult":3,
                "Chip":True,
                "Spec":False,
                "Base":"DEX"},
              "Kung Fu":{
                "Desc":"TBD",
                "Mult":3,
                "Chip":True,
                "Spec":False,
                "Base":"DEX"},
              "Boxing":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"BOD"},
              "Karate":{
                "Desc":"TBD",
                "Mult":2,
                "Chip":True,
                "Spec":False,
                "Base":"BOD"},
              "Wrestling":{
                "Desc":"TBD",
                "Mult":1,
                "Chip":True,
                "Spec":False,
                "Base":"BOD"},
}}