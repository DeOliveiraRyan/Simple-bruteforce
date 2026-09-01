# Simple-bruteforce
A simple bruteforce script in python 

Foi feito apenas a lógica da programação de um ataque a força bruta de uma senha de 5 dígitos, sendo eles apenas números.

Foi importado *digits* da biblioteca **string** e *randint* da biblioteca **random**

A lógica do código é gerar uma senha numérica aleatória de 5 dígitos com o *randint* e guarda-la na variável senha. A partir dessa geração aleatória foi feito 5 loops **for** , cada um sendo um dígito da senha, e guardando esses 5 dígitos na variável *tentativa*.

Após os loops, foi feito **if** para cada indentação dos dígitos no **for** , comparando a tentativa com a senha, se o dígito for o mesmo da senha, o comando **break** vai encerrar o loop na indentação correspondente e guardar o dígito na variável. 

Apenas um simples projeto de um estudante de programação e cibersegurança. 
