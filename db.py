import os
from textwrap import dedent
from typing import LiteralString, cast

from neo4j import GraphDatabase, basic_auth

url = os.getenv("NEO4J_URI", "neo4j://localhost:7687")
username = os.getenv("NEO4J_USER", "neo4j")
password = os.getenv("NEO4J_PASS", "mysupersecretpassword")
database = "neo4j"

# driver
driver = GraphDatabase.driver(url, auth=basic_auth(username, password))


def query(q: LiteralString) -> LiteralString:
    # this is a safe transform:
    # no way for cypher injection by trimming whitespace
    # hence, we can safely cast to LiteralString
    return cast(LiteralString, dedent(q).strip())
