SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `fraude_transaction`
--

CREATE DATABASE IF NOT EXISTS fraude_transaction;
USE fraude_transaction;

-- --------------------------------------------------------

--
-- Structure de la table `origin`
--

DROP TABLE IF EXISTS `origin`;
CREATE TABLE IF NOT EXISTS `origin` (
  `idOrigin` varchar(50) NOT NULL,
  `NAME` varchar(50) DEFAULT NULL,
  `balance` decimal(15,2) DEFAULT NULL,
  PRIMARY KEY (`idOrigin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `receiver`
--

DROP TABLE IF EXISTS `receiver`;
CREATE TABLE IF NOT EXISTS `receiver` (
  `idReceiver` int NOT NULL,
  `NAME` varchar(50) DEFAULT NULL,
  `balance` decimal(15,2) DEFAULT NULL,
  PRIMARY KEY (`idReceiver`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
CREATE TABLE IF NOT EXISTS `transaction` (
  `idOrigin` int NOT NULL,
  `idReceiver` int NOT NULL,
  `idTransaction` int NOT NULL,
  `amount` decimal(15,2) DEFAULT NULL,
  `step` int DEFAULT NULL,
  `TYPE` varchar(50) DEFAULT NULL,
  `newBalanceOrig`decimal(15,2) DEFAULT NULL,
  `newBalanceDest`decimal(15,2) DEFAULT NULL,
  `isFraude` int DEFAULT NULL,
  PRIMARY KEY (`idOrigin`,`idReceiver`),
  KEY `idReceiver` (`idReceiver`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `transaction`
--
ALTER TABLE `transaction`
  ADD CONSTRAINT `transaction_ibfk_1` FOREIGN KEY (`idOrigin`) REFERENCES `origin` (`idOrigin`),
  ADD CONSTRAINT `transaction_ibfk_2` FOREIGN KEY (`idReceiver`) REFERENCES `receiver` (`idReceiver`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
