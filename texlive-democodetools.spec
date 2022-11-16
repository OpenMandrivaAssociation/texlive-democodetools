Name:		texlive-democodetools
Version:	64314
Release:	1
Summary:	Package for LaTeX code documentation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/democodetools
License:	lppl1.3c gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/democodetools.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/democodetools.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is 'yet another doc/docx/doc3' package for LaTeX code
documentation.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/democodetools
%doc %{_texmfdistdir}/doc/latex/democodetools

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
