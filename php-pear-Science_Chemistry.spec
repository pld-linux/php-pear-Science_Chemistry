%define		status		stable
%define		pearname	Science_Chemistry
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - manipulate chemical objects: atoms, molecules, etc
Summary(pl.UTF-8):	%{pearname} - manipulacje na klasach obiektów chemicznych
Name:		php-pear-%{pearname}
Version:	1.1.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	e23e312408aea67b3a778289e72877e4
URL:		http://pear.php.net/package/Science_Chemistry/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear
Obsoletes:	php-pear-Science_Chemistry-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
General classes to represent Atoms, Molecules and Macromolecules. Also
parsing code for PDB, CML and XYZ file formats. Examples of parsing
and conversion to/from chemical structure formats.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Ogólna klasa reprezentująca atomy, molekuły oraz makromolekuły. Także
parsowanie kodu w formatach PDB, CML oraz XYZ. Zawiera w dokumentacji
przykłady parsowania oraz konwersji z/do formatów struktur
chemicznych.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

install -d docs
mv .%{php_pear_dir}/data/Science_Chemistry/{README.md,TODO} docs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Science/Chemistry.php
%{php_pear_dir}/Science/Chemistry
