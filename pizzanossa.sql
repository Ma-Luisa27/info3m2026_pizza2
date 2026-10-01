-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Host: psi2025_mysql
-- Tempo de geração: 01/10/2026 às 11:44
-- Versão do servidor: 8.0.46
-- Versão do PHP: 8.3.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `psi2025_pizzanossa`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('88c3864f97aa');

-- --------------------------------------------------------

--
-- Estrutura para tabela `pedido`
--

CREATE TABLE `pedido` (
  `id` int NOT NULL,
  `usuario_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `pedido`
--

INSERT INTO `pedido` (`id`, `usuario_id`) VALUES
(1, 4),
(3, 4),
(2, 5);

-- --------------------------------------------------------

--
-- Estrutura para tabela `pizza`
--

CREATE TABLE `pizza` (
  `id` int NOT NULL,
  `sabor` varchar(100) DEFAULT NULL,
  `preco` float DEFAULT NULL,
  `imagem` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `pizza`
--

INSERT INTO `pizza` (`id`, `sabor`, `preco`, `imagem`) VALUES
(1, 'Muzzarela', 20, 'uploads/cb130f6920fc42a3bc4179affa4eaa6d.webp'),
(2, 'Calabreza', 40, 'uploads/87422c3ae91b4a14a587d6227dd280f9.jpg'),
(8, 'Catupiry', 50, 'uploads/f35231bb50734d2ba14b672964756a0e.jpg');

-- --------------------------------------------------------

--
-- Estrutura para tabela `pizza_pedido`
--

CREATE TABLE `pizza_pedido` (
  `pedido_id` int NOT NULL,
  `pizza_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `pizza_pedido`
--

INSERT INTO `pizza_pedido` (`pedido_id`, `pizza_id`) VALUES
(1, 1),
(2, 1),
(3, 1),
(1, 2);

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuario`
--

CREATE TABLE `usuario` (
  `id` int NOT NULL,
  `nome` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `senha` varchar(200) DEFAULT NULL,
  `administrador` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `usuario`
--

INSERT INTO `usuario` (`id`, `nome`, `email`, `senha`, `administrador`) VALUES
(4, 'Ítalo', 'italo@ifrn.edu.br', '123', 0),
(5, 'Mariele', 'mariele@email.com', '951', 0),
(8, 'Alba', 'alba.lopes@ifrn.edu.br', 'scrypt:32768:8:1$0ixGeAZZROiSPfEV$5b14aac9dbb337f7ac98456a6d6125bf980bc66a12760089b94e3e6b2a640ccb8f0b962287bc2f820a557771bf0f68bc639cc05cf75f6ed809198e25797e43fa', 1),
(9, 'Pedro', 'pedro@email.com', 'scrypt:32768:8:1$KU6x8wkHb5mpTgwO$491411e0fab89902bc9aa04a2b8fd0058b0afe908fdcdd2fd74bd5e375049483486344fc08e6a00927b36d5027d2fac73439c7fe50fdb21c84e7079e6df01793', 0),
(10, 'Maria Luisa', 'marialuisa@ifrn.edu.br', 'scrypt:32768:8:1$54rBz29ZVHT2bZG1$b3105c524d2ae36519429acc2d74378a86025bd41528fb026bd3c4768fefe709d13f2006065a8d07e0ad323a7cc001c7e70d8b1758a2778fbab9dc6347c5aeda', 0),
(12, 'admin', 'admin@email.com', 'scrypt:32768:8:1$RnyHP8AiyQvLv2XW$915007e166ad6f82bac54f47c842a4a82c687dfd32a94036f32b4b3f34104b4796d60751e09032a6e314b8f68f92cc043230b324ea1454e345574de9c87732a5', 1);

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Índices de tabela `pedido`
--
ALTER TABLE `pedido`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_pedido_usuario_id` (`usuario_id`);

--
-- Índices de tabela `pizza`
--
ALTER TABLE `pizza`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `pizza_pedido`
--
ALTER TABLE `pizza_pedido`
  ADD PRIMARY KEY (`pedido_id`,`pizza_id`),
  ADD KEY `pizza_id` (`pizza_id`);

--
-- Índices de tabela `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `pedido`
--
ALTER TABLE `pedido`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `pizza`
--
ALTER TABLE `pizza`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de tabela `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `pedido`
--
ALTER TABLE `pedido`
  ADD CONSTRAINT `fk_pedido_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`);

--
-- Restrições para tabelas `pizza_pedido`
--
ALTER TABLE `pizza_pedido`
  ADD CONSTRAINT `pizza_pedido_ibfk_1` FOREIGN KEY (`pedido_id`) REFERENCES `pedido` (`id`),
  ADD CONSTRAINT `pizza_pedido_ibfk_2` FOREIGN KEY (`pizza_id`) REFERENCES `pizza` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
