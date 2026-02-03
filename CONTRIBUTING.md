# Contributing

Agreed upon by Sarisha Das, Sarah Gauthier, Yuheng Ouyang and Harry Yau.

Contributions of all kinds are welcome here, and they are greatly appreciated!
Every little bit helps, and credit will always be given.

## Example Contributions

You can contribute in many ways, for example:

- [Report bugs](#report-bugs)
- [Fix Bugs](#fix-bugs)
- [Implement Features](#implement-features)
- [Write Documentation](#write-documentation)
- [Submit Feedback](#submit-feedback)

### Report Bugs

Report bugs at <https://github.com/UBC-MDS/wordguess/issues>.

**If you are reporting a bug, please follow the template guidelines. The more
detailed your report, the easier and thus faster we can help you.**

### Fix Bugs

Look through the GitHub issues for bugs. Anything labelled with `bug` and
`help wanted` is open to whoever wants to implement it. When you decide to work on such
an issue, please assign yourself to it and add a comment that you'll be working on that,
too. If you see another issue without the `help wanted` label, just post a comment, the
maintainers are usually happy for any support that they can get.

### Implement Features

Look through the GitHub issues for features. Anything labelled with
`enhancement` and `help wanted` is open to whoever wants to implement it. As
for [fixing bugs](#fix-bugs), please assign yourself to the issue and add a comment that
you'll be working on that, too. If another enhancement catches your fancy, but it
doesn't have the `help wanted` label, just post a comment, the maintainers are usually
happy for any support that they can get.

### Write Documentation

wordguess could always use more documentation, whether as
part of the official documentation, in docstrings, or even on the web in blog
posts, articles, and such. Just
[open an issue](https://github.com/UBC-MDS/wordguess/issues)
to let us know what you will be working on so that we can provide you with guidance.

### Submit Feedback

The best way to send feedback is to file an issue at
<https://github.com/UBC-MDS/wordguess/issues>. If your feedback fits the format of one of
the issue templates, please use that. Remember that this is a volunteer-driven
project and everybody has limited time.

## Get Started

Ready to contribute? Here's how to set up wordguess for
local development.

1. Fork the <https://github.com/UBC-MDS/wordguess>
   repository on GitHub.
2. Clone your fork locally (*if you want to work locally*)

    ```shell
    git clone git@github.com:your_name_here/wordguess.git
    ```

3. [Install hatch](https://hatch.pypa.io/latest/install/).

4. Create a branch for local development using the default branch (typically `main`) as a starting point. Use `fix` or `feat` as a prefix for your branch name.

    ```shell
    git checkout main
    git checkout -b fix-name-of-your-bugfix
    ```

    Now you can make your changes locally.

5. When you're done making changes, apply the quality assurance tools and check
   that your changes pass our test suite. This is all included with tox

    ```shell
    hatch run test:run
    ```

6. Commit your changes and push your branch to GitHub. Please use [semantic
   commit messages](https://www.conventionalcommits.org/).

    ```shell
    git add .
    git commit -m "fix: summarize your changes"
    git push -u origin fix-name-of-your-bugfix
    ```

7. Open the link displayed in the message when pushing your new branch in order
   to submit a pull request.

### Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put your
   new functionality into a function with a docstring.
3. Your pull request will automatically be checked by the full test suite.
   It needs to pass all of them before it can be considered for merging.

### Code Style

Your suggested code should follow [PEP 8](https://pep8.org/) Python style guide. We recommend [Ruff](https://docs.astral.sh/ruff/) for automatic code formatting and linting. Use straightforward variable names and keep functions focused on one single task. Docstrings need to be documented under all functions and classes definitions using [NumPy style](https://peps.python.org/pep-0008/#documentation-strings).

## Development Tools and Infrastructure

This section documents the development tools, GitHub infrastructure, and organizational practices applied in this project, as well as considerations for scaling up similar projects.

### Tools Used in This Project

#### Package Management and Build Tools
- **Hatch**: Modern Python project manager for building, versioning, and environment management
  - Simplifies dependency management and virtual environment creation
  - Provides consistent build and test workflows on deploying package

#### Code Quality and Testing
- **pytest**: Testing framework for writing and running unit tests
  - Comprehensive test coverage in `tests/` directory
  - Enables test-driven development practices

#### Documentation
- **Quarto**: Scientific and technical publishing system
  - Generates project documentation from markdown and code
  - Integrates narrative text with executable code examples
- **NumPy-style docstrings**: Standard documentation format
  - Provides clear, structured documentation for all functions
  - Enables automatic documentation generation

#### Version Control
- **Git**: Distributed version control system
- **GitHub**: Cloud-based repository hosting and collaboration platform

### GitHub Infrastructure

Our project leverages several GitHub features for collaboration and automation:

#### Repository Organization
- **Branching Strategy**: Feature branch workflow
  - `main` branch for stable code
  - `otter` branch as our dev branch to integrate features, bug fixes, and changes before they are ready for production
  - Pull requests required for merging to main

#### Collaboration at Scale
- **Branch Protection Rules**: Require reviews and passing tests
  - Prevent direct pushes to main
  - Require status checks to pass
  - Enforce code owner reviews for critical files

#### Issue Tracking
- **GitHub Projects**: Kanban boards for task tracking
  - Sprint planning and backlog management
  - Roadmap visualization
  - Allow tracking issues, pull requests, and ideas across customizable columns
- **Issue Templates**: Standardized formats for bug reports and feature requests
  - Ensures comprehensive information collection
  - Streamlines triage and prioritization

#### Pull Request Workflow
- **Pull Request Templates**: Guide contributors through necessary information
- **Code Review**: Peer review process before merging
- **Automated Checks**: CI/CD integration validates code quality

#### Project Documentation
- **README.md**: Project overview, installation, and usage instructions
- **CONTRIBUTING.md**: Contribution guidelines and development setup
- **CODE_OF_CONDUCT.md**: Community standards and expectations
- **LICENSE**: MIT License for open-source distribution

### Organizational Practices

#### Development Workflow
1. **Issue-Driven Development**: All changes start with an issue
2. **Test-Driven Development**: Write tests before implementing features
3. **Code Review**: All changes reviewed by at least one team member

#### Team Collaboration
- **Clear Ownership**: Issues assigned to specific team members
- **Communication**: GitHub issues and pull requests for async collaboration
- **Documentation**: Comprehensive inline comments and docstrings
- **Consistency**: Shared code style and formatting standards

#### Quality Assurance
- **Type Hints**: Python type annotations throughout codebase
- **Unit Tests**: Comprehensive test coverage in `tests/unit/`
- **Manual Testing**: Verification of functionality before merging

### Scaling Up: Tools and Practices for Larger Projects

If scaling this or similar projects, we would implement the following additional tools and practices:

#### Continuous Integration/Continuous Deployment (CI/CD)
- **GitHub Actions**: Automate testing, building, and deployment
  - Run test suite on every push and pull request
  - Automated code quality checks (linting, type checking)
  - Automatic package building and publishing to PyPI
  - Documentation deployment to GitHub Pages or Read the Docs
- **Pre-commit Hooks**: Enforce code quality locally before commits
  - Check for large files, merge conflicts, and trailing whitespace

#### Enhanced Testing
- **pytest-cov**: Code coverage reporting
  - Track test coverage percentage
  - Identify untested code paths
- **pytest-benchmark**: Performance testing
  - Ensure functions maintain acceptable performance
- **Hypothesis**: Property-based testing
  - Generate edge cases automatically
  - More robust validation of function behavior
- **Integration Tests**: Test component interactions
- **End-to-End Tests**: Validate complete workflows

#### Dependency Management
- **Dependabot**: Automated dependency updates
  - Security vulnerability notifications
  - Automatic pull requests for updates
- **Safety/Bandit**: Security scanning for vulnerabilities
- **Lock Files**: Pin exact dependency versions for reproducibility

#### Code Quality Tools
- **MyPy**: Static type checking
  - Catch type errors before runtime
  - Improve code reliability
- **Coverage Requirements**: Enforce minimum coverage thresholds
- **SonarQube/CodeClimate**: Advanced code quality metrics
  - Code complexity analysis
  - Maintainability scoring
  - Security hotspot detection

#### Project Management
- **Issue Automation**: Automated labeling and triage
- **Release Management**: Semantic versioning with automated releases

#### Monitoring and Analytics
- **PyPI Statistics**: Track package downloads and usage
- **Error Tracking**: Sentry or similar for runtime error monitoring
- **User Feedback**: Issue templates for user-reported bugs and features

#### Security
- **Security Policy**: SECURITY.md with vulnerability reporting process
- **Code Scanning**: GitHub Advanced Security features
- **Secret Scanning**: Prevent credential leakage

### Conclusion
The tools and practices applied in this project establish a solid foundation for collaborative open-source development. For larger-scale projects, the additional infrastructure focuses on automation, quality assurance, and enabling distributed teams to work effectively. The key principle is to automate routine tasks, enforce quality standards early in the development process, and maintain clear documentation and communication channels.

## Code of Conduct

Please not that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.
