from random import randint

# instead of using an API, a database with 219 "Customers" was used.
# being selected randomly.

names = "Francisco Nunes", "Pedro Henrique Vieira", "João Felipe Ramos", "Vitória Nunes", "João Guilherme Freitas", \
        "Vinicius Santos", "Maria Sophia Cunha", "Lucas Gabriel Castro", "Alexandre Dias", "Maria Alice Mendes", \
        "Pedro Oliveira", "Rafael Barbosa", "Ana Carolina CamposAgatha Moraes", "Juan da Mata", \
        "Dr. Leonardo Almeida", "Isaac Dias", "Enzo Gabriel Gomes", "Sr. Joaquim da Mata", "Otávio Nunes", \
        "Gabrielly Costa", "Kaique Nogueira", "Enzo Porto", "Sra. Emanuella Nogueira", "ia Silveira", \
        "Vinicius Santos", "Maria Sophia Cunha", "Lucas Gabriel Castro", "Alexandre Dias", "Maria Alice Mendes", \
        "Pedro Oliveira", "Rafael Barbosa", "Ana Carolina Campos", "Agatha Moraes", "Juan da Mata", \
        "Dr. Leonardo Almeida", "Isaac Dias", "Enzo Gabriel Gomes", "Sr. Joaquim da Mata", "Otávio Nunes", \
        "Gabrielly Costa", "Kaique Nogueira", "Enzo Porto", "Sra. Emanuella Nogueira", "Sr. João Felipe Correia", \
        "Sophie Sales", "Maitê Cardoso", "Sra. Maria Eduarda Aragão", "Laís Nunes", "Ian Fogaça", "Lorenzo Nunes", \
        "Ana Vitória Farias", "Vinicius Nascimento", "Dr. Enrico Almeida", "Luiz Miguel Costela", "Ana Vieira", \
        "Renan Nogueira", "Amanda Duarte", "Davi Lucca da Paz", "Thomas Nogueira", "Vitor Gabriel da Costa", \
        "Arthur Barbosa", "Marcos Vinicius Jesus", "Lara Cardoso", "Rafaela Campos", "Marcos Vinicius Costa", \
        "Maria Clara da Cruz", "Yasmin Cardoso", "Lívia Moraes", "Ana Beatriz Novaes", "Sr. Raul Pereira", \
        "Emanuelly Viana", "Joaquim Melo", "Clarice Pereira", "Rodrigo Correia", "Srta. Mariana Duarte", \
        "Dr. Renan Dias", "Bruno Teixeira", "Stephany Carvalho", "Beatriz Ferreira", "Alexia Nascimento", \
        "Sr. Luigi Fernandes", "João Felipe Mendes", "Sophia das Neves", "Lorena da Cunha", "Emilly Correia", \
        "Davi da Cunha", "Gustavo da Rocha", "André Freitas", "Guilherme Farias", "Brenda Gomes", "Alícia Almeida", \
        "Dr. Thales Fernandes", "Calebe Alves", "João Gabriel Silveira", "Daniela da Mata", "Dr. Renan da Conceição", \
        "Nicole da Rosa", "Srta. Lara Caldeira", "Ana Julia Cunha", "Júlia Melo", "Mariana Freitas", \
        "Dra. Marcela da Conceição", "Ana Luiza Cardoso", "Dr. Fernando da Paz", "Gabrielly Rocha", \
        "Dr. Paulo Farias", "Srta. Luna Nunes", "Ryan Pinto", "Dr. Breno Gomes", "Daniela Costa", "Noah Gonçalves", \
        "Lavínia Nascimento", "Maria Sophia Cavalcanti", "Mariana Azevedo", "Alícia Cardoso", "Emanuel Lopes", \
        "Catarina Ferreira", "Sr. Diego Moreira", "Kamilly Costa", "Júlia Viana", "Evelyn Porto", "Yasmin Melo", \
        "Pedro Lucas Viana", "Isadora Cardoso", "Luiza Ferreira", "Larissa Cavalcanti", "Sr. Erick Barbosa", \
        "Ana Sophia Aragão", "Vitor Gabriel Rodrigues", "Henrique Oliveira", "Levi Costela", "João Barbosa", \
        "Larissa Gonçalves", "Isis Pinto", "Srta. Bruna Novaes", "Gabriela da Mata", "Henrique Novaes", \
        "Dra. Ana Lívia da Paz", "Juan Araújo", "Gustavo da Rosa", "Dr. Yuri Almeida", "Pietra Sales", \
        "Erick Jesus", "Alice Rocha", "Mirella Ferreira", "Benício Aragão", "Raul da Luz", "Marcelo Pires", \
        "Fernanda Costela", "Sra. Manuela Vieira", "Eduarda da Mata", "Clarice Costela", "Mirella Alves", \
        "Clara Pinto", "Cauã Pires", "Eduarda Duarte", "Maria Vitória Dias", "Sra. Mariana Campos", \
        "Sra. Alana Vieira", "Erick Rezende", "Isabella Cavalcanti", "Arthur da Conceição", "Marcelo Cavalcanti", \
        "Sabrina Vieira", "Alice Nascimento", "Dr. Isaac Correia", "Fernanda Santos", "Dr. Henrique Teixeira", \
        "Igor Monteiro", "Benjamin Monteiro", "Srta. Maria Vitória Nunes", "Enrico Barros", "Rafaela Araújo", \
        "Nathan Nogueira", "Helena Mendes", "Emanuel Nascimento", "Igor Mendes", "Evelyn Rocha", "Bárbara da Mota", \
        "Benjamin Dias", "Dr. Davi Luiz Sales", "Miguel Rodrigues", "Ana Vitória Moraes", "Bruno Duarte", \
        "Emilly Dias", "Sr. Thomas Freitas", "Joana Alves", "Sr. João Felipe Nogueira", "Júlia Jesus", \
        "Heloísa Vieira", "Daniela Ferreira", "Daniela Moura", "João Gabriel Porto", "Calebe Viana", \
        "Dra. Kamilly Monteiro", "Letícia Cunha", "Nicole Sales", "Bruna Nogueira", "Esther Novaes", \
        "Raul Nogueira", "João Miguel Ribeiro", "Luiz Henrique Nunes", "Stella da Cruz", "Vinicius Nascimento", \
        "João Pedro da Paz", "Sr. Nathan Mendes", "Maria Alice Fernandes", "Sarah Carvalho", "Alexia Duarte", \
        "Sra. Ana Beatriz Barbosa", "Bárbara Pires", "Marcos Vinicius Cunha", "Matheus Campos", \
        "Sr. Vinicius Martins", "Ana Vitória Almeida", "Gabriela Pinto", "Sr. João Felipe Dias", \
        "Mariana Moraes", "Alexia Silveiraprint"


def name():
    return names[randint(0, 218)]
