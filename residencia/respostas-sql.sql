-- QUESTAO 1 --
SELECT * FROM produtos;

-- QUESTAO 2 --
SELECT nome, preco FROM produtos;

-- QUESTAO 3 --
SELECT * FROM produtos WHERE preco > 50;

-- QUESTAO 4 --
SELECT * FROM produtos WHERE estoque < 10;

-- QUESTAO 5 --
SELECT * FROM produtos ORDER BY preco ASC;

-- QUESTAO 6 --
SELECT * FROM produtos ORDER BY estoque DESC;

-- QUESTAO 7 --
SELECT * FROM produtos WHERE nome LIKE 'A%';

-- QUESTAO 8 --
SELECT * FROM produtos WHERE nome LIKE '%o';

-- QUESTAO 9 --
SELECT * FROM produtos WHERE nome LIKE '%tech%';

-- QUESTAO 10 --
SELECT * FROM produtos WHERE preco BETWEEN 20 AND 100;

-- QUESTAO 11 --
SELECT * FROM produtos WHERE estoque BETWEEN 5 AND 50;

-- QUESTAO 12 --
SELECT * FROM produtos WHERE email IS NULL;

-- QUESTAO 13 --
SELECT * FROM produtos WHERE email IS NOT NULL;

-- QUESTAO 14 --
SELECT * FROM produtos ORDER BY preco DESC LIMIT 5;

-- QUESTAO 15 --
SELECT * FROM produtos ORDER BY estoque ASC LIMIT 10;

-- QUESTAO 16 --
SELECT COUNT(*) FROM produtos;

-- QUESTAO 17 --
SELECT AVG(preco) FROM produtos;

-- QUESTAO 18 --
SELECT SUM(estoque) FROM produtos;

-- QUESTAO 19 --
SELECT MAX(preco) FROM produtos;

-- QUESTAO 20 --
SELECT MIN(preco) FROM produtos;
