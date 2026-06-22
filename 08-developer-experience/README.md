# Developer Experience

Repeatedly pushing workflows to GitHub in order to test them is a slow and frustrating experience.

Fortunately, there are ways we can iterate on actions and workflows locally to speed up the iteration loop.

## Actions

When developing actions, there are two main things we can do to validate locally.

### 1. Write/execute tests

We can write a test suite just like any other software project.

```bash
npm run test
# NODE_OPTIONS=--experimental-vm-modules NODE_NO_WARNINGS=1 npx jest
```
https://github.com/actions/typescript-action/blob/7a1ec05faaad7a2d54c398cfd8b9ef358e087cf8/package.json#L35


### 2. Run action with local-action

GitHub has published a tool for executing and debugging github actions locally. 

Repo: https://github.com/github/local-action

```bash
npm run local-action
# npx @github/local-action . src/main.ts .env
```
https://github.com/actions/typescript-action/blob/7a1ec05faaad7a2d54c398cfd8b9ef358e087cf8/package.json#L32

## Workflows

### 1. Move logic out of the workflow

Whenever possible, you should move logic out of the workflow yaml files.

My tool of choice for this is https://taskfile.dev/, but shell scripts or a simple custom CLI tool are also fine options.

The goal is to be able to test as much logic as possible independently of GitHub Actions.

Some logic will be very dependent on Git/GitHub related state, but many things can be written/executed separately.

### 2. Run workflow with act

Sometimes it is necessary to test things in the context of the workflow. 

There is a tool called act (https://github.com/nektos/act) which enables us to do this within containters.

We can mock specific GitHub events and pass necessary environment variables/secrets to test almost any GHA workflow:

```
act workflow_dispatch \
  --container-architecture linux/amd64 \
  -P ubuntu-24.04=node:16-bullseye-slim \
  -W '../.github/workflows/03-core-features--01-hello-world.yaml'
```

### 3. Set up breakpoints

Out of the box, the default GitHub hosted runners do not have a way to connect to the runner directly.

There are a few 3rd party solutions which can enable this type of behavior:

- [If using GitHub Hosted Runnerss)](https://github.com/mxschmitt/action-tmate)
- [If using https://namespace.so/](https://namespace.so/docs/reference/github-actions/breakpoint)
- [If using https://actuated.com/](https://github.com/self-actuated/connect-ssh)
- [If using http://blacksmith.sh/](https://docs.blacksmith.sh/blacksmith-observability/ssh-access)