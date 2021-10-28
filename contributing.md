# Contributing to Generlate

Hey! :wave:      

So - you want to contribute huh?...  
Well, THANK YOU. Generlate is making architectural design easier and any help is greatly appreciated!
  



## Code of Conduct

This project and everyone participating in it is governed by the Generlate [Code of Conduct](https://github.com/Generlate/Generlate/blob/main/CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to austencabret@Generlate.com.

## What should I know before getting started?

### Generlate Structure

To get a sense for the files that are included with Generlate, you can go to Generlate Core's default branch on the GitHub page and take a look around.


## How Can I Contribute?

When suggesting changes, please include as many details as possible. 
Generlate Core's default branch is intentionally a stable release, so that anyone downloading the code and compiling it gets a stable release. Active development occurs on branches named after the version they are targeting, for example the 1.0.0 branch is named `1.0.0-dev.` When raising PRs, please raise against the relevant development branch and __not__ against the `master` branch

The codebase is maintained using the "contributor workflow" where everyone without exception contributes patch proposals using "pull requests". This facilitates social contribution, easy testing and peer review.

To contribute a patch, the workflow is as follows:

* Fork the repository in GitHub, and clone it your development machine.
* Create a topic branch from the relevant development branch.
* Commit changes to the branch.
* Test your changes, which must include the unit and RPC tests passing.
* Push topic branch to your copy of the repository.
* Raise a Pull Request via GitHub.

Commit messages should be verbose by default consisting of a short subject line (50 chars max), a blank line and detailed explanatory text as separate paragraph(s); unless the title alone is self-explanatory (like "Corrected typo in init.cpp") then a single title line is sufficient. Commit messages should be helpful to people reading your code in the future, so explain the reasoning for your decisions. 

Please refer to the [Git manual](https://git-scm.com/doc) for more information about Git.

The body of the pull request should contain enough description about what the patch does together with any justification/reasoning. You should include references to any discussions (for example other tickets or mailing list discussions). At this stage one should expect comments and review from other contributors. You can add more commits to your pull request by committing them locally and pushing to your fork until you have satisfied feedback.

If your pull request is accepted for merging, you may be asked by a maintainer to squash and or rebase your commits before it will be merged.

Please refrain from creating several pull requests for the same change. Use the pull request that is already open (or was created earlier) to amend changes. This preserves the discussion and review that happened earlier for the respective change set.

The length of time required for peer review is unpredictable and will vary between pull requests.

## Pull Request Philosophy

Pull Requests should always be focused. For example, a pull request could add a feature, fix a bug, or refactor code; but not a mixture. Please avoid submitting pull requests that attempt to do too much, are overly large, or overly complex as this makes review difficult.

### Features

When adding a new feature, thought must be given to the long term technical debt and maintenance that feature may require after inclusion. Before proposing a new feature that will require maintenance, please consider if you are willing to maintain it (including bug fixing). If features get orphaned with no maintainer in the future, they may be removed.

## "Decision Making" Process

Whether a pull request is merged into Generlate Core rests with the repository maintainers.

Maintainers will take into consideration if a patch is in line with the general principles of Generlate; meets the minimum standards for inclusion; and will take into account the consensus among frequent contributors.

In general, all pull requests must:

* have a clear use case, fix a demonstrable bug or serve the greater good of Generlate;
* be peer reviewed;
* have functional tests;
* follow code style guidelines;



### Peer Review

Anyone may participate in peer review which is expressed by comments in the pull request. Typically reviewers will review the code for obvious errors, as well as test out the patch set and opine on the technical merits of the patch. Repository maintainers take into account the peer review when determining if there is consensus to merge a pull request.

Maintainers reserve the right to weigh the opinions of peer reviewers using common sense judgement and also may weight based on meritocracy: Those that have demonstrated a deeper commitment and understanding towards Generlate (over time) or have clear domain expertise may naturally have more weight, as one would expect in all walks of life.


# Copyright
By contributing to this repository, you agree to license your work under the [Apach-2.0 license](https://github.com/Generlate/Generlate/blob/main/License), unless specified otherwise. Any work contributed where you are not the original author must contain its license header with the original author(s) and source.



## Styleguides



### Git Commit Messages

### JavaScript StyleGuide

### CoffeeScript Styleguide

### Specs Styleguide

### Documentation Styleguide

## Additional Notes

### Issues and Pull Request Labels
