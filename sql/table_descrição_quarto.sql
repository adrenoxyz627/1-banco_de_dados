USE hotel;
CREATE TABLE descição_quarto(
	descrição VARCHAR(20),
    detalhes VARCHAR(200),
    FOREIGN KEY (descição) REFERENCES quarto(descrição),
);

