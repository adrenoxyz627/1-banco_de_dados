import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    username="root",
    passwd=""
)
cursor = banco.cursor()

def cria_hotel():
    cursor.execute("CREATE DATABASE hotel;")

def apaga_hotel():
    cursor.execute("DROP DATABASE hotel;")

def usa_hotel():
    cursor.execute("USE hotel;")

def cria_cliente():
    cursor.execute("CREATE TABLE cliente(rg VARCHAR(11) NOT NULL, nome VARCHAR(50) NOT NULL, fone VARCHAR(12) DEFAULT NULL, sexo VARCHAR(10) DEFAULT NULL, PRIMARY KEY (rg));")

def cria_ocupa():
    cursor.execute("CREATE TABLE ocupa(rg VARCHAR(11) NOT NULL, numero INT(3) NOT NULL, data_entrada DATE NOT NULL, data_saida DATE DEFAULT NULL, PRIMARY KEY (rg, numero, data_entrada), KEY fk_rg (rg), KEY fk_numero (numero), CONSTRAINT FOREIGN KEY (rg) REFERENCES cliente(rg) ON DELETE RESTRICT ON UPDATE CASCADE, CONSTRAINT FOREIGN KEY (numero) REFERENCES quarto(numero) ON DELETE RESTRICT ON UPDATE CASCADE);")

def cria_quarto(): #tipos de quartos:quarto solteiro, duplo solteiro, quarto casal, dormitórios
    # descrição :Standard, Executivo, Deluxe 
    cursor.execute("CREATE TABLE quarto(numero INT(3) NOT NULL, andar INT(1) NOT NULL, tipo VARCHAR(20) DEFAULT 'Solteiro', descrição VARCHAR(20) DEFAULT 'Standard', preço DECIMAL(5,2) NOT NULL, PRIMARY KEY (numero));")

def cria_reserva():
    cursor.execute("CREATE TABLE reserva(rg VARCHAR(11) NOT NULL, numero INT(3) NOT NULL, data_reservada DATE NOT NULL, tempo INT(3) DEFAULT NULL,  PRIMARY KEY (rg, numero, data_reservada), KEY fk_rg (rg), KEY fk_numero (numero), CONSTRAINT FOREIGN KEY (rg) REFERENCES cliente(rg) ON DELETE RESTRICT ON UPDATE CASCADE, CONSTRAINT FOREIGN KEY (numero) REFERENCES quarto(numero) ON DELETE RESTRICT ON UPDATE CASCADE);")

def cria_servico():
    cursor.execute("CREATE TABLE servico(codigo VARCHAR(11), tipo VARCHAR(11), descrição VARCHAR(100), valor DECIMAL(5, 2) NOT NULL, PRIMARY KEY (codigo))")

def cria_solicita():
    cursor.execute("CREATE TABLE solicita(codigo VARCHAR(11) NOT NULL, numero INT(3) NOT NULL, PRIMARY KEY (codigo, numero), KEY fk_numero (numero), CONSTRAINT FOREIGN KEY (numero) REFERENCES quarto(numero) ON DELETE RESTRICT ON UPDATE CASCADE);")

def apaga_tables():
    cursor.execute("DROP TABLE cliente;")
    cursor.execute("DROP TABLE ocupa;")
    cursor.execute("DROP TABLE quarto;")
    cursor.execute("DROP TABLE reserva;")
    cursor.execute("DROP TABLE servico;")
    cursor.execute("DROP TABLE solicita;")

def limpa_tables():
    cursor.execute("DELETE FROM cliente;")
    cursor.execute("DELETE FROM ocupa;")
    cursor.execute("DELETE FROM quarto;")
    cursor.execute("DELETE FROM reserva;")
    cursor.execute("DELETE FROM servico;")

def insere_cliente():
    cursor.execute("INSERT INTO cliente VALUES (61110128374, 'João Vitor', 959517963, 'Masculino')")
    cursor.execute("INSERT INTO cliente VALUES (49844791741, 'Bernardo Robalinho Carmo', 977793124, 'Masculino')")
    cursor.execute("INSERT INTO cliente VALUES (19448120552, 'Vitória Guedes Gameiro', 975759409, 'Feminino')")
    cursor.execute("INSERT INTO cliente VALUES (26811719885, 'Hermano Fitas Keil', 915052119, 'Masculino')")
    cursor.execute("INSERT INTO cliente VALUES (46570404980, 'Luke Marcondes Veleda', 912109071, 'Masculino')")
    cursor.execute("INSERT INTO cliente VALUES (75482872565, 'Nalini Olaio Severo', 943497703, 'Feminino')")
    cursor.execute("INSERT INTO cliente VALUES (88445115721, 'Maribel Castelo Boaventura', 948166274, 'Masculino')")
    cursor.execute("INSERT INTO cliente VALUES (40230251257, 'Diana Domingues Remígio', 974265390, 'Femino')")
    cursor.execute("INSERT INTO cliente VALUES (96089661020, 'Zihao Cardoso Macena', 906902418, 'Masculino')")
    cursor.execute("INSERT INTO cliente VALUES (22149842885, 'Berenice Rebimbas Valgueiro', 934873304, 'Masculino')")
    cursor.execute("INSERT INTO cliente VALUES (56320131935, 'Gabriel Campelo Semedo', 911996600, 'Masculino')")
    cursor.execute("INSERT INTO cliente VALUES (63875084678, 'Patrício Fiúza Mata', 923025813, 'NULL')")
    cursor.execute("INSERT INTO cliente VALUES (52184579713, 'Lurdes Cirne França', 939348626, 'Masculino')")
    cursor.execute("INSERT INTO cliente VALUES (65008736059, 'Erick Boto Jordão', NULL, 'Masculino')")
    cursor.execute("INSERT INTO cliente VALUES (80427424164, 'Mikaela Keil Proença', 965928184, 'Feminino')")
    cursor.execute("INSERT INTO cliente VALUES (87514312667, 'Petra Barreiros Carreira', NULL, 'Feminino')")
    cursor.execute("INSERT INTO cliente VALUES (53513348969, 'Ivana da Costa Alves', 977681547, 'NULL')")
    cursor.execute("INSERT INTO cliente VALUES (75208778341, 'Joabe Espinosa Furquim', 914795265, 'Masculino')")
    cursor.execute("INSERT INTO cliente VALUES (14476060141, 'Rafael Brito Vila-Chã', 916416465, 'Masculino')")
    cursor.execute("INSERT INTO cliente VALUES (16525885162, 'Jeremias Paulos Camarinho', 946126603, 'NULL')")
    cursor.execute("INSERT INTO cliente VALUES (88420176763, 'Ayla Malta Raposo', 968837574, 'Feminino')")
    cursor.execute("INSERT INTO cliente VALUES (49167726797, 'Inês Figueira Cachão', 937051705, 'NULL')")
    cursor.execute("INSERT INTO cliente VALUES (14692326089, 'Celeste Galindo Picanço', 914544862, 'Feminino')")
    cursor.execute("INSERT INTO cliente VALUES (68384788670, 'Élton Pureza Ribas', 918536619, 'Masculino')")
    cursor.execute("INSERT INTO cliente VALUES (46599069890, 'Berenice Carvalhal Póvoas', 966401211, 'NULL')")
    cursor.execute("INSERT INTO cliente VALUES (84117735916, 'Milena Cruz Tristão', 970100982, 'Feminino')")
    cursor.execute("INSERT INTO cliente VALUES (18229458416, 'Válter Paiva Alvim', 986973234, 'Masculino')")
    cursor.execute("INSERT INTO cliente VALUES (56013881942, 'Jade Cartaxo Fortes', 949694565, 'Feminino')")
    cursor.execute("INSERT INTO cliente VALUES (54983363397, 'Armando Tigre Dourado', 952477394, 'NULL')")
    cursor.execute("INSERT INTO cliente VALUES (10952907906, 'Fabrício Mortágua Furtado', NULL, 'Masculino')")
    cursor.execute("INSERT INTO cliente VALUES (31416754507, 'Emanuel Pontes Azambuja', 903256211, 'Masculino')")
    cursor.execute("INSERT INTO cliente VALUES (89387023627, 'Cédric Rebotim Morais', NULL, 'Masculino')")
    cursor.execute("INSERT INTO cliente VALUES (85196414655, 'Mellyssa Santarém Cedra', NULL, 'NULL')")
    cursor.execute("INSERT INTO cliente VALUES (27558715532, 'Janice Valério Olivares', NULL, 'Feminino')")
    cursor.execute("INSERT INTO cliente VALUES (11525008512, 'Irís Santarém Paulos', 962774174, 'Feminino')")
    cursor.execute("INSERT INTO cliente VALUES (41484446591, 'Geovanna Orriça Franca', 912848246, 'NULL')")
    cursor.execute("INSERT INTO cliente VALUES (61110758374, 'Fabiana Matos Vides', 990641370, 'Feminino')")
    cursor.execute("INSERT INTO cliente VALUES (56308080210, 'Rodney Macena Alvim', 907774156, 'NULL')")
    cursor.execute("INSERT INTO cliente VALUES (53365889226, 'Giovani Keil Lessa', 925992568, 'Masculino')")
    cursor.execute("INSERT INTO cliente VALUES (91597182654, 'Mikaela Lobato Lagos', 977826294, 'NULL')")
    cursor.execute("INSERT INTO cliente VALUES (36588224374, 'Fabiano Bulhosa Poças', 951271860, 'Masculino')")
    cursor.execute("INSERT INTO cliente VALUES (84571967524, 'Elizabet Lacerda Garrido', 958174278, 'Feminino')")
    cursor.execute("INSERT INTO cliente VALUES (40879800894, 'Teresinha Roçadas Amaral', 960865873, 'Feminino')")
    cursor.execute("INSERT INTO cliente VALUES (45105341623, 'Rayan Parreir Custódio', 989012433, 'Masculino')")
    cursor.execute("INSERT INTO cliente VALUES (12968679239, 'Bruno Faustino Belém', 981200092, 'NULL')")
    cursor.execute("INSERT INTO cliente VALUES (71314284516, 'Rebecca Gravato Esteves', 900214499, 'Feminino')")

def insere_ocupa():
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada) VALUES (61110128374, 100, '2021-12-30');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada, data_saida) VALUES (49844791741, 101, '2021-10-30', '2021-12-30');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada) VALUES (19448120552, 102, '2021-11-30');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada, data_saida) VALUES (26811719885, 103, '2021-10-03', '2021-11-03');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada) VALUES (46570404980, 104, '2021-01-30');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada, data_saida) VALUES (75482872565, 105, '2021-12-30', '2022-01-30');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada) VALUES (88445115721, 106, '2021-10-20');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada, data_saida) VALUES (40230251257, 107, '2020-12-24', '2021-01-22');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada) VALUES (96089661020, 108, '2021-12-30');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada, data_saida) VALUES (22149842885, 109, '2021-12-03', '2021-12-30');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada) VALUES (56320131935, 306, '2021-10-23');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada, data_saida) VALUES (63875084678, 307, '2021-12-08', '2021-12-30');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada) VALUES (52184579713, 308, '2021-11-07');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada, data_saida) VALUES (65008736059, 309, '2021-12-30', '2022-01-01');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada) VALUES (80427424164, 400, '2021-12-02');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada) VALUES (87514312667, 401, '2021-12-18');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada, data_saida) VALUES (53513348969, 402, '2021-12-30', '2022-01-20');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada) VALUES (75208778341, 403, '2021-12-21');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada, data_saida) VALUES (14476060141, 404, '2021-11-28', '2021-12-01');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada) VALUES (16525885162, 405, '2021-07-30');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada, data_saida) VALUES (88420176763, 406, '2021-11-20', '2021-11-28');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada) VALUES (49167726797, 407, '2021-11-30');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada, data_saida) VALUES (14692326089, 408, '2021-11-03', '2021-11-28');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada) VALUES (68384788670, 409, '2021-11-27');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada, data_saida) VALUES (46599069890, 500, '2021-11-30', '2022-01-01');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada) VALUES (84117735916, 501, '2021-11-20');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada, data_saida) VALUES (18229458416, 502, '2021-11-01', '2021-12-01');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada, data_saida) VALUES (56013881942, 503, '2021-10-30', '2021-11-28');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada) VALUES (54983363397, 504, '2021-11-03');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada, data_saida) VALUES (10952907906, 505, '2021-11-20', '2021-12-01');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada) VALUES (31416754507, 506, '2021-12-30');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada, data_saida) VALUES (89387023627, 507, '2021-11-30', '2021-12-30');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada) VALUES (85196414655, 508, '2021-10-30');")
    cursor.execute("INSERT INTO ocupa (rg, numero, data_entrada, data_saida) VALUES (27558715532, 509, '2021-11-03', '2021-12-01');")

def insere_reserva():
    cursor.execute("INSERT INTO reserva (rg, numero, data_reservada) VALUES (71314284516, 200, '2021-12-30');")
    cursor.execute("INSERT INTO reserva (rg, numero, data_reservada, tempo) VALUES (12968679239, 201, '2021-12-30', 20);")
    cursor.execute("INSERT INTO reserva (rg, numero, data_reservada) VALUES (45105341623, 202, '2021-12-30');")
    cursor.execute("INSERT INTO reserva (rg, numero, data_reservada, tempo) VALUES (40879800894, 203, '2021-12-30', 60);")
    cursor.execute("INSERT INTO reserva (rg, numero, data_reservada, tempo) VALUES (84571967524, 204, '2021-12-30', 10);")
    cursor.execute("INSERT INTO reserva (rg, numero, data_reservada, tempo) VALUES (91597182654, 205, '2021-12-30', 15);")
    cursor.execute("INSERT INTO reserva (rg, numero, data_reservada, tempo) VALUES (53365889226, 206, '2021-12-30', 22);")
    cursor.execute("INSERT INTO reserva (rg, numero, data_reservada, tempo) VALUES (56308080210, 207, '2021-12-30', 2);")
    cursor.execute("INSERT INTO reserva (rg, numero, data_reservada, tempo) VALUES (61110758374, 208, '2021-12-30', 19);")
    cursor.execute("INSERT INTO reserva (rg, numero, data_reservada, tempo) VALUES (41484446591, 209, '2021-12-30', 12);")
    cursor.execute("INSERT INTO reserva (rg, numero, data_reservada) VALUES (11525008512, 300, '2021-12-30');")
    cursor.execute("INSERT INTO reserva (rg, numero, data_reservada, tempo) VALUES (36588224374, 305, '2021-12-30', 25);")

def insere_quarto():
     cursor.execute("INSERT INTO quarto (numero, andar, preço) VALUES (100, 1, 110);")
     cursor.execute("INSERT INTO quarto (numero, andar, preço) VALUES (101, 1, 110);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, preço) VALUES (102, 1, 'Casal', 150);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, preço) VALUES (103, 1, 'Casal', 150);")
     cursor.execute("INSERT INTO quarto (numero, andar, preço) VALUES (104, 1, 110);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, preço) VALUES (105, 1, 'Casal', 150);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, preço) VALUES (106, 1,'Casal', 150);")
     cursor.execute("INSERT INTO quarto (numero, andar, preço) VALUES (107, 1, 110);")
     cursor.execute("INSERT INTO quarto (numero, andar, preço) VALUES (108, 1, 110);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, preço) VALUES (109, 1,'Casal', 150);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, preço) VALUES (200, 2, 'Dormitório', 50);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, preço) VALUES (201, 2, 'Duplo Solteiro', 150);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, preço) VALUES (202, 2, 'Duplo Solteiro', 150);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, preço) VALUES (203, 2, 'Duplo Solteiro', 150);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, preço) VALUES (204, 2, 'Duplo Solteiro', 150);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (205, 2, 'Duplo Solteiro', 'Executivo', 200);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (206, 2, 'Duplo Solteiro', 'Executivo', 200);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (207, 2, 'Duplo Solteiro', 'Executivo', 200);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (208, 2, 'Duplo Solteiro', 'Executivo', 200);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (209, 2, 'Casal', 'Executivo', 200);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (300, 3, 'Casal', 'Executivo', 200);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, preço) VALUES (301, 3, 'Dormitório', 50);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (302, 3, 'Casal', 'Executivo', 200);")
     cursor.execute("INSERT INTO quarto (numero, andar, descrição, preço) VALUES (303, 3, 'Executivo', 150);")
     cursor.execute("INSERT INTO quarto (numero, andar, descrição, preço) VALUES (304, 3, 'Executivo', 150);")
     cursor.execute("INSERT INTO quarto (numero, andar, descrição, preço) VALUES (305, 3, 'Executivo', 150);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (306, 3, 'Casal', 'Executivo', 200);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (307, 3, 'Casal', 'Executivo', 200);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (308, 3, 'Casal', 'Executivo', 200);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (309, 3, 'Casal', 'Executivo', 200);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (400, 4, 'Dormitório', 'Executivo', 110);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (401, 4, 'Casal', 'Executivo', 200);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (402, 4, 'Duplo Solteiro', 'Executivo', 200);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (403, 4, 'Casal', 'Executivo', 200);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (404, 4, 'Duplo Solteiro', 'Executivo', 200);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (405, 4, 'Casal', 'Executivo', 200);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (406, 4, 'Duplo Solteiro', 'Executivo', 200);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (407, 4, 'Casal', 'Executivo', 200);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (408, 4, 'Duplo Solteiro', 'Executivo', 200);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (409, 4, 'Duplo solteiro', 'Deluxe', 300);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (500, 5, 'Dormitório', 'Deluxe', 150);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (501, 5, 'Casal', 'Executivo', 225);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (502, 5, 'Casal', 'Executivo', 225);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (503, 5, 'Casal', 'Executivo', 225);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (504, 5, 'Casal', 'Deluxe', 300);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (505, 5, 'Casal', 'Deluxe', 300);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (506, 5, 'Casal', 'Deluxe', 300);")
     cursor.execute("INSERT INTO quarto (numero, andar, descrição, preço) VALUES (507, 5, 'Deluxe', 200);")
     cursor.execute("INSERT INTO quarto (numero, andar, descrição, preço) VALUES (508, 5, 'Deluxe', 200);")
     cursor.execute("INSERT INTO quarto (numero, andar, tipo, descrição, preço) VALUES (509, 5, 'Duplo solteiro', 'Deluxe', 300);")

def insere_servico():#manutenção(MAN000), encanamento(ENC000), limpeza(LIM000), refeição(REF000)
    cursor.execute("INSERT INTO servico (codigo, tipo, descrição, valor) VALUES ('MAN001', 'manutenção', 'ar-condicionado quebrado', 0);")
    cursor.execute("INSERT INTO servico (codigo, tipo, descrição, valor) VALUES ('MAN002', 'manutenção', 'televisão quebrada', 0);")
    cursor.execute("INSERT INTO servico (codigo, tipo, descrição, valor) VALUES ('MAN003', 'manutenção', 'aquecedor quebrado', 0);")
    cursor.execute("INSERT INTO servico (codigo, tipo, descrição, valor) VALUES ('MAN004', 'manutenção', 'refrigerador quebrado', 0);")
    cursor.execute("INSERT INTO servico (codigo, tipo, descrição, valor) VALUES ('MAN005', 'manutenção', 'computador quebrado', 0);")
    cursor.execute("INSERT INTO servico (codigo, tipo, descrição, valor) VALUES ('ENC001', 'encanamento', 'chuveiro entupida', 10);")
    cursor.execute("INSERT INTO servico (codigo, tipo, descrição, valor) VALUES ('ENC002', 'encanamento', 'pia entupida', 10);")
    cursor.execute("INSERT INTO servico (codigo, tipo, descrição, valor) VALUES ('ENC003', 'encanamento', 'ralo entupida', 0);")
    cursor.execute("INSERT INTO servico (codigo, tipo, descrição, valor) VALUES ('ENC004', 'encanamento', 'privada entupida', 10);")
    cursor.execute("INSERT INTO servico (codigo, tipo, descrição, valor) VALUES ('LIM001', 'limpeza', 'geral quarto', 20);")
    cursor.execute("INSERT INTO servico (codigo, tipo, descrição, valor) VALUES ('LIM002', 'limpeza', 'geral banheiro', 15);")
    cursor.execute("INSERT INTO servico (codigo, tipo, descrição, valor) VALUES ('LIM003', 'limpeza', 'geral quarto deluxe', 50);")
    cursor.execute("INSERT INTO servico (codigo, tipo, descrição, valor) VALUES ('LIM004', 'limpeza', 'limpeza cama', 5);")
    cursor.execute("INSERT INTO servico (codigo, tipo, descrição, valor) VALUES ('REF001', 'refeição', 'receber cafe', 10);")
    cursor.execute("INSERT INTO servico (codigo, tipo, descrição, valor) VALUES ('REF002', 'refeição', 'receber almoço', 10);")
    cursor.execute("INSERT INTO servico (codigo, tipo, descrição, valor) VALUES ('REF003', 'refeição', 'receber janta', 10);")

def insere_solicita():
    cursor.execute("INSERT INTO solicita VALUES ('MAN001', 100);")
    cursor.execute("INSERT INTO solicita VALUES ('MAN001', 200);")
    cursor.execute("INSERT INTO solicita VALUES ('MAN002', 109);")
    cursor.execute("INSERT INTO solicita VALUES ('MAN003', 408);")
    cursor.execute("INSERT INTO solicita VALUES ('MAN004', 206);")
    cursor.execute("INSERT INTO solicita VALUES ('MAN005', 205);")
    cursor.execute("INSERT INTO solicita VALUES ('ENC001', 105);")
    cursor.execute("INSERT INTO solicita VALUES ('ENC002', 106);")
    cursor.execute("INSERT INTO solicita VALUES ('ENC003', 105);")
    cursor.execute("INSERT INTO solicita VALUES ('ENC004', 103);")
    cursor.execute("INSERT INTO solicita VALUES ('LIM001', 302);")
    cursor.execute("INSERT INTO solicita VALUES ('LIM002', 305);")
    cursor.execute("INSERT INTO solicita VALUES ('LIM003', 502);")
    cursor.execute("INSERT INTO solicita VALUES ('LIM004', 103);")
    cursor.execute("INSERT INTO solicita VALUES ('REF001', 302);")
    cursor.execute("INSERT INTO solicita VALUES ('REF002', 505);")
    cursor.execute("INSERT INTO solicita VALUES ('REF003', 302);")

def cria_tables():
    cria_cliente()
    cria_ocupa()
    cria_quarto()
    cria_reserva()
    cria_servico()
    cria_solicita()

def cria_dados():
    insere_cliente()
    insere_ocupa()
    insere_reserva()
    insere_quarto()
    insere_servico()
    insere_solicita()

def select_cliente():
    consulta = "SELECT * FROM cliente"
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    print("Número total de registros retornados: ", cursor.rowcount, "\n")
    print("Mostrando os clientes cadastrados")
    for linha in linhas:
        print("RG:", linha[0])
        print("Nome:", linha[1])
        print("Fone:", linha[2])
        print("Sexo:", linha[3], "\n")

def select_quarto():
    consulta = "SELECT * FROM quarto"
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    print("Número total de registros retornados: ", cursor.rowcount, "\n")
    print("Mostrando os quartos cadastrados")
    for linha in linhas:
        print("Número:", linha[0])
        print("Andar:", linha[1])
        print("Tipo:", linha[2])
        print("Descrição:", linha[3], "\n")

def select_reserva():
    consulta = "SELECT * FROM reserva"
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    print("Número total de registros retornados: ", cursor.rowcount, "\n")
    print("Mostrando reservas cadastradas")
    for linha in linhas:
        print("RG:", linha[0])
        print("Número:", linha[1])
        print("Data Reservada:", linha[2])
        print("Tempo:", linha[3], "dias\n")

def select_ocupa():
    consulta = "SELECT * FROM ocupa"
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    print("Número total de registros retornados: ", cursor.rowcount, "\n")
    print("Mostrando ocupacao cadastradas")
    for linha in linhas:
        print("RG:", linha[0])
        print("Número:", linha[1])
        print("Data Entrada:", linha[2])
        print("Data Saída:", linha[3], "\n")

def select_servico():
    consulta = "SELECT * FROM servico"
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    print("Número total de registros retornados: ", cursor.rowcount, "\n")
    print("Mostrando os serviços cadastrados")
    for linha in linhas:
        print("Código:", linha[0])
        print("Tipo:", linha[1])
        print("Descrição:", linha[2])
        print("Valor:", linha[3], "\n")

def select_detcliente():
    consulta = "SELECT * FROM cliente WHERE sexo = 'Masculino' AND fone is NULL"
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    print("Número total de registros retornados: ", cursor.rowcount, "\n")
    print("Mostrando os clientes cadastrados")
    for linha in linhas:
        print("RG:", linha[0])
        print("Nome:", linha[1])
        print("Fone:", linha[2])
        print("Sexo:", linha[3], "\n")

def select_detquarto():
    consulta = "SELECT * FROM quarto WHERE tipo = 'Casal' AND descrição = 'Deluxe'"
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    print("Número total de registros retornados: ", cursor.rowcount, "\n")
    print("Mostrando os clientes cadastrados")
    for linha in linhas:
        print("Número:", linha[0])
        print("Andar:", linha[1])
        print("Tipo:", linha[2])
        print("Descrição:", linha[3])
        print("Preço: R$", linha[4], "\n")

def qttd_quarto():
    consulta = "SELECT tipo, COUNT(*) FROM quarto GROUP BY tipo"
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    print("Número total de registros retornados: ", cursor.rowcount, "\n")
    print("Mostrando os quartos cadastrados")
    for linha in linhas:
        print("Tipo:", linha[0])
        print("Quantidade:", linha[1], "\n")

def tipo_servico():
    consulta = "SELECT tipo, COUNT(*) FROM servico GROUP BY tipo"
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    print("Número total de registros retornados: ", cursor.rowcount, "\n")
    print("Mostrando os quartos cadastrados")
    for linha in linhas:
        print("Tipo:", linha[0])
        print("Quantidade:", linha[1], "\n")

def quarto_reser():
    consulta = "SELECT q.numero, r.rg FROM quarto q JOIN reserva r ON q.numero = r.numero "
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    print("Número total de registros retornados: ", cursor.rowcount, "\n")
    print("Mostrando os quartos cadastrados")
    for linha in linhas:
        print("Número:", linha[0])
        print("RG da pessoa:", linha[1], "\n")

def quarto_ocup():
    consulta = "SELECT q.numero, o.rg FROM quarto q  JOIN ocupa o ON q.numero = o.numero"
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    print("Número total de registros retornados: ", cursor.rowcount, "\n")
    print("Mostrando os quartos cadastrados")
    for linha in linhas:
        print("Número:", linha[0])
        print("RG da pessoa:", linha[1], "\n")

def select_sol():
    consulta = "SELECT * FROM solicita"
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    print("Número total de registros retornados: ", cursor.rowcount, "\n")
    print("Mostrando as solicitacoes cadastradas")
    for linha in linhas:
        print("Codigo:", linha[0])
        print("Numero:", linha[1], "\n")

def insere_manucliente():
    string_rg = input("Digite o RG:\n")
    string_nome = input("Digite o nome:\n")
    string_fone = input("Digite o fone:\n")
    string_sexo = input("Digite o sexo:\n")

    dados = (string_rg, string_nome, string_fone, string_sexo)
    comando = "INSERT INTO cliente (rg, nome, fone, sexo) VALUES (%s, %s, %s, %s)"
    cursor.execute(comando, dados)
    banco.commit()

def insere_manusolicita():
    string_cod = input("Digite o Codigo:\n")
    string_num = input("Digite o Numero do quarto:\n")

    dados = (string_cod, string_num)
    comando = "INSERT INTO solicita (codigo, numero) VALUES (%s, %s)"
    cursor.execute(comando, dados)
    banco.commit()

def insere_manuservico():
    string_cod = input("Digite o Codigo:\n")
    string_tipo = input("Digite o Tipo:\n")
    string_desc = input("Digite o Descricão:\n")
    string_valor = input("Digite o Valor:\n")

    dados = (string_cod, string_tipo, string_desc, string_valor)
    comando = "INSERT INTO servico (codigo, tipo, descrição, valor) VALUES (%s, %s, %s, %s)"
    cursor.execute(comando, dados)
    banco.commit()

def insere_manureser():
    print("OBS: Insira o Cliente como mesmo RG tambem\n")
    string_rg = input("Digite o RG:\n")
    string_num = input("Digite o Número do quarto:\n")
    string_datres = input("Digite  a Data da Reserva(aaaa-mm-dd):\n")
    string_temp= input("Digite o Tempo:\n")

    dados = (string_rg, string_num, string_datres, string_temp)
    comando = "INSERT INTO reserva (rg, numero, data_reservada, tempo) VALUES (%s, %s, %s, %s)"
    cursor.execute(comando, dados)
    banco.commit()

def insere_manuocup():
    print("OBS: Insira o Cliente com o mesmo RG tambem\n")
    string_rg = input("Digite o RG:\n")
    string_num = input("Digite o Número do quarto:\n")
    string_datent = input("Digite a Data de Entrada(aaaa-mm-dd):\n")
    string_datsai = input("Digite o Data de Saída(aaaa-mm-dd):\n")

    dados = (string_rg, string_num, string_datent, string_datsai)
    comando = "INSERT INTO ocupa (rg, numero, data_entrada, data_saida) VALUES (%s, %s, %s, %s)"
    cursor.execute(comando, dados)
    banco.commit()

def del_cliente():
    string_rg = input("Digite o RG:\n")

    comando = "DELETE FROM cliente WHERE rg = %s" %string_rg
    cursor.execute(comando)
    banco.commit()

def selecionar():
    print("===Tabela de Selecionar:===\n")
    print("1:Selecionar cliente")
    print("2:Selecionar reserva")
    print("3:Selecionar servico")
    print("4:Selecionar quarto")
    print("5:Selecionar clientes masculino sem fone registrado")
    print("6:Selecionar quarto de Deluxe para casais ")
    print("7:Selecionar qtdd de quartos por tipo ")
    print("8:Selecionar servico por tipo")
    print("9:Selecionar quartos reservados")
    print("10:Selecionar quartos ocupados")
    print("11:Selecionar solicitacoes")
    print("12:Selecionar ocupacao")
    num = int(input())
    if(num==0):
        pass
    elif(num==1):
        select_cliente()
    elif(num==2):
        select_reserva()
    elif(num==3):
        select_servico()
    elif(num==4):
        select_quarto()
    elif(num==5):
        select_detcliente()
    elif(num==6):
        select_detquarto()
    elif(num==7):
        qttd_quarto()
    elif(num==8):
        tipo_servico()
    elif(num==9):
        quarto_reser()
    elif(num==10):
        quarto_ocup()   
    elif(num==11):
        select_sol()  
    elif(num==12):
        select_ocupa()
    else:
        print("Opção Inexistente")

def escolh_ins():
    print("===Tabela de Inserir:===\n")
    print("1:Inserir cliente")
    print("2:Inserir solicitacao")
    print("3:Inserir servico")
    print("4:Inserir ocupacao")
    print("5:Inserir reserva")
    num = int(input())
    if(num==1):
        insere_manucliente()
    elif(num==2):
        insere_manusolicita()
    elif(num==3):
        insere_manuservico()
    elif(num==4):
        insere_manuocup()
    elif(num==5):
        insere_manureser()
    else:
        print("Opção Inexistente")

def escolha():
    print("===Tabela Geral:===\n")
    print("0:Sair")
    print("1:Apaga tabelas")
    print("2:Criar tabelas")
    print("3:Criar dados das tabelas")
    print("4:Selecionar um tabela")
    print("5:Inserir na tabela")
    print("6:Deletar cliente")
    num = int(input())
    if(num==0):
        pass
    elif(num==1):
        apaga_tables()
    elif(num==2):
        cria_tables()
    elif(num==3):
        cria_dados()
    elif(num==4):
        selecionar()
    elif(num==5):
       escolh_ins()
    elif(num==6):
       del_cliente()
    else:
        print("Opção Inexistente")
    return num

if __name__ == "__main__":
    usa_hotel()

    retornador = 1
    while(retornador!=0):
        retornador = escolha()

    banco.close()

