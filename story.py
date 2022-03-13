import random

kada = ["pre nekoliko godina", "juce", "zadnje vece", "Nekada davno"]
ko = ["zec", "slon", "mis", "kornjaca", "macka"]
ime = ["Alija", "Mehmed", "Ajna", "Ahmed", "Muhamed", "Tajiba", "Nenad", "Emir"]
mesto = ["Skola", "Indija", "Kuca", "Venecija", "Engleska"]
otisao = ["bioskop", "univerzitet", "seminar", "skola", "perionica", "programiranje"]
desilo_se = [
    "sreo zmaja",
    "jede burger",
    "nasao strasni kljuc",
    "usporio misteriju",
    "napisao knigu",
    "porucio ps5",
    "dobio 5",
    "izgubio mozak",
]
print(
    random.choice(kada)
    + ", "
    + random.choice(ko)
    + " , "
    + random.choice(mesto)
    + ", otisao "
    + random.choice(otisao)
    + " i "
    + random.choice(desilo_se)
)
