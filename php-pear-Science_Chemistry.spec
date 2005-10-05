%include	/usr/lib/rpm/macros.php
%define		_class		Science
%define		_subclass	Chemistry
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - manipulate chemical objects: atoms, molecules, etc
Summary(pl):	%{_pearname} - manipulacje na klasach obiektów chemicznych
Name:		php-pear-%{_pearname}
Version:	1.1.0
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6ee17eb8ac2b67b31bbf5e222739000c
URL:		http://pear.php.net/package/Science_Chemistry/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
General classes to represent Atoms, Molecules and Macromolecules. Also
parsing code for PDB, CML and XYZ file formats. Examples of parsing
and conversion to/from chemical structure formats.

In PEAR status of this package is: %{_status}.

%description -l pl
Ogólna klasa reprezentuj±ca atomy, moleku³y oraz makromoleku³y. Tak¿e
parsowanie kodu w formatach PDB, CML oraz XYZ. Zawiera w dokumentacji
przyk³ady parsowania oraz konwersji z/do formatów struktur
chemicznych.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

install -d ./%{php_pear_dir}/tests/%{_pearname}/data
mv ./%{php_pear_dir}/{%{_class}/%{_subclass}/test/*,tests/%{_pearname}}
mv ./%{php_pear_dir}/{data/%{_pearname}/%{_subclass}/test/*,tests/%{_pearname}/data}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/%{_subclass}/*
%dir %{php_pear_dir}/%{_class}/%{_subclass}/
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
