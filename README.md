# Try pyramid_sacrud

### Required

- vagrant 1.8.3 or higher

### Usage

1. Start up vagrant VM

    ```shell
    $ vagrant up
    ```

2. Setup project's local vitualenv

    ```shell
    $ cd /vagrant/<project-dir>
    $ pyenv local pyramid-sacrud
    ```

3. Setup project require package

    ```shell
    $ cd /vagrant/<project-dir>
    $ pip install -e .
    $ initialize_<project-name>_db development.ini
    $ pserve development.init
    ```

4. Check from host machine

    open [http://localhost:6543](http://localhost:6543) in browser