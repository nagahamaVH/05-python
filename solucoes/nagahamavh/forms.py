class forms:
    sep = ","

    def __init__(self, path):
        self.path = path
        self.form = open(self.path, "w")
        self.form.write("id_usuario,nome,idade,sexo\n")
        self.form.close()

    def insert_registry(self):
        should_insert = True

        while should_insert:
            user_id = input("Nome do usuário: ")
            name = input("Nome: ")
            age = input("Idade: ")
            sex = input("Sexo: ")

            new_registry = user_id + self.sep + name + self.sep + age + self.sep + sex + "\n"

            self.form = open(self.path, "a")
            self.form.write(new_registry)
            self.form.close()
            print("Registro concluído")
            should_insert = input("Continuar inserindo? (1 - sim, 0 - não): ")
            should_insert = True if should_insert == "1" else False

    def print(self):
        form = open(self.path, "r")
        print(form.read())
        form.close()
