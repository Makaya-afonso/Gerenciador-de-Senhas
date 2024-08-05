from crypto_manager import CryptoManager
from db_manager import DBManager

def menu():
    print("1. Adicionar senha")
    print("2. Visualizar senhas")
    print("3. Editar senha")
    print("4. Excluir senha")
    print("5. Sair")

def main():
    crypto_manager = CryptoManager()
    db_manager = DBManager()
    
    while True:
        menu()
        choice = input("Escolha uma opção: ")

        if choice == '1':
            site = input("Site: ")
            username = input("Nome de usuário: ")
            password = input("Senha: ")
            encrypted_password = crypto_manager.encrypt(password)
            db_manager.add_password(site, username, encrypted_password)
            print("Senha adicionada com sucesso.")
        
        elif choice == '2':
            passwords = db_manager.get_passwords()
            for pwd in passwords:
                decrypted_password = crypto_manager.decrypt(pwd[3])
                print(f"ID: {pwd[0]}, Site: {pwd[1]}, Nome de usuário: {pwd[2]}, Senha: {decrypted_password}")

        elif choice == '3':
            id = input("ID da senha a ser editada: ")
            new_password = input("Nova senha: ")
            encrypted_password = crypto_manager.encrypt(new_password)
            db_manager.update_password(id, encrypted_password)
            print("Senha atualizada com sucesso.")
        
        elif choice == '4':
            id = input("ID da senha a ser excluída: ")
            db_manager.delete_password(id)
            print("Senha excluída com sucesso.")
        
        elif choice == '5':
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
