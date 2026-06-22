def build_user_profile(first_name, last_name, **user_info):
    user_info["first_name"] = first_name
    user_info["last_name"] = last_name

    return user_info


user_profile = build_user_profile(
    "albert", "einstein", location="princeton", field="physics"
)

print(user_profile)
