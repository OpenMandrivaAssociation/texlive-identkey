Name:		texlive-identkey
Version:	61719
Release:	2
Summary:	Typesetting bracketed dichotomous identification keys
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/identkey
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/identkey.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/identkey.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is for typesetting bracketed dichotomous
identification keys.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/identkey
%doc %{_texmfdistdir}/doc/latex/identkey

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
