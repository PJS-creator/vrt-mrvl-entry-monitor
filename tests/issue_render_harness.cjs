// Exercise the checked-in Issue script with fake files and a fake GitHub API.
const fs = require('node:fs');
const input = JSON.parse(fs.readFileSync(0, 'utf8'));
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;
const render = new AsyncFunction('require', 'context', 'process', 'github', input.script);
let issue;
const fakeRequire = (name) => {
  if (name !== 'fs') throw new Error(`Unexpected module: ${name}`);
  return { readFileSync: (path) => {
    if (!(path in input.files)) throw new Error('missing fixture');
    return input.files[path];
  } };
};
const context = { repo: { owner: 'test-owner', repo: 'test-repo' }, actor: 'test-owner', runId: 1 };
const processStub = { env: { N1_VALID: String(input.valid), JOB_STATUS: 'success', GITHUB_SERVER_URL: 'https://github.test' } };
const github = { rest: { issues: { create: async (data) => { issue = data; } } } };
render(fakeRequire, context, processStub, github).then(() => {
  process.stdout.write(JSON.stringify(issue));
}).catch((error) => {
  process.stderr.write(error.stack);
  process.exitCode = 1;
});
