# First install homebrew for managing mac dependencies
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# Second, install super duper mode for mac keyboard
git clone https://github.com/jasonrudolph/keyboard.git ~/.keyboard
cd ~/.keyboard
script/setup
cd ..
### this installs karabiner-elements from https://pqrs.org/osx/karabiner/ 
### and hammerspoon https://github.com/Hammerspoon/hammerspoon

# Third, install keycastr
brew cask install keycastr

### See System Preferences > Security & Privacy > Privacy > Accessibility to enable Accessibility for hammerspoon and keycastr
### See System Preferences > Security & Privacy > General to allow apps from Fumihiko Takayama 

# Now you have awesome cap lock functionality and other sweet stuff described here: https://github.com/jasonrudolph/keyboard plus you have visual confirmation of what keys you pressed (keycastr)

#Install vmail
gem install vmail
# add .vimrc to home directory

# Install iterm2
brew cask install iterm2

# keep & access clipboard history
brew cask install flycut

# Install xcode before git
xcode-select --install
brew install git

# Install python with neovim client
brew install python
brew install python3
pip2 install neovim --upgrade
pip3 install neovim --upgrade

# Install neovim
brew install neovim

#Install zsh (according to https://justinzimmerman.net/post/switching-from-bash-to-zsh/)
brew install zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# more on zsh: http://zpalexander.com/switching-to-zsh/
# powerline9k: https://gist.github.com/kevin-smets/8568070

sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# Optional apps
brew cask install evernote
brew cask install alfred
brew cask install flux
brew cask install vlc
brew install tree
brew install wget
brew install tmux
brew install w3m
brew install django-completion
brew install brew-cask-completion
brew install bash-completion
# Install miniconda for managing python dependencies https://conda.io/miniconda.html
wget https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh && bash Miniconda-latest-MacOSX-x86_64.sh -b
brew install cmus
<<<<<<< HEAD

# install r and rstudio as per https://www.r-bloggers.com/install-r-and-python-via-homebrew/
brew cask install rstudio
brew install openblas
brew install r --with-openblas

=======
>>>>>>> 65ddcd03caaff218411af471b69ea531963fc2e4
brew install --HEAD https://raw.githubusercontent.com/jeffkowalski/geeknote/master/geeknote.rb
