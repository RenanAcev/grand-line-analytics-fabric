# 🏴‍☠️ Grand Line Analytics

An end-to-end analytics platform built with Microsoft Fabric using data from a public One Piece API.

## Project Overview

This project demonstrates how to build a modern analytics solution using Microsoft Fabric, following a Medallion Architecture (Bronze, Silver, Gold) and a dimensional Star Schema for reporting and analysis.

## Dashboard

![Dashboard](C:\Users\Renan\Downloads\db_op.png)

## Architecture

One Piece API → Bronze Layer → Silver Layer → Gold Layer → Star Schema → Semantic Model → Power BI

## Key Features

* REST API Data Ingestion
* Lakehouse Architecture
* Bronze, Silver & Gold Layers
* PySpark Transformations
* Delta Tables
* Dimensional Star Schema Modeling
* Semantic Model
* Interactive Power BI Dashboard
* GitHub Source Control Integration

## Data Model

Star Schema:

* dim_character
* dim_crew
* fact_character_bounty

## Business Questions

* Which pirate crews have the highest total bounty?
* Which characters have the highest bounties?
* What are the most common Devil Fruit types?
* How does crew size relate to total bounty?

## Technologies

* Microsoft Fabric
* Lakehouse
* OneLake
* PySpark
* SQL
* Delta Lake
* Power BI
* GitHub

## Future Improvements

* Data Pipelines
* Incremental Processing
* Data Quality Framework
* CI/CD & Deployment Pipelines
