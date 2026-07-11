%global tl_name identkey
%global tl_revision 61719

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1.0
Release:	%{tl_revision}.1
Summary:	Typesetting bracketed dichotomous identification keys
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/identkey
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/identkey.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/identkey.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is for typesetting bracketed dichotomous identification
keys.

