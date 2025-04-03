# Cifra de Vigenère - Aplicação Python

## 📝 Descrição

Esta aplicação implementa a Cifra de Vigenère, um método de criptografia por substituição polialfabética que utiliza uma série de diferentes cifras de César baseadas em letras de uma palavra-chave. Desenvolvida com Python e interface gráfica usando Tkinter, a aplicação permite criptografar e descriptografar mensagens de texto.

##  Características

- Interface gráfica simples e intuitiva
- Criptografia de mensagens usando o algoritmo de Vigenère
- Descriptografia de mensagens cifradas
- Suporte a caracteres alfabéticos (preserva maiúsculas e minúsculas)
- Preservação de caracteres não alfabéticos (números, símbolos, espaços)

##  Como Usar

1. Execute o script Python:
   ```
   python vigenere_cipher.py
   ```

2. Selecione a ação desejada:
   - `criptografar`: Para transformar texto plano em texto cifrado
   - `descriptografar`: Para recuperar o texto original a partir do texto cifrado

3. Digite a mensagem que deseja processar

4. Forneça uma chave alfabética (apenas letras)

5. O resultado será exibido em uma caixa de diálogo

## 🧠 Como Funciona a Cifra de Vigenère

A Cifra de Vigenère funciona da seguinte forma:

1. Para **criptografar**:
   - Cada letra da mensagem original é deslocada de acordo com a letra correspondente da chave
   - O deslocamento é determinado pela posição da letra da chave no alfabeto (A=0, B=1, C=2, etc.)
   - A chave é repetida para cobrir todo o comprimento da mensagem

2. Para **descriptografar**:
   - O processo é inverso, subtraindo o valor do deslocamento

### Exemplo

```
Mensagem: HELLO
Chave: KEY
```

Processo de criptografia:
- H + K = R (H deslocado 10 posições)
- E + E = I (E deslocado 4 posições)
- L + Y = J (L deslocado 24 posições)
- L + K = V (L deslocado 10 posições)
- O + E = S (O deslocado 4 posições)

Resultado criptografado: RIJVS

##  Requisitos

- Python 3.x
- Tkinter (geralmente vem instalado com Python)

## ⚙️ Estrutura do Código

- `vigenere_criptografar()`: Função para criptografar texto usando o algoritmo de Vigenère
- `vigenere_descriptografar()`: Função para descriptografar texto cifrado
- `principal()`: Função principal que gerencia a interface do usuário e o fluxo do programa

##  Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## 👤 Autor

[jaupventur]

---

⭐ Se este projeto foi útil para você, considere dar uma estrela!
