"""
Obtiene tokens desde el archivo sitedata.json utilizando
el patrón de diseño Singleton.
"""

import json
import sys


class TokenManager:
    """
    Clase Singleton encargada de administrar el acceso
    a los datos del archivo JSON.
    """

    _instance = None
    VERSION = "1.1"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TokenManager, cls).__new__(cls)
        return cls._instance

    def get_token(self, key="token1"):
        """
        Obtiene un token desde sitedata.json.
        """

        try:
            with open("sitedata.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            if key in data:
                return data[key]

            return f"Error: la clave '{key}' no existe."

        except FileNotFoundError:
            return "Error: archivo sitedata.json no encontrado."

        except json.JSONDecodeError:
            return "Error: formato JSON inválido."

        except PermissionError:
            return "Error: permisos insuficientes para acceder al archivo."

        except OSError as error:
            return f"Error de sistema controlado: {error}"


def validate_arguments():
    """
    Valida los parámetros recibidos por línea de comandos.
    """

    args = sys.argv[1:]

    if len(args) > 1:
        return None, "Error: cantidad de argumentos inválida."

    if len(args) == 1:
        if args[0] == "-v":
            print(f"Versión {TokenManager.VERSION}")
            sys.exit(0)

        return args[0], None

    return "token1", None


def main():
    """
    Punto de entrada principal.
    """

    key, error = validate_arguments()

    if error:
        print(error)
        sys.exit(1)

    manager = TokenManager()
    print(manager.get_token(key))


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error controlado: {error}")
        sys.exit(1)