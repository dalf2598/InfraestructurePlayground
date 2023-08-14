## Commit messages format

Below there are some common examples you can use for your commit messages:

- **feat**: A new feature.
- **fix**: A bug fix.
- **perf**: A code change that improves performance.
- **ci**: Changes to our CI or CD configuration files and scripts (example scopes: Azure devops, github actions).
- **docs**: Documentation only changes.
- **refactor**: A code change that neither fixes a bug nor adds a feature.
- **style**: Changes that do not affect the meaning of the code (typos, white-space, formatting, missing semi-colons, etc).
  It is important to mention that this key is not related to css styles.
- **test**: Adding missing tests or correcting existing tests.

### Example

    fix: orders can now be placed

## Branch names format

For your branch name you can follow the next format:

```shell
  {work type}/{trello ticket name}
```
For the `work type` we have the next types:

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