class Etudiant:
    """defintion du class"""
    def __init__(self, nom, prenom, age, cne, moyenne):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne


# la liste d'etudiant
studentsList = [ Etudiant("benha", "mira", 21, "P8764235", 12),
             Etudiant("toong", "hamid", 20, "P1408883", 19),
             Etudiant(" 3aba", "kamla", 22, "P1338764", 8.5),
             Etudiant("sandi", "morro", 21, "P1332878", 8),
             Etudiant("innai", "nora", 23, "P1503373", 11.5)]

# triage selon l'age 
def sortByAge(student):
    return student.age

studentsList.sort(key=sortByAge)

for student in studentsList:
    print(".........")
    print(student.nom)
    print(student.prenom)
    print(student.age)
print(".....end of list.........")

# triage selon la moyenne
def sortByAverage(student):
    return student.moyenne

studentsList.sort(key=sortByAverage)

for student in studentsList:
    print("...........")
    print(student.nom)
    print(student.prenom)
    print(student.moyenne)

print("......end of list.........")