USE hotel;
CREATE TABLE solicita(
	código VARCHAR(11) NOT NULL,
    número INT(3) NOT NULL,
    FOREIGN KEY (número) REFERENCES quarto(número),
	PRIMARY KEY (código)
);

