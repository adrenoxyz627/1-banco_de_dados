USE hotel;
CREATE TABLE quarto(
	número INT(3) NOT NULL,
    andar INT(1) NOT NULL,
    tipo VARCHAR(20) DEFAULT 'Casal',
    descrição VARCHAR(20) DEFAULT 'Standard',
    preço DECIMAL(5,2) NOT NULL,
    PRIMARY KEY (número)
);

