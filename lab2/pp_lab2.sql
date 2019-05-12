-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 12, 2019 at 12:42 PM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.3.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pp_lab2`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `addClient` (IN `_name` VARCHAR(100) CHARSET utf8)  INSERT INTO clients(ID_Clients,ClientName) VALUES(NULL,_name)$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `addOrder` (IN `_date` DATE, IN `ID_Client` INT)  INSERT INTO orders VALUES(NULL,_date,ID_Client)$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `addOS` (IN `Order_ID` INT, IN `Service_ID` INT, IN `Quentity` INT)  INSERT INTO orders_services VALUES(Null,Order_ID,Service_ID,Quentity)$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `addService` (IN `name` VARCHAR(100) CHARSET utf8, IN `price` DOUBLE)  INSERT INTO services VALUES(NULL,name,price)$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `deleteClient` (IN `name` VARCHAR(100) CHARSET utf8)  DELETE FROM `clients` WHERE clients.ClientName=name$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `deleteOrder` (IN `ID_Order` INT)  DELETE FROM orders WHERE ID_Orders=ID_Order$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `deleteOS` (IN `ID_OS` INT)  DELETE FROM orders_services WHERE orders_services.ID_Orders_Services = ID_OS$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `deleteService` (IN `_name` VARCHAR(100) CHARSET utf8)  DELETE FROM services WHERE services.ServiceName = _name$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `getClient` (IN `id` INT)  SELECT * FROM `clients` WHERE ID_Clients=id$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `getClients` ()  SELECT * FROM clients$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `getOrder` (IN `_id` INT)  SELECT ID_Orders,OrderDate,ClientName from orders INNER JOIN clients ON Clients_ID=ID_Clients WHERE ID_Orders=_id$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `getOrders` ()  SELECT ID_Orders,OrderDate,ClientName FROM orders INNER JOIN clients ON Clients_ID = ID_Clients$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `getOS` (IN `id_OS` INT)  SELECT orders_services.ID_Orders_Services,orders.OrderDate,clients.ClientName,services.ServiceName,services.Price FROM orders_services INNER JOIN orders ON orders.ID_Orders=orders_services.Orders_ID INNER JOIN services ON services.ID_Services = orders_services.Services_ID INNER JOIN clients ON clients.ID_Clients=orders.Clients_ID WHERE orders_services.ID_Orders_Services=id_OS$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `getOSS` ()  SELECT orders_services.ID_Orders_Services,orders.OrderDate,clients.ClientName,services.ServiceName,services.Price FROM orders_services INNER JOIN orders ON orders.ID_Orders=orders_services.Orders_ID INNER JOIN services ON services.ID_Services = orders_services.Services_ID INNER JOIN clients ON clients.ID_Clients=orders.Clients_ID$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `getService` (IN `id_service` INT)  SELECT * FROM services WHERE services.ID_Services=id_service$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `getServices` ()  SELECT * FROM services$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `updateClient` (IN `_id` INT, IN `name` VARCHAR(100))  UPDATE clients SET ClientName=name WHERE ID_Clients=_id$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `updateOrder` (IN `ID_Order` INT, IN `_date` DATE, IN `Client_ID` INT)  UPDATE orders SET OrderDate=_date, Clients_ID = Client_ID WHERE ID_Orders=ID_Order$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `updateOS` (IN `Order_ID` INT, IN `Service_ID` INT, IN `Quentity` INT, IN `ID_OS` INT)  UPDATE orders_services SET orders_services.Orders_ID=Order_ID, orders_services.Services_ID=Service_ID, orders_services.Quentity = Quentity WHERE orders_services.ID_Orders_Services = ID_OS$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `updateService` (IN `id_service` INT, IN `name` VARCHAR(100) CHARSET utf8, IN `price` DOUBLE)  UPDATE services SET services.ServiceName=name, services.Price = price WHERE services.ID_Services = id_service$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `clients`
--

CREATE TABLE `clients` (
  `ID_Clients` int(11) NOT NULL,
  `ClientName` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `clients`
--

INSERT INTO `clients` (`ID_Clients`, `ClientName`) VALUES
(22, 'Kylie Jenner(Updated name)'),
(24, 'Kropotin Ivan'),
(25, 'Helena Swid'),
(26, 'Helena Swid'),
(27, 'Helena Swid'),
(28, 'Helena Swid');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `ID_Orders` int(11) NOT NULL,
  `OrderDate` datetime NOT NULL,
  `Clients_ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`ID_Orders`, `OrderDate`, `Clients_ID`) VALUES
(1, '0000-00-00 00:00:00', 22),
(3, '0000-00-00 00:00:00', 24);

-- --------------------------------------------------------

--
-- Table structure for table `orders_services`
--

CREATE TABLE `orders_services` (
  `ID_Orders_Services` int(11) NOT NULL,
  `Orders_ID` int(10) NOT NULL,
  `Services_ID` int(10) NOT NULL,
  `Quentity` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `orders_services`
--

INSERT INTO `orders_services` (`ID_Orders_Services`, `Orders_ID`, `Services_ID`, `Quentity`) VALUES
(3, 1, 2, 5),
(5, 1, 1, 3),
(6, 1, 2, 4),
(7, 2, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `services`
--

CREATE TABLE `services` (
  `ID_Services` int(11) NOT NULL,
  `ServiceName` varchar(100) NOT NULL,
  `Price` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `services`
--

INSERT INTO `services` (`ID_Services`, `ServiceName`, `Price`) VALUES
(1, 'Change motor', 15000),
(2, 'Замена литых дисков', 5000),
(11, 'Change color', 800);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `clients`
--
ALTER TABLE `clients`
  ADD PRIMARY KEY (`ID_Clients`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`ID_Orders`),
  ADD KEY `Clients_ID` (`Clients_ID`);

--
-- Indexes for table `orders_services`
--
ALTER TABLE `orders_services`
  ADD PRIMARY KEY (`ID_Orders_Services`),
  ADD KEY `Orders_ID` (`Orders_ID`,`Services_ID`);

--
-- Indexes for table `services`
--
ALTER TABLE `services`
  ADD PRIMARY KEY (`ID_Services`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `clients`
--
ALTER TABLE `clients`
  MODIFY `ID_Clients` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `ID_Orders` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `orders_services`
--
ALTER TABLE `orders_services`
  MODIFY `ID_Orders_Services` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `services`
--
ALTER TABLE `services`
  MODIFY `ID_Services` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
