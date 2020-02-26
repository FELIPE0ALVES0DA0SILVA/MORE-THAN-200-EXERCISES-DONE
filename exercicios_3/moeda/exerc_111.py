# Within of the package  utilidadescev that we create in the challenge 111,
# we have a module called data, Create a function called leiadinheiro() that be able to work like a function input(),
# but with a validation of data to accept just values that be monetaries.


from utilidades import money, dados


numero = dados.leiadinheiro("Digite o valor em reais a ser calculado: R$ ")
mais = int(input("Digite o aumento que o salário receberá: "))
menos = int(input("Digite o desconto que o salário receberá: "))
print(money.resumo(numero, mais, menos))
