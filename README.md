# Promoter Sequence Classifier

Este projeto é um classificador de sequências de promotores de genes baseado em aprendizado de máquina, especificamente usando redes neurais (MLP - Perceptron Multicamadas). O objetivo é identificar e classificar sequências de DNA de promotores, que são regiões específicas do DNA onde a transcrição de genes é iniciada.

## O que é um Promoter Sequence Classifier?

Um **Promoter Sequence Classifier** (classificador de sequências de promotores) é um modelo de aprendizado de máquina treinado para identificar regiões de promotores em sequências de DNA. Promotores são segmentos de DNA localizados antes de um gene e são fundamentais no processo de transcrição genética, pois eles "dizem" à célula onde iniciar a cópia do DNA em RNA.

Identificar promotores é importante em bioinformática e biologia molecular, pois ajuda na compreensão dos mecanismos reguladores dos genes e no estudo de como genes específicos são ativados ou desativados em diferentes condições. Com o avanço do aprendizado de máquina, modelos como este podem auxiliar na identificação automática de promotores, economizando tempo e aumentando a precisão em estudos genéticos.

## Sobre o Dataset

O dataset usado neste projeto vem do repositório de aprendizado de máquina da [UCI](https://archive.ics.uci.edu/dataset/67/molecular+biology+promoter+gene+sequences), na seção de Biologia Molecular. Este conjunto de dados foi projetado para a classificação de sequências de DNA de promotores em duas classes (`+` e `-`), onde:

- **`+`** significa que a sequência de DNA é um promotor.
- **`-`** significa que a sequência de DNA não é um promotor.

### Estrutura do Dataset

O dataset consiste em várias sequências de DNA, onde cada sequência está associada a uma classe (`+` ou `-`). A estrutura de cada linha no arquivo de dados é:

```
Class,ID,Sequence
+,S10,	tactagcaatacgcttgcgttcggtggttaagtatgtataatgcgcgggcttgtcgt
-,867,	atatgaacgttgagactgccgctgagttatcagctgtgaacgacattctggcgtcta
...
```

- **Class**: Rótulo que indica se a sequência é um promotor (`+`) ou não (`-`).
- **ID**: Um identificador opcional para cada sequência (não é utilizado diretamente no treinamento).
- **Sequence**: A sequência de DNA em si, composta por nucleotídeos (`A`, `T`, `C`, `G`).

### Uso do Dataset

Este dataset é utilizado para treinar e avaliar modelos de classificação que possam distinguir entre sequências de promotores e não-promotores. O modelo MLP (Perceptron Multicamadas) é treinado para aprender padrões nas sequências que indicam a presença ou ausência de promotores, com base nos nucleotídeos.
