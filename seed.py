import neo4j

from db import database, driver


def seed_users():
    return driver.execute_query(
        """
    CREATE (John:Profile {name: "John Doe", email: "johndoe@example.com", address: "Kathmandu, Nepal"})
    CREATE (Joe:Profile {name: "Joe Doe", email: "joedoe@example.com", address: "Bhaktapur, Nepal"})
    CREATE (Jane:Profile {name: "jane Doe", email: "janedoe@example.com", address: "Lalitpur, Nepal"})
    CREATE (Ram:Profile {name: "Ram", email: "ram@example.com", address: "Janakpur, Nepal"})
    CREATE (Seeta:Profile {name: "Seeta", email: "seeta@example.com", address: "Janakpur, Nepal"})
    CREATE (Shyam:Profile {name: "Shyam", email: "shyam@example.com", address: "Janakpur, Nepal"})
    CREATE (Geeta:Profile {name: "Geeta", email: "geeta@example.com", address: "Palpa, Nepal"})
    CREATE (Prema:Profile {name: "Prema", email: "prema@example.com", address: "Butwal, Nepal"})
    CREATE (Prem:Profile {name: "Prem", email: "prem@example.com", address: "Tanahun, Nepal"})
    CREATE (Bipin:Profile {name: "Bipin", email: "bipin@example.com", address: "Jhapa, Nepal"})
    """,
        database_=database,
        result_transformer_=neo4j.Result.consume,
    )


summary = seed_users()

print("User Seeded = ", summary.counters.properties_set)
