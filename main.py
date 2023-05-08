import yaml

def load_config():
    with open("config.yaml", "r") as file:
        con_fig = yaml.safe_load(file)
    return con_fig
print(load_config())