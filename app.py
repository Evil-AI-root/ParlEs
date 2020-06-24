from ParlEs import Preprocess


def main():
    sentence = input("Escribe una oracion cualquiera (mas de diez letras): ")
    if len(sentence) < 10:
        print("Tu Oracion fue muy corta asi que usare otra: ")
        sentence = r"Salve $oh patria %mil veces Oh Patria,@ gloria a ti, <> gloria a ti!"

    my_preprocess = Preprocess.Simple(sentence)
    my_preprocess.show_tree().pretty_print()
    print(my_preprocess.bag.counter)
    print(my_preprocess.bag.model(10))


if __name__ == '__main__':
    main()
