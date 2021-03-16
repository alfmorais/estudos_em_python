{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled74.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyP56Xw3cL+810apW53M9Ahu",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/alfmorais/estudos_em_python/blob/main/estudos_em_python/curso_dev_aprender/mod_shutil.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2BtAywVnU8Xp"
      },
      "source": [
        "# Movimentando e Copiando Arquivos e Diretórios com Shutil\r\n",
        "\r\n",
        "import shutil\r\n",
        "import os\r\n",
        "\r\n",
        "# copia e movimenta arquivo de diretório 'x' para outro diretório 'y'\r\n",
        "shutil.copy(src=os.getcwd() + os.sep + 'fotos' + 'foto1.jpg',\r\n",
        "            dst=os.getcwd() + os.sep + 'backup')\r\n",
        "\r\n",
        "# copiar um pasta inteira\r\n",
        "shutil.copytree(src=os.getcwd() + os.sep + 'fotos',\r\n",
        "                dst=os.getcwd() + os.sep + 'backup')\r\n",
        "\r\n",
        "# movimentar todos os arquivos de um diretório 'x' para outro diretório 'y'\r\n",
        "shutil.move(src=os.getcwd() + os.sep + 'fotos backup',\r\n",
        "            dst=os.getcwd() + os.sep + 'backup')\r\n",
        "\r\n",
        "# movimentando um arquivo\r\n",
        "shutil.move(src=os.getcwd() + os.sep + 'fotos backup' + os.sep + 'fotos.jpg',\r\n",
        "            dst=os.getcwd() + os.sep + 'backup')\r\n",
        "\r\n",
        "# apagando uma pasta e tudo que estiver dentro dela\r\n",
        "shutil.rmtree(os.getcwd() + os.sep + 'musicas')\r\n",
        "\r\n",
        "# compactar arquivos\r\n",
        "shutil.make_archive('backup_fotos', 'zip',\r\n",
        "                    os.getcwd() + os.sep + 'fotos')\r\n",
        "\r\n",
        "# compactando todos os arquivos do diretório\r\n",
        "shutil.make_archive('backup_fotos', 'zip',\r\n",
        "                    os.getcwd())\r\n",
        "\r\n",
        "# desconpactar arquivos\r\n",
        "shutil.unpack_archive('backup_vs_code.zip',\r\n",
        "                      os.getcwd() + os.sep + 'backup_vs_code')\r\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "YtSvy3IHcXG1"
      },
      "source": [
        "# Desafio\r\n",
        "\r\n",
        "## Crie 3 pastas diferentes no seu diretório atual (manualmente):\r\n",
        "1) Arquivos 2010\r\n",
        "\r\n",
        "2) Documentação \r\n",
        "\r\n",
        "3) Backup\r\n",
        "\r\n",
        "## Agora crie 3 arquivos fora destas pastas\r\n",
        "1) nomes.txt\r\n",
        "\r\n",
        "2) inscrições.pdf\r\n",
        "\r\n",
        "3) relatorios.xlsx\r\n",
        "\r\n",
        "## Instruções:\r\n",
        "1) Copie o arquivo nomes.txt para a pasta 'Arquivos 2010'\r\n",
        "\r\n",
        "2) Mova o arquivo incrições.pdf para a pasta 'Documentação'\r\n",
        "\r\n",
        "3) Faça uma cópia de pasta 'Arquivos 2010' e tudo que estiver contido nela para a pasta uma nova pasta chamada 'Backup Arquivos 2010'\r\n",
        "\r\n",
        "4) Compacte todo o contéudo da pasta 'Documentação' no formato zip\r\n",
        "\r\n",
        "5) Mova o arquivo compactado para dentro da pasta 'Backup'\r\n",
        "\r\n",
        "6) Exclua o diretório 'Arquivos 2010' e  'Documentação' e seus contéudos\r\n",
        "\r\n",
        "7) Compacte o diretório inteiro, para um arquivo chamado 'Backup Arquivos Python.zip'\r\n",
        "\r\n",
        "8) Antes de ir para o próximo vídeo e ver a solução poste a solução que você criou no link que vou deixar abaixo deste vídeo.\r\n",
        "\r\n"
      ]
    }
  ]
}