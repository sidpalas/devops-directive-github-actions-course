The docs say to check in node_modules https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-javascript-action#commit-tag-and-push-your-action

Alternatively, you can use:

- NCC https://github.com/vercel/ncc

OR

- Rollup https://github.com/actions/hello-world-javascript-action/blob/main/rollup.config.js

but that adds a build step.

Here is a template repo that implemented with rollup https://github.com/actions/hello-world-javascript-action

Honestly you should be using Typescript anyways... so that requires a builds step (and avoids the need to check in node_modules)
