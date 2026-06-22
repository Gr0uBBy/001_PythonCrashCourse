# unprinted_designs = ["phone case", "Thor's hammer", "King Kong"]
# printed_designs = []

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Currently printing: {current_design}...")
#     printed_designs.append(current_design)

# for design in printed_designs:
#     print(f"3D printing of {design} is complete.")


def models_to_be_printed(unprinted_models, completed_models):
    while unprinted_models:
        current_model = unprinted_models.pop()
        print(f"Currently printing: {current_model}. Please wait.")
        completed_models.append(current_model)


def show_completed_models(completed_models):
    print("Below you can find a list of all completed models.")
    for model in completed_models:
        print(model)


unprinted_designs = ["phone case", "Thor's hammer", "King Kong"]
completed_models = []

models_to_be_printed(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

print(unprinted_designs)
print(completed_models)
