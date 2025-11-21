# Semantic Release Setup Complete! 🚀

Your Discord bot project is now configured with automated semantic versioning and releases.

## What Was Set Up

### 1. **Configuration Files**

-   ✅ `pyproject.toml` - Semantic release configuration
-   ✅ `src/__version__.py` - Version tracking file
-   ✅ `requirements-dev.txt` - Development dependencies

### 2. **GitHub Actions Workflows**

-   ✅ `.github/workflows/semantic-release.yml` - Automated versioning and releases
-   ✅ `.github/workflows/release.yml` - Updated to work with semantic-release
-   ✅ `.github/workflows/validate-commits.yml` - PR commit validation

### 3. **Documentation**

-   ✅ `docs/SEMANTIC_RELEASE.md` - Complete usage guide
-   ✅ `.commit-examples` - Quick commit reference
-   ✅ `.github/pull_request_template.md` - PR template with commit guidelines
-   ✅ `README.md` - Updated with contribution guidelines

## Quick Start

### Making Your First Release

1. **Commit with conventional format:**

    ```bash
    git add .
    git commit -m "feat: initial semantic-release setup"
    ```

2. **Push to main:**

    ```bash
    git push origin main
    ```

3. **Automatic release happens:**
    - Version bumped to `0.1.0` (initial feature)
    - `CHANGELOG.md` created
    - Git tag `v0.1.0` created
    - GitHub Release published
    - Docker image built and pushed

### Commit Message Examples

```bash
# Feature - Minor version bump (0.X.0)
git commit -m "feat(music): add shuffle command"

# Bug fix - Patch version bump (0.0.X)
git commit -m "fix(queue): prevent duplicate songs"

# Breaking change - Major version bump (X.0.0)
git commit -m "feat!: upgrade to discord.py 3.0"

# No release
git commit -m "docs: update installation guide"
git commit -m "chore: update dependencies"
```

## Required GitHub Secrets

Make sure these are configured in your repository settings:

1. **GITHUB_TOKEN** - ✅ Automatically provided by GitHub Actions
2. **DOCKER_USERNAME** - Your Docker Hub username
3. **DOCKER_PASSWORD** - Your Docker Hub password/token

## Workflow Overview

```
┌─────────────────────────────────────────────────┐
│  Developer commits to main with conventional    │
│  commit message (e.g., "feat: add feature")     │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│  semantic-release.yml workflow triggers         │
│  1. Analyzes commits                            │
│  2. Determines version (0.1.0 → 0.2.0)          │
│  3. Updates pyproject.toml & __version__.py     │
│  4. Generates CHANGELOG.md entry                │
│  5. Creates git tag (v0.2.0)                    │
│  6. Creates GitHub Release                      │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│  release.yml workflow triggers on tag           │
│  1. Builds Docker image                         │
│  2. Pushes to Docker Hub                        │
│  3. Tags: v0.2.0 and latest                     │
│  4. Updates GitHub Release with Docker info     │
└─────────────────────────────────────────────────┘
```

## Testing Locally

Install development dependencies:

```bash
pip install -e ".[dev,test]"
```

Preview next version (dry-run):

```bash
semantic-release version --print
```

Generate changelog:

```bash
semantic-release changelog
```

## Common Scenarios

### Scenario 1: Bug Fix Release

```bash
git commit -m "fix(ytdl): handle rate limiting errors"
git push origin main
# Result: 1.2.3 → 1.2.4
```

### Scenario 2: New Feature

```bash
git commit -m "feat(commands): add search history"
git push origin main
# Result: 1.2.4 → 1.3.0
```

### Scenario 3: Breaking Change

```bash
git commit -m "feat!: change command prefix from . to !"
git push origin main
# Result: 1.3.0 → 2.0.0
```

### Scenario 4: Multiple Commits

```bash
git commit -m "docs: update README"
git commit -m "fix: memory leak in queue"
git commit -m "feat: add playlist support"
git push origin main
# Result: Bumps to next minor (feat takes precedence)
```

## Pull Request Flow

1. Create feature branch
2. Make changes
3. Commit with conventional format
4. Open PR (title must follow conventional commits)
5. `validate-commits.yml` checks PR title
6. Merge to main
7. Semantic release triggers automatically

## Version History

Check version history:

```bash
git tag -l
semantic-release changelog
cat CHANGELOG.md
```

## Troubleshooting

### Release didn't trigger

-   Check commit message follows convention
-   Ensure pushed to `main` branch
-   Verify commit type triggers release (`feat`, `fix`, `perf`)

### Wrong version number

-   Review commit types (feat=minor, fix=patch, breaking=major)
-   Check CHANGELOG.md for version history

### Docker build failed

-   Verify Docker Hub credentials in GitHub Secrets
-   Check Actions logs for build errors

## Next Steps

1. **Make a test commit** to verify the workflow
2. **Review generated CHANGELOG.md** after first release
3. **Update team** on new commit message conventions
4. **Add branch protection** to main requiring PR reviews

## Resources

-   📚 [Full Documentation](docs/SEMANTIC_RELEASE.md)
-   💬 [Conventional Commits](https://www.conventionalcommits.org/)
-   🔧 [Python Semantic Release](https://python-semantic-release.readthedocs.io/)
-   📦 [Semantic Versioning](https://semver.org/)

---

**Ready to release!** Just commit and push to main using conventional commit format. 🎉
