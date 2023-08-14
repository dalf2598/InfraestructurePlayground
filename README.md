# InfraestructurePlayground

[![codecov](https://codecov.io/github/dalf2598/InfraestructurePlayground/branch/main/graph/badge.svg?token=5C102BNOTP)](https://codecov.io/github/dalf2598/InfraestructurePlayground)

## Commit messages format

Below there are some common examples you can use for your commit messages:

- **feat**: A new feature.
- **fix**: A bug fix.
- **refactor**: A code change that neither fixes a bug nor adds a feature.
- **test**: Adding missing tests or correcting existing tests.
- **ci**: Changes to our CI or CD configuration files and scripts (example scopes: Azure devops, github actions).
- **docs**: Documentation only changes.

### Example
```shell
fix: orders can now be placed
```
## Branch names format

For your branch name you can follow the next format:

<p align="center"><b>{work-type}/{trello-ticket-name}</b></p>

For the `work-type` we have the next types:

- **bug**: Code changes to fix a known bug.
- **feature**: Development of a new feature.
- **test**: Code changes related to tests.
- **hotfix**: Quick fix for a critical bug.

### Example:

```shell
bug/PIZ1-I-cannot-create-an-order
```
## Pull-request names format
For your PR only use the trello ticket name 

### Example:

```shell
PIZ1: I cannot create an order
```
