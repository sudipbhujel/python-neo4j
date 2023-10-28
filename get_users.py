import pprint

from db import driver
from serializer import serialize_profile


def get_users():
    records, _, _ = driver.execute_query(
        """
            MATCH (profile: Profile) RETURN profile
        """,
    )

    return [serialize_profile(record["profile"]) for record in records]


pprint.pprint(get_users())
