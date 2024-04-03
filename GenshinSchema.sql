/*
GenshinSchema.sql
Author: Grace Bero

Description: This is an sql doc that creates 
my database, the 'Characters'and 'Weapons' tables, and 
adds 5 entries to each table

References: Used ChatGPT to help create this doc.
https://chat.openai.com/share/180c8072-0eee-4e50-8020-7a7bff859ce0
*/

-- Create the ProjectOneGenshin database
CREATE DATABASE IF NOT EXISTS ProjectOneGenshin;

-- Use the ProjectOneGenshin database
USE ProjectOneGenshin;

-- Create the Characters table
CREATE TABLE IF NOT EXISTS Characters (
    CName VARCHAR(100) PRIMARY KEY,
    Region VARCHAR(100),
    WeaponType VARCHAR(100),
    ReleaseVersion FLOAT
);

-- Create the Build table
CREATE TABLE IF NOT EXISTS Build (
    CName VARCHAR(100) PRIMARY KEY,
    Artifact VARCHAR(100),
    Weapon VARCHAR(100) 
);

--------------Populate the SQL Database -------------------------------------------

-- Insert characters
INSERT INTO Characters (CName, Region, WeaponType, ReleaseVersion)
VALUES ('Diluc', 'Mondstadt', 'Claymore', 1.0),
    ('Jean', 'Mondstadt', 'Sword', 1.0),
    ('Fischl', 'Mondstadt', 'Bow', 1.0),
    ('Keqing', 'Liyue', 'Sword', 1.1),
    ('Zhongli', 'Liyue', 'Polearm', 1.1)
    ('Ayaka', 'Inazuma', 'Sword', 2.0),
    ('Yoimiya', 'Inazuma', 'Bow', 2.0),
    ('Nahida', 'Sumeru', 'Catalyst', 3.2),
    ('Xingqiu', 'Liyue', 'Sword', 1.0),
    ('Collei', 'Sumeru', 'Bow', 3.0),
    ('Lyney', 'Fontaine', 'Bow', 4.0),
    ('Neuvillette', 'Fontaine', 'Catalyst', 4.1),
    ('Chevreuse', 'Fontaine', 'Polearm', 4.3);

-- Insert weapons
INSERT INTO Build (CName, Artifact, Weapon)
VALUES ('Diluc', 'Gladiators Finale', 'Wolfs Gravestone'),
    ('Jean', 'Viridescent', 'Aquila Favonia'),
    ('Fischl', 'Thundering', 'Stringless'),
    ('Keqing', 'Thundering', 'Mistsplitter'),
    ('Zhongli', 'Millelith', 'Black Tassel'),
    ('Ayaka', 'Blizzard', 'Mistsplitter'),
    ('Yoimiya', 'Shimenawa', 'Thundering Pulse'),
    ('Nahida', 'Deepwood', 'Sacrificial'),
    ('Xingqiu', 'Emblem', 'Sacrificial'),
    ('Collei', 'Deepwood', 'Favonius'),
    ('Lyney', 'Marechaussee', 'Aqua'),
    ('Neuvillette', 'Marechaussee', 'Lost Prayer'),
    ('Chevreuse', 'Song of Days Past', 'Black Tassel');
