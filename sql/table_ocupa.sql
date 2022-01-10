USE hotel;
CREATE TABLE ocupa(
	rg VARCHAR(11) NOT NULL,
    número INT(3) NOT NULL,
    data_entrada DATE NOT NULL,
    data_saida DATE,
    FOREIGN KEY (rg) REFERENCES cliente(rg),
	FOREIGN KEY (número) REFERENCES quarto(número),
	PRIMARY KEY (rg, número, data_entrada)
);

