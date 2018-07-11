set nocompatible

set tabstop=4
set shiftwidth=4
set softtabstop=4
set noexpandtab
set et
set autochdir
set exrc
set secure
set clipboard=unnamed

set showmatch
set hlsearch
set incsearch
set ignorecase
let &path.="include,/usr/include/AL,"
let g:ycm_global_ycm_extra_conf = "~/.vim/.ycm_extra_conf.py"
let g:ycm_complete_in_comments=1
let g:ycm_confirm_extra_conf=0
let g:ycm_collect_identifiers_from_tags_files=1
set completeopt-=preview
let g:ycm_min_num_of_chars_for_completion=1
let g:ycm_cache_omnifunc=0
let g:ycm_seed_identifiers_with_syntax=1
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'scrooloose/nerdtree'
Plugin 'jlanzarotta/bufexplorer'
Plugin 'Valloric/YouCompleteMe'

call vundle#end() 
           
filetype plugin indent on
autocmd VimEnter * NERDTree
