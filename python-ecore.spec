#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/BINDINGS/python/python-ecore python-ecore; \
#cd python-ecore; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#v_maj=$(cat configure.ac | grep 'm4_define(\[v_maj\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_min=$(cat configure.ac | grep 'm4_define(\[v_min\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_mic=$(cat configure.ac | grep 'm4_define(\[v_mic\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#PKG_VERSION=$v_maj.$v_min.$v_mic.$SVNREV; \
#cd ..; \
#tar -Jcf python-ecore-$PKG_VERSION.tar.xz python-ecore/ --exclude .svn --exclude .*ignore

%define svnrev  65723

Summary:	Ecore bindings for Python 
Name:		python-ecore
Version:	0.7.3
Release:	0.%{svnrev}.1
Source0:	%{name}-%{version}.%{svnrev}.tar.xz
License:	GPLv2
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/

BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(eina)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(python-evas)
BuildRequires:	python-cython
%py_requires -d

%description
Python support files for Ecore

%package devel
Summary:    Development files for %{name}
Group:      Development/Python

%description devel
Development files for the Python wrapper for the Ecore libraries.

%prep
%setup -qn %{name}

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%doc README
%{py_platsitedir}/ecore/*

%files devel
%{_includedir}/python*/ecore/*
%{_datadir}/%{name}/*
%{_libdir}/pkgconfig/*.pc

