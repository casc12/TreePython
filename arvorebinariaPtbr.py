{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN788ZA4kA5AXw5zjK0vgTl",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/casc12/TreePython/blob/code/arvorebinariaPtbr.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#1  Definição da arvaroe Binária\n",
        "\n",
        "# definição do No ou NODE\n",
        "class Galho:\n",
        "  def __init__(self, data):\n",
        "     self.left = None\n",
        "     self.right = None\n",
        "     self.data = data\n",
        "\n",
        "\n",
        "  def insert(self, data):\n",
        "     if self.data is None:\n",
        "\t        self.data = data\n",
        "     else:\n",
        "         if data < self.data:\n",
        "          if self.left is None:\n",
        "            self.left = Galho(data)\n",
        "          else:\n",
        "            self.left.insert(data)\n",
        "         elif data > self.data:\n",
        "             if self.right is None:\n",
        "              self.right = Galho(data)\n",
        "             else:\n",
        "              self.right.insert(data)\n",
        "def inOrderPrint(r):\n",
        "    if r is None:\n",
        "        return\n",
        "    else:\n",
        "        inOrderPrint(r.left)\n",
        "        print(r.data, end=' ')\n",
        "        inOrderPrint(r.right)\n",
        "\n",
        "\n",
        "def preOrderPrint(r):\n",
        "       if r is None:\n",
        "           return\n",
        "       else:\n",
        "           print(r.data, end=' ')\n",
        "           preOrderPrint(r.left)\n",
        "           preOrderPrint(r.right)\n",
        "\n",
        "def postOrderPrint(r):\n",
        "       if r is None:\n",
        "           return\n",
        "       else:\n",
        "           print(r.data, end=' ')\n",
        "           postOrderPrint(r.right)\n",
        "           postOrderPrint(r.left)\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    print(\"Bem vindo a arvore\")\n",
        "    root = Galho('g')\n",
        "    root.insert('c')\n",
        "    root.insert('b')\n",
        "    root.insert('a')\n",
        "    root.insert('e')\n",
        "    root.insert('d')\n",
        "    root.insert('f')\n",
        "    root.insert('i')\n",
        "    root.insert('h')\n",
        "    root.insert('j')\n",
        "    root.insert('k')\n",
        "\n",
        "# 4 . Imprimindo os galhos em ordem\n",
        "print(\"\\nimprimindo em ordem\")\n",
        "inOrderPrint(root)\n",
        "print(\"\\nimprimindo em pre-ordem\")\n",
        "preOrderPrint(root)\n",
        "print(\"\\nimprimindo em post-ordem\")\n",
        "postOrderPrint(root)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XPYrK6v2JCQa",
        "outputId": "735e3454-ff3a-4755-c385-081359043a30"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Bem vindo a arvore\n",
            "\n",
            "imprimindo em ordem\n",
            "a b c d e f g h i j k \n",
            "imprimindo em pre-ordem\n",
            "g c b a e d f i h j k \n",
            "imprimindo em post-ordem\n",
            "g i j k h c e f d b a "
          ]
        }
      ]
    }
  ]
}