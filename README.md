# AirBnB Clone - The Console

## Description

The AirBnB clone is a simple command-line interpreter that allows users to manage objects like `User`, `State`, `City`, etc., for the AirBnB application. It implements the creation, retrieval, update, and destruction of these objects using the command interpreter.

## How to use it

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/Ivy-Joy5/AirBnB_clone.git
    ```

2. Navigate to the project directory:
    ```bash
    cd AirBnB_clone
    ```

3. Run the command interpreter:
    ```bash
    ./console.py
    ```

4. You will be presented with a prompt `(hbnb)`, where you can enter commands.

5. To exit the command interpreter, type `quit` or `EOF`.

---

## Examples

- **Create a new object (e.g., User)**
    ```bash
    (hbnb) create User
    ```

- **Show an object (e.g., User)**
    ```bash
    (hbnb) show User <object_id>
    ```

- **Update an object (e.g., User)**
    ```bash
    (hbnb) update User <object_id> name "John Doe"
    ```

- **Destroy an object (e.g., User)**
    ```bash
    (hbnb) destroy User <object_id>
    ```

- **Count the number of `User` objects**
    ```bash
    (hbnb) count User
    ```

### Example Session:

```bash
$ ./console.py
(hbnb) create User
12345678-90ab-cdef-ghij-klmnopqrstuv
(hbnb) show User 12345678-90ab-cdef-ghij-klmnopqrstuv
[User] (12345678-90ab-cdef-ghij-klmnopqrstuv) {'id': '12345678-90ab-cdef-ghij-klmnopqrstuv', 'name': 'John Doe'}
(hbnb) update User 12345678-90ab-cdef-ghij-klmnopqrstuv name "Jane Doe"
(hbnb) show User 12345678-90ab-cdef-ghij-klmnopqrstuv
[User] (12345678-90ab-cdef-ghij-klmnopqrstuv) {'id': '12345678-90ab-cdef-ghij-klmnopqrstuv', 'name': 'Jane Doe'}
(hbnb) quit
$

