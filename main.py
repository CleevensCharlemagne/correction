def finalGrade(resitation, test, exam):
  resitation = (resitation*5)/10

  final = test + resitation + exam

  return final

if __name__ == '__main__':
  run = ""
  while run != "x":
    res = float(input("resitation: "))
    test = float(input("Test d'evaluation: "))
    exam = float(input("Examen: "))

    print(finalGrade(res, test, exam))
    run = input("continue or not?  ")
    print("")