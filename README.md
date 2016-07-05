# clang-format based C++ formatting tools

This repository helps us keep our C++ source files in a uniform look on all our repositories. You might find this usefull too.

These achievements are due to clang-format, the backend for formatting of source code, based on Clang. We merely put files together in a git repository and wrote this README.

## How to use
The sequel assumes that you followed the installation steps bellow

- Apply formatting to staged files  
  Being in the git repository of one of your projects,

  ```shell
  git clang-format
  ```
- Apply formatting to complete repository

  ```shell
  git clang-format --commit `git hash-object -t tree /dev/null`
  ```

## Installing
The pre-requisite is to have clang-format installed. On ubuntu 16.04, you can install the package `clang-format`. At the time of writing (June 2016) the latest version is 3.8, on Ubuntu 16.04.

Check now that you can run `clang-format`. If it is not available with this name, try appending the verion number, for instance `clang-format-3.7`.

### Integrate clang-format in git
In your shell's configuration file, add the current repository to the path.

For Bash or Zsh:

```shell
export PATH=$PATH:/PATH/TO/format_code/
```

> **Note:** git-clang-format is released by LLVM. The latest version can be found at their [GitHub repository](https://github.com/llvm-mirror/clang/tree/master/tools/clang-format). It is distributed under the _University of Illinois Open Source License_.

### Telling git how to find clang-format
If you cannot run clang-fromat without specifying the version number, you'll also need to set a configuration entry in git. For instance, if you have clang-format 3.7:

```shell
git config --global clangFormat.binary clang-format-3.7
```

### Add the formatting convetion file
In our team we use the `.clang-format` convention in this repository. To have git-clang-format use it, we need to setup git config parameters:

```shell
git config --global clangFormat.style file
git config --global --path clangFormat.stylePath /PATH/TO/format_code
```

### Pre-commit hook (in EACH respository)
One might, by mistake, commit files that do not comply with the formatting convention. We can avoid this with a git hook, provided in this repository. To install, proceed as follow:

- give execution rights to the file  
  ```shell
  cd /PATH/TO/format_code
  chmod +x pre-commit
  ```
- install the hook  
  ```shell
  ln -s /PATH/TO/format_code/pre-commit /PATH/TO/YOUR/GIT/REPOSITORY/.git/hooks/
  ```

### Integrate with your favorite editor (optional)
To spare you the need to manually run the formatter script, you can use a plugin for your favorite source code editor:

- for Atom, install the plugin [clang-format](https://github.com/LiquidHelium/atom-clang-format)
- for Vim, Emacs, BBedit, Visual Studio, see the bottom of [this](http://clang.llvm.org/docs/ClangFormat.html) page

## More on clang-format
For more information on clang-format, please have a look at

- [Introduction to the clang tools](http://clang.llvm.org/docs/ClangTools.html)
- [Documentation on the program clang-format](http://clang.llvm.org/docs/ClangFormat.html)
- [clang format configurator](http://zed0.co.uk/clang-format-configurator/), that lets you see the effet of many clang-format's options.

## Contributing
Contributions for improvement or bug resolution are welcome, in the form of github issues or pull requests.

If you want, you can write a script to install the git hook on several git repositories, based on the above installation procedure.

## License
The software contained in the present repository is licensed under the (GNU GPL-compatible) CeCILL license. A copy can be found in `LICENSE`. `git-clang-format` is an exception, it is licensed under the the University of Illinois Open Source License, available in `LICENSE-clang-format`.

## Authors

- Authors/Maintainers: Dorian Goepp, Konstantinos Chatzilygeroudis
- Other contributors: Jean-Baptiste Mouret

This does not apply for git-clang-format.