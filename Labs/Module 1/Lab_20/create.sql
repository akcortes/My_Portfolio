CREATE DATABASE lab_mysql;
USE lab_mysql;
CREATE TABLE Cars (ID INT, VIN VARCHAR(255), Manufacturer TEXT, Model VARCHAR(255), Year INT, Color TEXT);
CREATE TABLE Customers (ID INT, Name TEXT, Manufacturer TEXT, Phone VARCHAR(255), Postal INT, City TEXT);
CREATE TABLE Salespersons (ID INT, StaffId INT, Name TEXT, Store VARCHAR(255));
CREATE TABLE Invoices (ID INT, InvoiceNumber INT, Date DATE, Car INT, Customer INT,SalesPerson INT);


