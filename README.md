# Python Unit Testing and Coverage Examples

### Provides some examples of python unit testing and test coverage

### Requires:
* Make
* Python 3

### Usage: 

```shell
make init # initialize the pip requirements
make lint # show python lint errors
make test # run both lint and unit tests
```

### Create a virtual environment
```shell

# create
virtualenv ~/venv/your_project

# activate
source ~/venv/your_project/bin/activate

# deactivate
deactivate

# delete
rm -rf ~/venv/your_project
```

### CI (e.g. Jenkins)

The Jenkins server would run:
``` make test ```
