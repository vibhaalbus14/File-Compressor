from pprint import pprint
#prettty-print:easier repr of complex data structures
list = [
    {
        "name": "Max",
        "breed": "Yorkshire",
        "age": 1,
        "owners": ["Susan, Camila, Paul"]
    },
    {
        "name": "Duke",
        "breed": "Bulldog",
        "age": 4,
        "owners": ["Thomas, David, Lucia"]
    },
    {
        "name": "Bella",
        "breed": "Poodle",
        "age": 2,
        "owners": ["Katharina, Arthur"]
    }
]

print("using print : ",list)
pprint("using pprint: ")
pprint(list)