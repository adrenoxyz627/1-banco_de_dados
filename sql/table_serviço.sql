USE hotel;
CREATE TABLE serviço(
	código VARCHAR(11) NOT NULL,
    tipo INT(3) NOT NULL,
    descrição VARCHAR(100),
    valor DECIMAL(5, 2),
    num_quarto INT(3) NOT NULL,
    FOREIGN KEY (num_quarto) REFERENCES quarto(número),
	PRIMARY KEY (código)
);

