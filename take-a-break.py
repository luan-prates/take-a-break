import time
import webbrowser

"""Módulo principal."""

def main():
    """Função principal da aplicação."""
    total_breaks = 3
    break_cont = 0

    print("Esse programa iniciou em: " + time.ctime())
    while (break_cont < total_breaks):
        time.sleep(108000)
        webbrowser.open(
            "https://indicadores.integrasus.saude.ce.gov.br/indicadores/indicadores-coronavirus/coronavirus-ceara")
        break_cont = break_cont + 1

if __name__ == "__main__":
    main()
