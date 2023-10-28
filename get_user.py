import pprint

import neo4j

from db import driver
from serializer import serialize_profile


def get_user(email: str):
    record = driver.execute_query(
        """
            MATCH (profile: Profile {email: $email}) RETURN profile
        """,
        email=email,
        result_transformer_=neo4j.Result.single,
    )

    if not record:
        return "Not Found"

    return serialize_profile(record["profile"])


email = input("Email: ")


pprint.pprint(
    get_user(email),
)
