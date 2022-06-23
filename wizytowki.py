
class BusinessCard:
    def __init__(self, name, surname, company, job_position, e_mail):
        self.name = name
        self.surname = surname
        self.company = company
        self.job_position = job_position
        self.e_mail = e_mail 
        
    def __str__(self):
        return f"{self.name}  ,  {self.surname}  ,  {self.company}  ,  {self.job_position}  ,  {self.e_mail}"
    #def __repr__(self):
        #return f"BusinessCard (name={self.name} surname={self.surname} company={self.company} job_position={self.job_position} e_mail={self.e_mail}"

MagdaRatajczak = BusinessCard(name = "Magda" ,surname = "Ratajczak", company = "Big_company", job_position = "technical advisor", e_mail = "magda.ratajczak@company.pl" )
StanislawRatajczak = BusinessCard(name = "Stanislaw" ,surname = "Ratajczak", company = "Very_Big_COmpany", job_position = "boss", e_mail = "boss@boss.pl" )
IgnacyRatajczak = BusinessCard(name = "Ignacy" ,surname = "Ratajczak", company = "Dziecko", job_position = "dziecko-9", e_mail = "Igidziecko@dziecko.pl" )
GabrielRatajczak = BusinessCard(name = "Gabriel" ,surname = "Ratajczak", company = "Dziecko", job_position = "dziecko-8", e_mail = "Gabrychdziecko@dziecko.pl" )
AugustynRatajczak = BusinessCard(name = "Augustyn" ,surname = "Ratajczak", company = "Dziecko", job_position = "dziecko-6", e_mail = "Augustyndziecko@dziecko.pl" )

adress_book = [MagdaRatajczak, StanislawRatajczak, IgnacyRatajczak, GabrielRatajczak, AugustynRatajczak]

for i in adress_book:
    print (i.name, i.surname, i.company, i.job_position, i.e_mail)

by_name = sorted(adress_book, key=lambda BusinessCard: BusinessCard.name)

print("Sortowanie po imieniu")

for a in by_name:
    print (a.name, a.surname, a.company, a.job_position, a.e_mail)


by_surname = sorted(adress_book, key=lambda BusinessCard: BusinessCard.name)

print("Sortowanie po nazwisku")
for b in by_surname:
    print (b.name, b.surname, b.company, b.job_position, b.e_mail)