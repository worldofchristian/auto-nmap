import pickle

emails = [
    ''
]

# export
with open("emails.pickle", "wb") as file:
    pickle.dump(emails, file)