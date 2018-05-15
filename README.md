# Python File Structure/Unit Testing and Coverage Examples

### Provides some examples of python project structure, unit testing, and coverage reports

### Requires:
* Make
* Python 3

### Usage: 

Init will create a virtual environment for the testing.

```shell
make init # initialize the pip requirements
make lint # show python lint errors
make test # run both lint and unit tests
```

### CI (e.g. Jenkins)

The Jenkins server would run:
``` make test ```
