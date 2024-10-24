def quiz_pokemon():
    print("Bem-vindo ao Quiz definitivo sobre Pokémon")
    g = int(input("Sobre qual geração será o quiz? \n 1 - Velha geração: 1° - 4° \n 2 - Nova geração: 5° - 9° "))
    score = 0
    if g == 1:
        perguntas_velha_ger = [
            {
                "pergunta_v": "1- Qual é o inicial de fogo da 2° geração?",
                "respostas_v": ["A) Chimchar", "B) Torchic", "C) Cyndaquil", "D) Charmander"],
                "resposta_certa_v": "C"
            },
            {
                "pergunta_v": "2- Qual dos três passaros lendários é do tipo gelo?",
                "respostas_v": ["A) Articuno", "B) Zapdos", "C) Moltreas", "D) Regice"],
                "resposta_certa_v": "A"
            },
            {
                "pergunta_v": "3- Qual é o nome da 3° região em pokemon?",
                "respostas_v": ["A) Kanto", "B) Hoemn", "C) Johto", "D) Sinnoh"],
                "resposta_certa_v": "B"
            },
            {
                "pergunta_v": "4- Qual Pokémon é a última evolução de Ralts?",
                "respostas_v": ["A) Aggron", "B) Exploud", "C) Gardevoir", "D) Slaking"],
                "resposta_certa_v": "C"
            },
            {
                "pergunta_v": "5- Qual tipo de Pokémon é eficaz contra o tipo Água?",
                "respostas_v": ["A) Metal", "B) Grama", "C) Fogo", "D) Fada"],
                "resposta_certa_v": "B"
            },
            {
                "pergunta_v": "6- Qual é a parceira do Ash na 1° região?",
                "respostas_v": ["A) May", "B) Max", "C) Misty", "D) Dawn"],
                "resposta_certa_v": "C"
            },
            {
                "pergunta_v": "7- Qual é o pokemon alienígena da 3° geração?",
                "respostas_v": ["A) Registeel", "B) Latios", "C) Groudon", "D) Deoxys"],
                "resposta_certa_v": "D"
            },
            {
                "pergunta_v": "8- De qual geração o pokemon inicial tipo grama Turtwig é?",
                "respostas_v": ["A) Kanto", "B) Hoemn", "C) Johto", "D) Sinnoh"],
                "resposta_certa_v": "D"
            },
            {
                "pergunta_v": "9- Em qual pais as primeiras 4 regiões foram inspiradas?",
                "respostas_v": ["A) Japão", "B) Coreia", "C) Russia", "D) Alemanha"],
                "resposta_certa_v": "A"
            },
            {
                "pergunta_v": "10- Quantos pokemons Ash capturou nas 4 primeiras regiões?",
                "respostas_v": ["A) 33", "B) 45", "C) 52", "D) 84"],
                "resposta_certa_v": "A"
            },
            ]

        for q in perguntas_velha_ger:
            print("\n" + q["pergunta_v"])
            for option in q["respostas_v"]:
                print(option)
            resposta_certa_v = input("Sua resposta (A, B, C ou D): ").strip().upper()
                
            if resposta_certa_v == q["resposta_certa_v"]:
                print("Correto!")
                score += 1
            else:
                print(f"Incorreto! A resposta correta é {q['resposta_certa_v']}.")

        print(f"\nSeu resultado final: {score}/{len(perguntas_velha_ger)}")

    elif g == 2:
        perguntas_nova_ger = [
            {
                "pergunta": "Qual é o Pokémon inicial do tipo Água da 5ª geração?",
                "respostas": ["A) Snivy", "B) Tepig", "C) Oshawott", "D) Chespin"],
                "resposta_certa": "C"
            },
            {
                "pergunta": "Qual Pokémon é conhecido como o Pokémon Lendário da terra e agricultura da 5ª geração?",
                "respostas": ["A) Landorus", "B) Thundurus", "C) Zekrom", "D) Genesect"],
                "resposta_certa": "A"
            },
            {
                "pergunta": "Qual é a evolução final de Sprigatito na 9ª geração?",
                "respostas": ["A) Meowscarada", "B) Skeledirge", "C) Floragato", "D) Cacturne"],
                "resposta_certa": "A"
            },
            {
                "pergunta": "Qual Pokémon da 6ª geração é conhecido por sua habilidade Proteção contra Fogo?",
                "respostas": ["A) Chespin", "B) Fennekin", "C) Braixen", "D) Delphox"],
                "resposta_certa": "D"
            },
            {
                "pergunta": "Qual tipo de Pokémon é eficaz contra o tipo psíquico?",
                "respostas": ["A) Lutador", "B) Gelo", "C) Terra", "D) Sombrio"],
                "resposta_certa": "D"
            },
            {
                "pergunta": "Qual é a forma regional de Mr. Mime introduzida na 8ª geração?",
                "respostas": ["A) Galariam", "B) Alolan", "C) Hisuian", "D) Kantonian"],
                "resposta_certa": "A"
            },
            {
                "pergunta": "Qual Pokémon é a evolução final de Froakie na 6ª geração?",
                "respostas": ["A) Swampert", "B) Greninja", "C) Zapdos", "D) Frogadier"],
                "resposta_certa": "B"
            },
            {
                "pergunta": "Qual é o Pokémon inicial do tipo Grama da 8ª geração?",
                "respostas": ["A) Sobble", "B) Scorbunny", "C) Grookey", "D) Rillaboom"],
                "resposta_certa": "C"
            },
            {
                "pergunta": "Qual Pokémon da 9ª geração é conhecido por ser um Pokémon Fantasma tipo Fogo?",
                "respostas": ["A) Spirgitito", "B) Grafaiai", "C) Tinkaton", "D) Ceruledge"],
                "resposta_certa": "D"
            },
            {
                "pergunta": "Qual é o rival de ash na 7° geração?",
                "respostas": ["A) Trip", "B) Paul", "C) Morrison", "D) Gladion"],
                "resposta_certa": "D"
            }
            ]

        for q in perguntas_nova_ger:
            print("\n" + q["pergunta"])
            for option in q["respostas"]:
                print(option)
            resposta_certa = input("Sua resposta (A, B, C ou D): ").strip().upper()
                
            if resposta_certa == q["resposta_certa"]:
                print("Correto!")
                score += 1
            else:
                print(f"Incorreto! A resposta correta é {q['resposta_certa']}.")

        print(f"\nSeu resultado final: {score}/{len(perguntas_nova_ger)}")

    else:
        print("opção inválida, tente novamente.")
quiz_pokemon()
