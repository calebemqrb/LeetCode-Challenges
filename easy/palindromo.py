# Dado um inteiro x, retorne truese xfor umpalíndromo, e falsede outra forma .

 

# Exemplo 1:

# Entrada: x = 121
#  Saída: verdadeiro
#  Explicação: 121 é lido como 121 da esquerda para a direita e da direita para a esquerda.

# Exemplo 2:

# Entrada: x = -121
#  Saída: falso
#  Explicação: Da esquerda para a direita, lê-se -121. Da direita para a esquerda, torna-se 121-. Portanto, não é um palíndromo.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        str_x = str(x)[::-1]
        return x == int(str_x)