import sqlite3

def get_person_and_pets(person_id):
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()

    cursor.execute('SELECT first_name, last_name, age FROM person WHERE id = ?', (person_id,))
    person = cursor.fetchone()

    if person:
        print(f"{person[0]} {person[1]}, {person[2]} years old")

        cursor.execute('''
            SELECT pet.name, pet.breed, pet.age, pet.dead
            FROM pet
            JOIN person_pet ON pet.id = person_pet.pet_id
            WHERE person_pet.person_id = ?
        ''', (person_id,))

        pets = cursor.fetchall()

        for pet in pets:
            status = "that is no longer alive" if pet[3] == 1 else "that is still alive"
            print(f"  - Owned {pet[0]}, a {pet[1]}, that was {pet[2]} years old, {status}.")
    else:
        print("Person not found.")

    conn.close()

def main():
    while True:
        try:
            person_id = int(input("Enter person ID (-1 to exit): "))
            if person_id == -1:
                break
            get_person_and_pets(person_id)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    print("Running query_pets.py")
    main()
