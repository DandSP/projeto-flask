from flask import Flask, render_template, redirect, request
import datetime


resp = ""

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", txt_titulo="Lista de Exercícios")

@app.route('/resposta')
def resposta(): 
  return render_template("respostas.html", txt_titulo="Resposta", R=resp)
  
@app.route('/ex1')
def ex1():
  return render_template("ex1.html", txt_titulo="Exercício 1")

@app.route('/res1', methods=['GET','POST'])
def res1():
  global resp
  resp=""
  resp = "Seja bem-vindo, " + request.form['nome'] + "!"
  return redirect('/resposta') 

@app.route('/ex2')
def ex2():
  return render_template("ex2.html", txt_titulo="Exercício 2")

@app.route('/res2', methods=['GET','POST'])
def res2():
  global resp
  resp=""
  
  n1 = int(request.form['num1'])
  n2 = int(request.form['num2'])

  def ope(x,y):
    soma = x + y
    sub = x - y
    mult = x * y
    div = x / y
    
    return ("Soma = {:.4}".format(str(soma)) + "<br>" +
            "Subtração = {:.4}".format(str(sub)) + "<br>" +
            "Multiplicação = {:.4}".format(str(mult)) + "<br>" +
            "Divisão = {:.4}".format(str(div))
           )

  resp = ope(n1,n2)
  
  return redirect('/resposta')
  
@app.route('/ex3')
def ex3():
  return render_template("ex3.html", txt_titulo="Exercício 3")

@app.route('/res3', methods=['GET','POST'])
def res3():
  global resp
  resp=""
  
  num = float(request.form['numero'])
  
  def pi(num):
    if (num % 2 == 0):
      rp = num / 2
      return "O número {:.2}".format(str(num)) + " é par. Dividido por dois é: {:.2}".format(str(rp))
    else:
      ri = num / 3
      return "O número {:.2}".format(str(num)) + " é ímpar. Dividido por três é: {:.4}".format(str(ri))
    
  resp = pi(num) 
  
  return redirect('/resposta')

@app.route('/ex4')
def ex4():
  return render_template("ex4.html", txt_titulo="Exercício 4")

@app.route('/res4', methods=['GET','POST'])
def res4():
  global resp
  resp=""
  
  n1 = int(request.form['num1'])
  n2 = int(request.form['num2'])

  if n1 < n2:
    while n1 <= n2:
      resp = resp + str(n1) + ", "
      n1 += 1
    return redirect('/resposta')
    
  elif n1 == n2:
    return "Os números são iguais. Digite novamente!"
    
  elif n1 > n2:
    return "O primeiro número deve ser menor que o segundo. Digite novamente!"
    
  else:
    return "Opção inválida!"

@app.route('/ex5')
def ex5():
  return render_template("ex5.html", txt_titulo="Exercício 5")

@app.route('/res5', methods=['GET','POST'])
def res5():
  global resp
  resp=""
  
  n1 = int(request.form['num1'])
  n2 = int(request.form['num2'])

  if n1 < n2:
    while n1 <= n2:
      if n1 % 2 == 0:
        resp += str(n1) + ", "
      n1 += 1
    return redirect('/resposta')
        
  elif n1 == n2:
    return "Os números são iguais. Digite novamente!"
    
  elif n1 > n2:
    return "O primeiro número deve ser menor que o segundo. Digite novamente!"
    
  else:
    return "Opção inválida!"

@app.route('/ex6')
def ex6():
  return render_template("ex6.html", txt_titulo="Exercício 6")

@app.route('/res6', methods=['GET','POST'])
def res6():
  global resp
  resp=""


  n1 = int(request.form['num1'])
  n2 = int(request.form['num2'])

  if n1 < n2 and n1 > 0:
    while n1 <= n2:
      if n1 % 2 == 0:
        resp += str(n1) + ", "
      n1 += 1
    
  elif n1 < n2 and n1 < 0 or n2 < 0:
    resp = "O número digitado é negativo. Digite novamente!" 
    
  elif n1 == n2:
    resp = "Os números são iguais. Digite novamente!"
    
  elif n1 > n2:
    resp = "O primeiro número deve ser menor que o segundo. Digite novamente!"
    
  else:
    resp =  "Opção inválida!"

  return redirect('/resposta')

@app.route('/ex7')
def ex7():
  return render_template("ex7.html", txt_titulo="Exercício 7")

@app.route('/res7', methods=['GET','POST'])
def res7():
  global resp
  resp=""


  n1 = int(request.form['num1'])
  n2 = int(request.form['num2'])

  if n1 < n2 and n1 < 0 and n2 < 0:
    while n1 <= n2:
      if n1 % 2 == 0:
        resp += str(n1) + ", "
      n1 += 1
    
  elif n1 < n2 and n1 < 0 and n2 >= 0:
    resp = "Um dos números digitado é positivo. Digite novamente!" 
    
  elif n1 == n2:
    resp = "Os números são iguais. Digite novamente!"
    
  elif n1 > n2:
    resp = "O primeiro número deve ser menor que o segundo. Digite novamente!"
    
  else:
    resp = "Opção inválida!"

  return redirect('/resposta')


@app.route('/ex8')
def ex8():
  return render_template("ex8.html", txt_titulo="Exercício 8")

@app.route('/res8', methods=['GET','POST'])
def res8():
  global resp
  resp=""


  n1 = int(request.form['num1'])
  n2 = int(request.form['num2'])

  if n1 < n2 and n1 > 0 and n2 > 0:
    while n1 <= n2:
      if n1 % 2 != 0:
        resp += str(n1) + ", "
      n1 += 1
    
  elif n1 < n2 and n1 < 0 and n2 < 0:
    resp = "O número digitado é negativo. Digite novamente!" 
    
  elif n1 == n2:
    resp = "Os números são iguais. Digite novamente!"
    
  elif n1 > n2:
    resp = "O primeiro número deve ser menor que o segundo. Digite novamente!"
    
  else:
    resp = "Opção inválida!"

  return redirect('/resposta')

@app.route('/ex9')
def ex9():
  return render_template("ex9.html", txt_titulo="Exercício 9")

@app.route('/res9', methods=['GET','POST'])
def res9():
  global resp
  resp=""

  n1 = int(request.form['num1'])
  n2 = int(request.form['num2'])

  if n1 < n2 and n1 < 0 and n2 < 0:
    while n1 <= n2:
      if n1 % 2 != 0:
        resp += str(n1) + ", "
      n1 += 1
    
  elif n1 < n2 and n1 > 0 and n2 >= 0:
    resp = "O número digitado é positivo. Digite novamente!" 
    
  elif n1 == n2:
    resp = "Os números são iguais. Digite novamente!"
    
  elif n1 > n2:
    resp = "O primeiro número deve ser menor que o segundo. Digite novamente!"
    
  else:
    resp = "Opção inválida!"

  return redirect('/resposta')

@app.route('/ex10')
def ex10():
  return render_template("ex10.html", txt_titulo="Exercício 10")

@app.route('/res10', methods=['GET','POST'])
def res10():
  global resp
  resp=""

  dia = int(request.form['dia'])
  mes = int(request.form['mes'])
  ano = int(request.form['ano'])
  prod = int(request.form['prec'])
  
  data = datetime.date.today()
  diaAtual = data.day
  mesAtual = data.month
  anoAtual = data.year

  if (anoAtual - ano) >= 18:
    if mesAtual > mes:
      desc = prod - (prod * (0.1))
      resp = "Você é maior de idade e ganhou 10% de desconto. O seu produto de: " + str(prod) + "R$ ficou: " + str(desc) + "R$."
      return redirect('/resposta')
      
    elif mesAtual == mes:
      if diaAtual >= dia:
        desc = prod - (prod * (0.1))
        resp = "Você é maior de idade e ganhou 10% de desconto. O seu produto de: " + str(prod) + "R$ ficou: " + str(desc) + "R$."
        return redirect('/resposta')
        
      else:
        desc = prod - (prod * (0.05))
        resp = "Você é menor de idade e ganhou 5% de desconto. O seu produto de: " + str(prod) + "R$ ficou: " + str(desc) + "R$."
        return redirect('/resposta')
        
    elif mesAtual < mes:
      if (anoAtual - ano) > 18:
        desc = prod - (prod * (0.1))
        resp = "Você é maior de idade e ganhou 10% de desconto. O seu produto de: " + str(prod) + "R$ ficou: " + str(desc) + "R$."
        return redirect('/resposta')
        
      else:
        desc = prod - (prod * (0.05))
        resp = "Você é menor de idade e ganhou 5% de desconto. O seu produto de: " + str(prod) + "R$ ficou: " + str(desc) + "R$."
        return redirect('/resposta')
        
  else:
    desc = prod - (prod * (0.05))
    resp = "Você é menor de idade e ganhou 5% de desconto. O seu produto de: " + str(prod) + "R$ ficou: " + str(desc) + "R$."
    return redirect('/resposta')

  if dia > 31 or mes > 12 or ano > anoAtual:
    resp = "Data inválida!"
    return redirect('/resposta')

@app.route('/ex11')
def ex11():
  return render_template("ex11.html", txt_titulo="Exercício 11")

@app.route('/res11', methods=['GET','POST'])
def res11():
  global resp
  resp=""
  
  celcius = int(request.form['grau'])
  resp = str(celcius) + "º Celcius equivalem a " + str(int(celcius + 273)) + "º Kelvin"
  
  return redirect('/resposta')

@app.route('/ex12')
def ex12():
  return render_template("ex12.html", txt_titulo="Exercício 12")

@app.route('/res12', methods=['GET','POST'])
def res12():
  global resp
  resp=""
  
  n1 = int(request.form['num1'])
  n2 = int(request.form['num2'])
  
  if n1 < n2:
    maior = n2
  elif n1 > n2:
    maior = n1
  elif n1 == n2:
    resp = "Os números são iguais."
    return redirect('/resposta')
    
  resp = "O maior número digitado foi: " + str(maior) + ". Somando 100 teremos: " + str(maior + 100)
    
  return redirect('/resposta')

@app.route('/ex13')
def ex13():
  return render_template("ex13.html", txt_titulo="Exercício 13")

@app.route('/res13', methods=['GET','POST'])
def res13():
  global resp
  resp=""

  n1 = int(request.form['num1'])
  n2 = int(request.form['num2'])

  if n1 > n2:
    maior = n1
  elif n1 < n2:
    maior = n2
  elif n1 == n2:
    resp = "Números iguais"
    return redirect('/resposta')
    
  resp = "O maior número digitado foi: " + str(maior)

  return redirect('/resposta')

@app.route('/ex14')
def ex14():
  return render_template("ex14.html", txt_titulo="Exercício 14")

@app.route('/res14', methods=['GET','POST'])
def res14():
  global resp
  resp=""

  n1 = int(request.form['num1'])
  n2 = int(request.form['num2'])

  if n1 < n2:
    maior = n2
    menor = n1
  elif n1 > n2:
    maior = n1
    menor = n2
  elif n1 == n2:
    resp = "Os números são iguais."
    return redirect('/resposta')

  resp = "A diferença entre: " + str(maior) + " e " + str(menor) + " é: " + str(maior-menor)
  return redirect('/resposta')

@app.route('/ex15')
def ex15():
  return render_template("ex15.html", txt_titulo="Exercício 15")

@app.route('/res15', methods=['GET','POST'])
def res15():
  global resp
  resp=""

  dias = int(request.form['dias'])
  diaria = 50.00
  
  if dias < 15:
    taxa = dias * 1.50
    vlrdiaria = dias * diaria
    preco = vlrdiaria + taxa
  elif dias == 15:
    taxa = dias * 1.00
    vlrdiaria = dias * diaria
    preco = vlrdiaria + taxa
  elif dias > 15:
    taxa = dias * 0.5
    vlrdiaria = dias * diaria
    preco = vlrdiaria + taxa

  resp = str(dias) + " diárias com a taxa de serviços ficou em: " + str(preco) + "R$."
    
  return redirect('/resposta')

@app.route('/ex16')
def ex16():
  return render_template("ex16.html", txt_titulo="Exercício 16")

@app.route('/res16', methods=['GET','POST'])
def res16():
  global resp
  resp=""

  saldo = int(request.form['cred'])

  if saldo >=0 and saldo <=200:
    resp = "Devido ao seu saldo médio de " + str(saldo) + "R$ não conseguimos aprovar nenhum crédito."
    return redirect('/resposta')
  elif saldo >=201 and saldo <=400:
    especial = saldo * 0.2
  elif saldo >=401 and saldo <=600:
    especial = saldo * 0.3
  elif saldo >=601:
    especial = saldo * 0.4
  resp = "Com seu saldo médio de " + str(saldo) + "R$ você terá: " + str(especial) + "R$ de crédito especial!"

  return redirect('/resposta')

@app.route('/ex17')
def ex17():
  return render_template("ex17.html", txt_titulo="Exercício 17")


@app.route('/res17', methods=['GET','POST'])
def res17():
  global resp
  resp=""

  cod = int(request.form['cod'])
  n1 = float(request.form['no1'])
  n2 = float(request.form['no2'])
  n3 = float(request.form['no3'])
  ne = float(request.form['no4'])
  media = (n1 + n2 * 2 + n3 * 3 + ne) / 7
  aprov = "a"

  if media >= 9.0:
    con = "A"
    aprov = "APROVADO"
  elif media >= 7.5 and media < 9.0:
    con = "B"
    aprov = "APROVADO"
  elif media >= 6.0 and media < 7.5:
    con = "C"
    aprov = "APROVADO"
  elif media >= 4.0 and media < 6.0:
    con = "D"
    aprov = "REPROVADO"
  elif media < 4.0:
    con = "E"
    aprov = "REPROVADO"
    
  resp = "Código do aluno: " + str(cod) + "<br>" + "Primeira nota: " + str(n1) + "<br>" + "Segunda nota: " + str(n2) + "<br>" + "Terceira nota: " + str(n3) + "<br>" + "Nota dos exercícios: " + str(ne) + "<br>" + "Média: {:.4}".format(str(media)) + "<br>" + "Conceito: " + con + "<br>" + "<br>" + aprov
  
  return redirect('/resposta')

@app.route('/ex18')
def ex18():
  return render_template("ex18.html", txt_titulo="Exercício 18")

@app.route('/res18', methods=['GET','POST'])
def res18():
  global resp
  resp=""

  cod = int(request.form['cod'])
  sexo = request.form['sex'].capitalize()
  anos = int(request.form['anos'])
  sal = float(request.form['sal'])

  if sexo == "Masculino" and anos > 15:
    bonus = sal * 0.2
  elif sexo == "Feminino" and anos > 10:
    bonus = sal * 0.25
  else:
    bonus =  100
  
  resp = "Código do funcionário: " + str(cod) + "<br>" + "Sexo: " + sexo + "<br>" + "Anos na empresa: "  + str(anos) + "<br>" + "Salário: " + str(sal) + "<br>" + "Bonûs: " + str(bonus)

  return redirect('/resposta')

@app.route('/ex19')
def ex19():
  return render_template("ex19.html", txt_titulo="Exercício 19")

@app.route('/res19', methods=['GET','POST'])
def res19():
  global resp
  resp=""

  user = int(request.form['ele'])
  ele = 2
  resp = []
  resp.append("1 elefante incomoda muita gente" + "<br>")
  while ele <= user:
    ele2 = 0
    while ele2 < ele:
      ele2 += 1
    if ele%2==0:
      resp.append(str(ele) + " elefantes " + " incomodam " * ele2 + " muito mais." + "<br>")
      resp.append(str(ele+1) + " elefantes incomodam muita gente."+ "<br>")
      ele = ele + 1
    elif ele%2!=0:
      resp.append(str(ele) + " elefantes " + " incomodam muito mais." + "<br>")
      resp.append(str(ele+1) + " elefantes incomodam muita gente."+ "<br>")
      ele = ele + 1
  
    ele = ele + 1

  return redirect('/resposta')

@app.route('/ex20')
def ex20():
  return render_template("ex20.html", txt_titulo="Exercício 20")

@app.route('/res20', methods=['GET','POST'])
def res20():
  global resp
  resp=""
  
  user = int(request.form['conta'])
  conta = 2
  conta2 = 1
  resp = []
  txt = "Mariana conta:"
  resp.append("Mariana conta 1" + "<br>")
  resp.append("Mariana conta 1: é 1, é Ana" + "<br>")
  resp.append("Viva a Mariana, viva a mariana" + "<br>")
  while conta <= user:
    resp.append("Mariana conta " + str(conta) + "<br>")
    while conta2 <= conta:
      txt +=" é " + str(conta2)     
      conta2 += 1
    resp.append(txt+" é Ana <br>")
    resp.append("Viva a Mariana, viva a mariana" + "<br>")
    
    conta += 1

  return redirect("/resposta")
  
app.run()
