# Merge_PDF
Ferramenta em Python Desenvolvida para Juntar PDF's <br> 
# Como Utilizar 

 - Os PDF's Devem ter o mesmo **Nome** mas com uma referência de numero no **final** (Arquivo-1.pdf, Arquivo-2.pdf, Arquivo-3.pdf).
 - Nesse Caso o Nome-Arquivo-1.pdf, Nome-Arquivo-2.pdf, Nome-Arquivo-3.pdf gerarão o Nome-Arquivo.pdf
 - Configurações no Algoritmo: 
    - Linha [#5](https://github.com/williamanjo/Merge_PDF/blob/26da813c188b75b76c68d24b91ba369de6c61d2e/MergePDFbyList.py#L5) Referenciar o **Local** do **list.txt** Com a lista de Arquivos(Nome).
        - **list.txt**
          ```
          1º  Nome-Arquivo
          2º  Nome-Arquivo
          3º  ... 
          ```
    - Linha [#18](https://github.com/williamanjo/Merge_PDF/blob/26da813c188b75b76c68d24b91ba369de6c61d2e/MergePDFbyList.py#L18) Colocar a **Quantidade Maxima** de arquivos (Arquivo-1.pdf, Arquivo-2.pdf, Arquivo-3.pdf , [...]) que no Caso está (8).
    - Linha [#19](https://github.com/williamanjo/Merge_PDF/blob/26da813c188b75b76c68d24b91ba369de6c61d2e/MergePDFbyList.py#L19) Colocar o **Local** dos arquivos ("C:\\\Users\\\Nome-Maquina\\\Documents\\\Arquivos\\\\").
    - Linha [#24](https://github.com/williamanjo/Merge_PDF/blob/26da813c188b75b76c68d24b91ba369de6c61d2e/MergePDFbyList.py#L24) Colocar o **Local de Destino** dos Arquivos **Final** ("C:\\\Users\\\william.silva\\\Downloads\\\Res-merged\\\\").
