![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![VS Code](https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge)
![Tema](https://img.shields.io/badge/Foco-Pesquisa%20de%20Opini%C3%A3o-blue?style=for-the-badge)


# Pesquisa de Opinião 📋
Programa em Python desenvolvido para coletar o nome, a idade e a opinião de até 50 participantes, contabilizando e exibindo os resultados finais.

# Regras de Negócio e Classificação
O sistema executa um ciclo de 50 iterações solicitando os dados de cada participante (`nome`, `idade` e `opinião`), aplicando a seguinte lógica de validação e contagem:

* **Validação de Entrada:** Caso o usuário informe uma opção de opinião inválida (diferente de 1, 2 ou 3), o sistema exibe uma mensagem de erro e solicita um novo valor.
* **Excelente (Opção 1):** Incrementa o contador de respostas para o perfil excelente.
* **Bom (Opção 2):** Registra a resposta intermediária sem acumular em contadores específicos.
* **Ruim (Opção 3):** Incrementa o contador de respostas para o perfil ruim.
* **Resultado Final:** Ao término das 50 entrevistas, exibe a quantidade total de pessoas que responderam excelente e ruim.


# Como executar o programa no VSCode

### Pré-requisitos
Antes de começar, você precisará ter instalado em sua máquina:
* [VSCode](https://code.visualstudio.com/)
* [Git](https://git-scm.com)
* [Python 3.x](https://www.python.org/)

### 1) Visual Studio Code
Para abrir o terminal integrado do VS Code, acesse o menu superior em **Terminal** > **Novo Terminal** (ou use o atalho `Ctrl + '`).

### 2) Git
No terminal do VS Code, baixe o repositório e acesse a pasta do projeto:

```bash
# a) Clonar o repositório do github para o seu computador
git clone https://github.com/carlaraiol/pesquisa-opiniao.git

# b) Acessar a subpasta do projeto
cd pesquisa-opiniao
