def serialize_profile(profile):
    return {
        "name": profile["name"],
        "email": profile["email"],
        "address": profile["address"],
    }
