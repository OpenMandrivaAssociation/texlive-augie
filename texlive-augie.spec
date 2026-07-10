%global tl_name augie
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Calligraphic font for typesetting handwriting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/augie
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/augie.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/augie.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A calligraphic font for simulating American-style informal handwriting.
The font is distributed in Adobe Type 1 format.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/fonts/afm
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/fonts/vf
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/augie
%dir %{_datadir}/texmf-dist/fonts/afm/public
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/fonts/type1/public
%dir %{_datadir}/texmf-dist/fonts/vf/public
%dir %{_datadir}/texmf-dist/tex/latex/augie
%dir %{_datadir}/texmf-dist/doc/latex/augie/other
%dir %{_datadir}/texmf-dist/doc/latex/augie/vtex
%dir %{_datadir}/texmf-dist/fonts/afm/public/augie
%dir %{_datadir}/texmf-dist/fonts/map/dvips/augie
%dir %{_datadir}/texmf-dist/fonts/tfm/public/augie
%dir %{_datadir}/texmf-dist/fonts/type1/public/augie
%dir %{_datadir}/texmf-dist/fonts/vf/public/augie
%doc %{_datadir}/texmf-dist/doc/latex/augie/README.augie
%doc %{_datadir}/texmf-dist/doc/latex/augie/augie.txt
%doc %{_datadir}/texmf-dist/doc/latex/augie/other/Augie___.pfm
%doc %{_datadir}/texmf-dist/doc/latex/augie/other/augie___.inf
%doc %{_datadir}/texmf-dist/doc/latex/augie/vtex/augie.ali
%{_datadir}/texmf-dist/fonts/afm/public/augie/augie___.afm
%{_datadir}/texmf-dist/fonts/map/dvips/augie/augie.map
%{_datadir}/texmf-dist/fonts/tfm/public/augie/augie7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/augie/augie8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/augie/augie8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/augie/augie8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/augie/augie___.tfm
%{_datadir}/texmf-dist/fonts/type1/public/augie/augie___.pfb
%{_datadir}/texmf-dist/fonts/vf/public/augie/augie7t.vf
%{_datadir}/texmf-dist/fonts/vf/public/augie/augie8c.vf
%{_datadir}/texmf-dist/fonts/vf/public/augie/augie8t.vf
%{_datadir}/texmf-dist/tex/latex/augie/ot1augie.fd
%{_datadir}/texmf-dist/tex/latex/augie/t1augie.fd
%{_datadir}/texmf-dist/tex/latex/augie/ts1augie.fd
