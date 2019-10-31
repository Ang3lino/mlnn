#!/bin/bash

vi() {
	# Create required directory in case (optional)
	mkdir -p $(jupyter --data-dir)/nbextensions
	# Clone the repository
	cd $(jupyter --data-dir)/nbextensions
	git clone https://github.com/lambdalisue/jupyter-vim-binding vim_binding
	# Activate the extension
	jupyter nbextension enable vim_binding/vim_binding
}

theme() {
	# install jupyterthemes
	pip install jupyterthemes

	# upgrade to latest version
	pip install --upgrade jupyterthemes

	chrome https://github.com/dunovank/jupyter-themes

}


