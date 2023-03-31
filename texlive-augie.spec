Name:		texlive-augie
Version:	61719
Release:	2
Summary:	Calligraphic font for typesetting handwriting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/augie
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/augie.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/augie.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A calligraphic font for simulating American-style informal
handwriting. The font is distributed in Adobe Type 1 format.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/augie/augie___.afm
%{_texmfdistdir}/fonts/map/dvips/augie/augie.map
%{_texmfdistdir}/fonts/tfm/public/augie/augie7t.tfm
%{_texmfdistdir}/fonts/tfm/public/augie/augie8c.tfm
%{_texmfdistdir}/fonts/tfm/public/augie/augie8r.tfm
%{_texmfdistdir}/fonts/tfm/public/augie/augie8t.tfm
%{_texmfdistdir}/fonts/tfm/public/augie/augie___.tfm
%{_texmfdistdir}/fonts/type1/public/augie/augie___.pfb
%{_texmfdistdir}/fonts/vf/public/augie/augie7t.vf
%{_texmfdistdir}/fonts/vf/public/augie/augie8c.vf
%{_texmfdistdir}/fonts/vf/public/augie/augie8t.vf
%{_texmfdistdir}/tex/latex/augie/ot1augie.fd
%{_texmfdistdir}/tex/latex/augie/t1augie.fd
%{_texmfdistdir}/tex/latex/augie/ts1augie.fd
%doc %{_texmfdistdir}/doc/latex/augie/README.augie
%doc %{_texmfdistdir}/doc/latex/augie/augie.txt
%doc %{_texmfdistdir}/doc/latex/augie/other/Augie___.pfm
%doc %{_texmfdistdir}/doc/latex/augie/other/augie___.inf
%doc %{_texmfdistdir}/doc/latex/augie/vtex/augie.ali

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
