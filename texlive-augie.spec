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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A calligraphic font for simulating American-style informal handwriting.
The font is distributed in Adobe Type 1 format.

