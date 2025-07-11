def identificar_animal():
    try:
        # Entrada de dados com tratamento
        palavra_1 = input().strip().lower()
        palavra_2 = input().strip().lower()
        palavra_3 = input().strip().lower()

        # Estrutura de dados para mapear as combinações
        classificacao = {
            'vertebrado': {
                'ave': {
                    'carnivoro': 'aguia',
                    'onivoro': 'pomba'
                },
                'mamifero': {
                    'onivoro': 'homem',
                    'herbivoro': 'vaca'
                }
            },
            'invertebrado': {
                'inseto': {
                    'hematofago': 'pulga',
                    'herbivoro': 'lagarta'
                },
                'anelideo': {
                    'hematofago': 'sanguessuga',
                    'onivoro': 'minhoca'
                }
            }
        }

        # Busca no dicionário com tratamento de erro
        animal = classificacao.get(palavra_1, {}).get(palavra_2, {}).get(palavra_3)
        if animal:
            return animal
        else:
            return "Animal não encontrado ou combinação inválida."

    except Exception as e:
        return f"Erro: {e}"


# Função principal
def main():
    resultado = identificar_animal()
    print(resultado)

if __name__ == "__main__":
    main()
