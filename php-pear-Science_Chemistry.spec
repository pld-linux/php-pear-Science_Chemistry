%include	/usr/lib/rpm/macros.php
%define		_class		Science
%define		_subclass	Chemistry
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - manipulate chemical objects: atoms, molecules, etc
Summary(pl):	%{_pearname} - manipulacje na klasach objektów chemicznych
Name:		php-pear-%{_pearname}
Version:	1.0.3
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
General classes to represent Atoms, Molecules and Macromolecules. Also
parsing code for PDB, CML and XYZ file formats. Examples of parsing
and conversion to/from chemical structure formats.

%description -l pl
Ogólna klasa reprezentuj±ca atomy, moleku³y oraz makromoleku³y. Tak¿e
parsowanie kodu w formatach PDB, CML oraz XYZ. Zawiera w dokumentacji
przyk³ady parsowania oraz konwersji z/do formatów struktur
chemicznych.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/%{_subclass}/{{doc,test}/*,README*,TODO}
%dir %{php_pear_dir}/%{_class}/%{_subclass}/
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
