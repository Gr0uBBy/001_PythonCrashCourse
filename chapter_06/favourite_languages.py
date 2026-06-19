favoutite_languages = {
    "john": ["c", "python"],
    "sarah": ["ruby"],
    "emanuel": ["php", "java"],
    "patric": [],
    "daniel": ["c++", "c", "bash"],
    "wojtek": ["assembler"],
}

for name, language in favoutite_languages.items():
    if len(language) == 0:
        print(f"{name.title()} has no favourite programing language.")
    elif len(language) == 1:
        print(f"{name.title()} has one favourite programing language - {language[0]}.")
    elif len(language) > 1:
        print(f"{name.title()} have {len(language)} favourite programing languages:")
        for i in language:
            print(f"\t{i}")
    # print(f"Name: {name} language: {language} and amount: {len(language)}")
