{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled1.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyO2fqzH8e8079vI6l/2IBZk",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "accelerator": "TPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/HarvinderSinghDiwan/python/blob/master/NameInBox.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xfLKr-wRdZ7x",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "c1b7a673-0f38-4ac7-a7fd-bdbe2ee73d6e"
      },
      "source": [
        "a=input(\"Please enter how many time do u want to print first name and last name : \")"
      ],
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Please enter how many time do u want to print first name and last name : 5\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ex288Y-9drEi",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 84
        },
        "outputId": "3d54c6c7-8f9e-4aac-c1b8-4924383f43e7"
      },
      "source": [
        "fname=input(\"Please enter your first name \\n\")\n",
        "lname=input(\"Please enter your last name \\n\")"
      ],
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Please enter your first name \n",
            "Harvinder\n",
            "Please enter your last name \n",
            "Singh\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "f4_atw7WeE1H",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 202
        },
        "outputId": "356b3417-a158-4fe4-bc56-5e8d3c341261"
      },
      "source": [
        "x=len(fname)+len(lname)\n",
        "for i in range(x+5):\n",
        "  print(\"*\",end=\"\")\n",
        "for j in range(int(a)):\n",
        "    print(\"\\n*\",fname,lname,\"*\",end=\"\\n\")\n",
        "for i in range(x+5):\n",
        "  print(\"*\",end=\"\")"
      ],
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "*******************\n",
            "* Harvinder Singh *\n",
            "\n",
            "* Harvinder Singh *\n",
            "\n",
            "* Harvinder Singh *\n",
            "\n",
            "* Harvinder Singh *\n",
            "\n",
            "* Harvinder Singh *\n",
            "*******************"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9wJZMFxAeXHV",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "  "
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}