# Neo4j Python

## Setup Environments

This repository contains a `docker-compose.yml` file that facilitates the setup of a `neo4j` database. First of all, define environment variable on separate `.env` file.

```bash
cp .env.example .env
```

Now, Run docker compose command;

```bash
docker compose up
```

## 1. Seed Data

Let's populate the database with profile data. This file contains a set of profile data that will be used for seeding.

```bash
python3 seed.py
```

## 2. Get users

List all users,
```bash
python3 get_users.py
```

## 3. Get user by email

Get user by email address,
```bash
python3 get_user.py
```

Enter email to get user's details, for eg. `johndoe@example.com`

**Output Sample**
```
Email: johndoe@example.com 
{'address': 'Kathmandu, Nepal',
 'email': 'johndoe@example.com',
 'name': 'John Doe'}
```

