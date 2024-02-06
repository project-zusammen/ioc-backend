# ioc-backend
This is the backend app for Indonesia Open Course Rest API using Python Flask

Ensure that you've accepted the invitation to become contributor of this repo.

To contribute:

1. Clone the repository
    ```bash
    git clone git@github.com:project-zusammen/ioc-backend.git
    ```

2. Checkout to a feature branch, add and commit your changes
    ```bash
    git checkout -b feat/short-desc-abt-the-feature
    ```

3. Push your feature branch
    ```bash
    git push origin feat/short-desc-abt-the-feature
    ```

4. Create a PR to the master branch

5. Run it with this code
    ```bash
    flask run
    ```

6. Run this code for Init the DB
    ```bash
    flask db init
    ```

7. Run this code for migrate the database
    ```bash
    flask db migrate
    ```

8. Run this code for upgrade the database after the migrate
    ```bash
    flask db upgrade
    ```

9. Copy .env-template and rename the copied file as .env, fill in the required credentials