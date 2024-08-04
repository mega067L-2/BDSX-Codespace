import os
import subprocess

# Función para instalar paquetes necesarios
def install_packages():
    try:
        # Instalar Node.js
        print("Instalando Node.js...")
        subprocess.check_call(["sudo", "apt-get", "install", "-y", "nodejs"])
        
        # Instalar npm (Node Package Manager)
        print("Instalando npm...")
        subprocess.check_call(["sudo", "apt-get", "install", "-y", "npm"])

        # Instalar BDSX
        print("Clonando BDSX desde GitHub...")
        subprocess.check_call(["git", "clone", "https://github.com/ArthasZ/bdsx.git"])
        
        # Ir al directorio de BDSX
        os.chdir("bdsx")

        # Instalar dependencias de BDSX
        print("Instalando dependencias de BDSX...")
        subprocess.check_call(["npm", "install"])

        print("BDSX instalado correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error durante la instalación: {e}")

if __name__ == "__main__":
    install_packages()
