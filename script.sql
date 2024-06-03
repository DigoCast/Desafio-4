CREATE DATABASE avaliacoes_site;
USE avaliacoes_site;

CREATE TABLE avaliacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    avaliacao INT NOT NULL CHECK (avaliacao BETWEEN 1 AND 5),
    comentario TEXT,
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);