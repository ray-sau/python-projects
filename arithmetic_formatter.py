def arithmetic_arranger(problems, solve=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  firstline=""
  secondline=""
  dashes=""
  answers=""
  arranged_problems=""

  for problem in problems:
    firstnum=problem.split()[0]
    operator=problem.split()[1]
    secondnum=problem.split()[2]

    if operator != "-" and operator != "+":
      return "Error: Operator must be '+' or '-'."

    if firstnum.isdigit()==False or secondnum.isdigit()==False:
      return "Error: Numbers must only contain digits."

    if len(firstnum)>4 or len(secondnum)>4:
      return "Error: Numbers cannot be more than four digits."

    length=max(len(firstnum),len(secondnum))+2

    top=str(firstnum).rjust(length)
    bot=operator + str(secondnum).rjust(length-1)
    dash=""
    for i in range(length):
      dash+="-"
      
    answer=0
  
    if operator == "-":
      answer= int(firstnum)-int(secondnum)
    elif operator == "+":
      answer=int(firstnum)+int(secondnum)

    firstline+=top + "    "
    secondline+=bot + "    "
    dashes+=dash + "    "

    answers+=str(answer).rjust(length) + "    "
    arranged_problems = firstline +"\n"+ secondline + "\n"+ dashes
    if solve==True:
      arranged_problems = firstline +"\n"+ secondline + "\n"+ dashes + "\n"+answers
         
  return arranged_problems
  
  print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
