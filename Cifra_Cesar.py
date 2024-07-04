from art import logo

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char.isalpha():  # Verifica se o caractere é uma letra do alfabeto
            position = alphabet.index(char)
            new_position = (position + shift_amount) % 26  # Usa % 26 para ajustar a nova posição
            end_text += alphabet[new_position]
        else:
            end_text += char  # Mantém caracteres que não estão no alfabeto
    print(f"Here's the {cipher_direction}d result: {end_text}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26  # Garante que o shift seja dentro de 0-25

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart != "yes":
        should_end = True
        print("Goodbye")
