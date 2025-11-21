# Semantic Release Guide

This project uses [Python Semantic Release](https://python-semantic-release.readthedocs.io/) to automate versioning, changelog generation, and releases.

> **📖 Quick Reference**: See [`.github/commit-instructions.md`](../.github/commit-instructions.md) for detailed conventional commit examples and format guide.

## How It Works

When you push commits to the `main` branch, the semantic-release workflow automatically:

1. **Analyzes commit messages** to determine the next version number
2. **Updates version** in `pyproject.toml` and `src/__version__.py`
3. **Generates/updates CHANGELOG.md** with all changes
4. **Creates a Git tag** (e.g., `v1.2.3`)
5. **Creates a GitHub Release** with release notes
6. **Triggers Docker image build** and push to Docker Hub

## Commit Message Convention

Use **Conventional Commits** format for all commit messages:

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Commit Types

| Type       | Description                           | Version Bump  |
| ---------- | ------------------------------------- | ------------- |
| `feat`     | New feature                           | Minor (0.X.0) |
| `fix`      | Bug fix                               | Patch (0.0.X) |
| `perf`     | Performance improvement               | Patch (0.0.X) |
| `docs`     | Documentation changes                 | None          |
| `style`    | Code style changes (formatting, etc.) | None          |
| `refactor` | Code refactoring                      | None          |
| `test`     | Adding/updating tests                 | None          |
| `build`    | Build system changes                  | None          |
| `ci`       | CI/CD changes                         | None          |
| `ops`      | Infrastructure/deployment changes     | None          |
| `chore`    | Other changes                         | None          |

### Breaking Changes

For **major version** bumps (X.0.0), add `BREAKING CHANGE:` in the footer or use `!` after type:

```bash
feat!: remove deprecated API endpoints

BREAKING CHANGE: The old v1 API has been removed. Use v2 instead.
```

### Examples

#### Feature (Minor Version Bump)

```bash
git commit -m "feat(music): add playlist support

Users can now queue entire YouTube playlists at once."
```

#### Bug Fix (Patch Version Bump)

```bash
git commit -m "fix(queue): resolve race condition in play_next

Fixes issue where queue would skip songs under high load."
```

#### Breaking Change (Major Version Bump)

```bash
git commit -m "feat!: upgrade to discord.py 3.0

BREAKING CHANGE: Requires Python 3.13+ and new bot intents configuration."
```

#### Documentation (No Version Bump)

```bash
git commit -m "docs: update README with new commands"
```

#### Chore (No Version Bump)

```bash
git commit -m "chore: update dependencies"
```

## Workflow Process

### 1. Normal Development Flow

```bash
# Make your changes
git add .

# Commit with conventional format
git commit -m "feat(music): add volume persistence"

# Push to main (or merge PR to main)
git push origin main
```

### 2. Semantic Release Workflow Triggers

The GitHub Actions workflow runs automatically and:

```bash
# Analyzes commits since last release
semantic-release version

# Updates version files
# Creates CHANGELOG.md entry
# Commits changes as "chore(release): X.Y.Z"
# Tags the release
# Pushes tag and commits

# Creates GitHub Release
semantic-release publish

# Triggers Docker build workflow
```

### 3. Docker Image Build

The `release.yml` workflow builds and pushes:

-   `ibfleming/zion-discord-bot:X.Y.Z`
-   `ibfleming/zion-discord-bot:latest`

## Release Types

### Automatic Release (Recommended)

Just push to main with conventional commits:

```bash
git commit -m "feat: add new feature"
git push origin main
# ✅ Automatic release triggered
```

### Manual Release (Not Recommended)

You can manually create a tag, but this bypasses changelog generation:

```bash
git tag v1.0.0
git push origin v1.0.0
# ⚠️ Only Docker build runs, no changelog
```

## Checking Version

### In Code

```python
from src.__version__ import __version__
print(__version__)  # e.g., "1.2.3"
```

### In Git

```bash
git describe --tags --abbrev=0  # Latest tag
```

### In pyproject.toml

```bash
grep version pyproject.toml
```

## Skipping Release

To commit to main without triggering a release, use a type that doesn't bump version:

```bash
git commit -m "docs: update installation guide"
git push origin main
# ✅ No release, CI tests still run
```

Or include `[skip ci]` in commit message:

```bash
git commit -m "chore: update README [skip ci]"
# ⚠️ Skips all CI including tests
```

## Troubleshooting

### Release Didn't Trigger

-   Check commit message follows convention
-   Ensure commit was pushed to `main` branch
-   Verify GitHub Actions workflow is enabled
-   Check for commits with types that trigger releases (`feat`, `fix`, `perf`)

### Wrong Version Number

-   Review recent commit messages
-   Ensure breaking changes use `!` or `BREAKING CHANGE:`
-   Remember: `feat` = minor, `fix` = patch, breaking = major

### Docker Build Failed

-   Check Docker Hub credentials in GitHub Secrets
-   Verify `DOCKER_USERNAME` and `DOCKER_PASSWORD` are set
-   Review build logs in Actions tab

## Configuration

Main configuration is in `pyproject.toml`:

```toml
[tool.semantic_release]
version_toml = ["pyproject.toml:project.version"]
version_variables = ["src/__version__.py:__version__"]
branch = "main"
upload_to_pypi = false
```

## Resources

-   [Conventional Commits](https://www.conventionalcommits.org/)
-   [Python Semantic Release Docs](https://python-semantic-release.readthedocs.io/)
-   [Semantic Versioning](https://semver.org/)
