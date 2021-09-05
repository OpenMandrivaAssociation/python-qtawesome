%define module    qtawesome
%define pypi_name QtAwesome

Name:           python-%{module}
Version:        1.0.2
Release:        %mkrel 2
Summary:        Iconic fonts in PyQt and PySide applications (Python 2)
Group:          Development/Python
License:        MIT and OFL
URL:            https://github.com/spyder-ide/qtawesome
Source0:        https://github.com/spyder-ide/%{module}/archive/v%{version}/%{module}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)

%description
QtAwesome enables iconic fonts such as Font Awesome and Elusive
Icons in PyQt and PySide applications.

#----------------------------------------------------

%package -n     python3-%{module}
Summary:        Iconic fonts in PyQt and PySide applications (Python 3)
Group:          Development/Python
BuildArch:      noarch
%{?python_provide:%python_provide python3-%{module}}

%description -n python3-%{module}
QtAwesome enables iconic fonts such as Font Awesome and Elusive
Icons in PyQt and PySide applications.

#----------------------------------------------------

%prep
%autosetup -n %{module}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{module}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{_bindir}/qta-browser
%{python3_sitelib}/%{module}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
