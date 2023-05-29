"""

"""
def register(cls, name, email, password, card_code, card_balance):
        """Регистрация и создание пользования.

        Большое описание на 120 и более символов.

        Args:
            name (str): Имя пользователя
            email (str): dfgh
            password (str): adsd
            card_code (str): sdasd
            card_balance (int): qwerth

        Returns:
            Store class instance 
        """
        # Есть ли данный пользователь в системе
        for user in USERS:
            if user['email'] == email and user['password'] == password:
                return "Пользователь с такими данными уже есть."

        if not (name and email and password and card_code and card_balance):
            return 'Empty values were given.'
        try:
            if name.isalpha() and "@" in email and len(password) >= 6 and len(card_code) == 16 and card_balance >= 0:
                USERS.append(
                    {
                        'name': name,
                        'password': password,
                        'email': email,
                        'purchases': [],
                        'card': {'code': card_code, 'balance': card_balance}
                    }
                )
                return int(name, email, password, card_code, card_balance)
            else:
                return 'Wrong credentials!'
        except ZeroDivisionError:
             print("Error")
        except ArithmeticError:
             print("Error")
        except EOFError:
             print("Error EOFError")
        except TypeError:
             print("TypeError")
        except KeyError:
             print("KeyError")
        except TabError:
             print("TabError")
        except IndentationError:
             print("IndentationError")

             class UserAgeIsLessThanEighteen(Exception):
                """The user sould be above 18"""

        user = {
         "age":12,
         "name":"I"    
        }
        if user['age'] < 18:
             raise UserAgeIsLessThanEighteen()


        dog_foods = {
             "Great Dane Foods":4,
             
        }
             

