%define module    qtawesome
%define pypi_name QtAwesome

Name:           python-%{module}
Version:        1.2.3
Release:        1
Summary:        Iconic fonts in PyQt and PySide applications
Group:          Development/Python
License:        MIT and OFL
URL:            https://github.com/spyder-ide/qtawesome
Source0:        https://github.com/spyder-ide/%{module}/archive/v%{version}/%{module}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)

Requires: python3dist(qtpy)

%{?python_provide:%python_provide python3-%{module}}

%description
QtAwesome enables iconic fonts such as Font Awesome and Elusive
Icons in PyQt and PySide applications.

#----------------------------------------------------

%prep
%autosetup -n %{module}-%{version}

%build
%py_build

%install
%py_install

%files
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{_bindir}/qta-browser
%{python_sitelib}/%{module}/
%{python_sitelib}/%{pypi_name}-%{version}-py%{python_version}.egg-info
