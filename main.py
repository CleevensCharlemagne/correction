def finalGrade(resitation, test, exam):
  resitation = (resitation*5)/10

  final = test + resitation + exam

  return final

def finalGrade2(res1, res2, test, exam):
  resitation = ((res1+res2)*5)/20

  final = test + resitation + exam

  return final

if __name__ == '__main__':
  run = ""
  while run != "x":
    res1 = float(input("resitation 1: "))
    res2 = float(input("resitation 2: "))
    test = float(input("Test d'evaluation: "))
    exam = float(input("Examen: "))

    print(finalGrade2(res1, res2, test, exam)*150/100)
    run = input("continue or not?  ")
    print("")