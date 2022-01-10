USE hotel;
CREATE TABLE reserva(
	rg VARCHAR(11) NOT NULL,
    número INT(3) NOT NULL,
    data_reservada DATE NOT NULL,
    tempo INT(3),
    FOREIGN KEY (rg) REFERENCES cliente(rg),
	FOREIGN KEY (número) REFERENCES quarto(número),
	PRIMARY KEY (rg, número, data_reservada)
);

